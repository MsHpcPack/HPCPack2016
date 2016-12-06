#!/usr/bin/env python
# Hpc Execution Filter Sample - Compose Customized Active Directory User Name
# Introduction:
# When it's in an Active Directly integrated Linux environment,
# it's necessary to compose right RunAs user with different settings,
# such as: 'winbind seperator' set in /etc/samba/smb.conf for Winbind
# or 're_expression' set in /etc/sssd/sssd.conf for SSSD.
# to ensure right user is used when HPC run jobs.
#
# In this case, we compose RunAs user, for example:
# composedUserName = "{0}.{1}".format(domainName, userName) when Winbind Seperator set to . delimiter
# or In SSSD, when set re_expression = ((?P<domain>.+)\.(?P<name>[^\\\.@]+$))
#
# Return codes:
# 0      success
# 1      incorrect invocation 

import json
import sys

def ComposeAdUserName(domainName, userName):
    """
    Examples:
    composedUserName = "{0}@{1}".format(userName, domainName), when using userName@domainName
    """
    composedUserName = "{0}.{1}".format(domainName, userName)
    return composedUserName

def Main():
    """The input is job execution context in json format."""
    jsonData = json.loads(sys.stdin.readline())

    """Get and compose user name, by default it's in domain\username format."""
    composedUserName = jsonData["m_Item3"]
    runAsUserInfo = composedUserName.split('\\')
    if len(runAsUserInfo) == 2:
        domainName = runAsUserInfo[0]
        userName = runAsUserInfo[1]
        composedUserName = ComposeAdUserName(domainName, userName)

    """Set composedUserName."""
    jsonData["m_Item3"] = composedUserName

    """Return the result through stdout"""
    print json.dumps(jsonData)

    sys.exit(0)

if __name__ == '__main__':
    Main()

