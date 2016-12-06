# Linux Execution Filter Samples
Execution filter on Linux compute nodes allows cluster admin to plugin customized scripts to be executed (under root) on Linux compute node during different stage of job/task execution.

Following is two execution filter samples used in Linux Active Directory integrated environment.
### Sample 1: Compose customized active directory user name
**ResolveUserName.py** is a sample script to compose an Active Directory user name. For an Active Directory integrated Linux environment, it is necessary to compose the RunAs user with different settings, such as: 'winbind seperator' set in /etc/samba/smb.conf for Winbind or 're_expression' set in /etc/sssd/sssd.conf for SSSD to ensure HPC jobs are run as the correct user.

### Sample 2: Compose customized active directory user name, and mount a SMB share if the user is not an HPC administrator.
**ResolveUserNameAndDoMount.py** is a sample script to compose an Active Directory user name, and mount a SMB share if the user is not an HPC administrator. It reuses **ResolveUserName.py** to compose the Active Directory user name.  