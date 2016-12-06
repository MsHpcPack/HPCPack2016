#!/usr/bin/env python
# Hpc Execution Filter Sample - Compose Customized Active Directory User Name and Do Mount For Non-Admin Users
# This script reuse ResolveUserName.py to compose right Active Directory user name,
# and do mount for Non-Admin users. 
#
# The sample fulfils the following scenario:
# Administrators use HPC Linux Support with Active Directory Integrated,
# and provide SMB Shares with pattern //SmbShareBasePath/UserName for each Active Directory User to do data movement.  
# Administrators wish to ensure the shares can be mounted for different users. 
# In this script, the specific SMB share will be mounted to the share folder in each users' home directory, 
# with uid and gid set correspondingly, and file_mode and dir_mode both set to 755.
#
# Please notice this sample script will parse the password of users for mounting, 
# and be sure this aligns security policies before using it in production environments. 
# 
# Return codes:
# This script follow command mount's return codes:
# 0      success
# 1      incorrect invocation or permissions
# 2      system error (out of memory, cannot fork, no more loop devices)
# 4      internal mount bug
# 8      user interrupt
# 16     problems writing or locking /etc/mtab
# 32     mount failure
# 64     some mount succeeded
# For more about mount's return codes, please refer man 8 mount.

import json
import os
import pwd
import string
import subprocess
import sys
import time
import ResolveUserName

"""Define the constants."""
SmbShareBasePath = "//[SmbShareSever]/SmbShareDemo"

def MountSmbShare(smbSharePath, targetPath, domainName, userName, password, uid, gid, fileMode="0755", dirMode="0755"):
    retCode = 0
    if os.path.ismount(targetPath) == False:
        maxRetry = 3
        while(maxRetry > 0):
            retCode = Run("mount -t cifs {0} {1} -o domain={2},username={3},password='{4}',uid={5},gid={6},file_mode={7},dir_mode={8}".format(smbSharePath, targetPath, domainName, userName, password, uid, gid, fileMode, dirMode))
            """Check if succeeded, and skip the case when another process successfully mount the share."""
            if retCode == 0 or os.path.ismount(targetPath):
                retCode = 0
                break
            maxRetry = maxRetry - 1     
            time.sleep(1)
    return retCode

"""Run command facilities."""
if not hasattr(subprocess,'check_output'):
    def check_output(*popenargs, **kwargs):
        r"""Backport from subprocess module from python 2.7"""
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be overridden.')
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise subprocess.CalledProcessError(retcode, cmd, output=output)
        return output

    # Exception classes used by this module.
    class CalledProcessError(Exception):
        def __init__(self, returncode, cmd, output=None):
            self.returncode = returncode
            self.cmd = cmd
            self.output = output
        def __str__(self):
            return "Command '%s' returned non-zero exit status %d" % (self.cmd, self.returncode)

    subprocess.check_output=check_output
    subprocess.CalledProcessError=CalledProcessError

def Run(cmd,chk_err=True):
    retcode,out=RunGetOutput(cmd,chk_err)
    return retcode

def RunGetOutput(cmd,chk_err=True):
    try:
        output=subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except subprocess.CalledProcessError,e :
        if chk_err :
            Error('CalledProcessError.  Error Code is ' + str(e.returncode)  )
            Error('CalledProcessError.  Command result was ' + (e.output[:-1]).decode('latin-1'))
        return e.returncode,e.output.decode('latin-1')
    return 0,output.decode('latin-1')
"""End of run command facilities."""

"""
Logging facilities can be removed from the script.
Log can be used for trouble shooting, and remember to comment them out when performance is considered more important.
"""
LocalTime = time.localtime()
ExecutionFilterSampleLogFile = "./ExecutionFilter_ResolveUserAndMount_%04u%02u%02u-%02u%02u%02u.log" % (LocalTime.tm_year, LocalTime.tm_mon, LocalTime.tm_mday, LocalTime.tm_hour, LocalTime.tm_min, LocalTime.tm_sec)
def LogWithPrefix(prefix, message):
    t = time.localtime()
    t = "%04u/%02u/%02u %02u:%02u:%02u " % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    t += prefix
    for line in message.split('\n'):
        line = t + line
        line = filter(lambda x : x in string.printable, line)
        try:
            with open(ExecutionFilterSampleLogFile, "a") as F :
                F.write(line.encode('ascii','ignore') + "\n")
        except IOError, e:
            pass

def Log(message):
    LogWithPrefix("INFO: ", message)

def Error(message):
    LogWithPrefix("ERROR: ", message)

def Warn(message):
    LogWithPrefix("WARNING: ", message)
"""End of logging facilities."""
    
def Main():
    retCode = 0

    """The input is job execution context in json format."""
    jsonData = json.loads(sys.stdin.readline())
    try:
        """Get user name, by default it's in domain\username format."""
        composedUserName = jsonData["m_Item3"]
        runAsUserInfo = composedUserName.split('\\')
        if len(runAsUserInfo) < 2:
            Error("Illegal input runAsUser: {0}, be sure the input is hpc job context in json format.".format(composedUserName))
            sys.exit(1)
        domainName = runAsUserInfo[0]
        userName = runAsUserInfo[1]
        
        """Resolve right Active Directory user name."""
        composedUserName = ResolveUserName.ComposeAdUserName(domainName, userName)

        """Query if the user is admin, and mount for Non-Admin users."""
        isAdmin = "0"
        try:
            isAdmin = jsonData["m_Item2"]["environmentVariables"]["CCP_ISADMIN"]
        except KeyError:
            pass

        if isAdmin == "0":
            """Check whether user exists, touch user's home dir, and get user information."""
            retCode = Run("mkhomedir_helper {0}".format(composedUserName))
            if retCode != 0:
                Error("No such user: {0}, or home directory for this user cannot be used or generated properly.".format(composedUserName))
                sys.exit(1)

            pwdInfo = pwd.getpwnam(composedUserName)
            uid = pwdInfo.pw_uid
            gid = pwdInfo.pw_gid
            homeDir = pwdInfo.pw_dir

            """Get password, please note the risk here."""
            password = jsonData["m_Item4"]

            """Do mount for Non-Admin users."""
            smbSharePath = "{0}/{1}".format(SmbShareBasePath, userName)
            targetPath = "{0}/share".format(homeDir)
            retCode = Run("mkdir -p {0}".format(targetPath))
            if retCode != 0:
                Error("Cannot find and create mount target path: {0}".format(targetPath))
                sys.exit(1)

            retCode = MountSmbShare(smbSharePath, targetPath, domainName, userName, password, uid, gid)

        """Set composedUserName."""
        jsonData["m_Item3"] = composedUserName
        
    except KeyError:
        """Please check whether the script is used correctly."""
        Error("Please check whether the script is used correctly, and ensure it get right format job context json.")
        retCode = 1
    
    """Return the result through stdout."""
    print json.dumps(jsonData)

    #Log("ExecutionFitler finished with retCode:{0}".format(retCode))
    sys.exit(retCode)

if __name__ == '__main__':
    Main()
