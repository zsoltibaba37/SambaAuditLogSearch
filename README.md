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

- The usernames.txt include the user names, line by line.
```
Marky
Ricky
Danny
Terry
Mikey
Davey
Timmy
Tommy
Joey
Robby
Johnny
Brian
```

#### Important

**The "ausearch.py" program does not check the contents of the AUDIT_LOG folder.**

**Opens everything that find in it. (all .txt files)**

**Therefore, you should check the contents of the folder before starting it.**

#### Usage

```
Windows
> ausearch.py usernames.txt d:\somewhere\audit_log

or

Linux
$ ./ausearch.py usernames.txt /AUDIT_LOG
```

#### Note

Returns results back in time. If there are 2135 matches and the choice is 20.

Then the program show the last 20 line.
