SambaAuditLogSearch
-----

### First step

- <a href="http://linux-sys-adm.com/ubuntu-16.04-lts-how-to-configure-samba-full-audit/">How To Configure SAMBA Full Audit.</a>


- Create a bash script (of course chmod 775), and copy to /usr/local/bin folder.
Name is as you want. I name it audit_file_copy.

```
#!/bin/bash
#
cat /var/log/samba/audit.log > /AUDIT_LOG/audit_files_$(date +%F).txt
```
- I setup the crontab, to run Monday to Saturday. Ones a day copy the audit.log file to /AUDIT_LOG folder.

```
$ crontab -e
#---------------------------------------
#
# m h  dom mon dow   command
00 13 * * 1-6 /usr/local/bin/audit_file_copy
```

### Install
```
sudo cp -p pyause /usr/local/bin/

sudo chown root:root /usr/local/bin/*
```

### Usage

```
$ pyause /AUDIT_LOG


 Short help

$ pyause -h 

or

$ pyause -help

```

### Important
**It can now only be used with "sudo".**

**Bash script integrated the python code.**

**Reads only 'txt' files from the target directory.**

### Note

Returns results back in time. If there are 2135 matches and the choice is 20.

Then the program show the last 20 line.

### Version

1.3 - Bigger repair. The 'inputcheck.py' built in.
1.2 - Python code Include the bash script.
