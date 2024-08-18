# Postmortem Report

## 504 Error while accessing a given URL

<p align="center">
<img src="https://raw.githubusercontent.com/joeldmrany/alx-system_engineering-devops/main/0x19-postmortem/image.gif" width=100% height=100% />
</p>

### Incident report for [504 error / Site Outage](https://github.com/joeldmrany/alx-system_engineering-devops/main/0x17-web_stack_debugging_3)

#### Summary

The server fell down at midnight on August 15, 2024, causing a 504 error for anyone attempting to access a website. An explanation of the server's LAMP stack foundation.

#### Timeline

- **00:00 PST** - 500 error for anyone trying to access the website
- **00:05 PST** - Ensuring Apache and MySQL are up and running.
- **00:10 PST** - The website was not loading properly which on background check revealed that the server was working properly as well as the database.
- **00:12 PST** - After quick restart to Apache server returned a status of 200 and OK while trying to curl the website.
- **00:18 PST** - Reviewing error logs to check where the error might be coming from.
- **00:25 PST** - Check /var/log to see that the Apache server was being prematurely shut down. The error log for PHP were nowhere to be found.
- **00:30 PST** - Checking php.ini settings revealed all error logging had been turned off. Turning the error logging on.
- **00:32 PST** - Restarting apache server and going to the error logs to check what is being logged into the php error logs.
- **00:36 PST** - Reviewing error logs for php revealed a mistyped file name which was resulting in incorrect loading and premature closing of apache.
- **00:38 PST** - Fixing file name and restarting Apache server.
- **00:40 PST** - Server is now running normally and the website is loading properly.


#### Root Cause and Resolution

The wp-settings.php file's incorrect file name reference was the root of the problem. The server responded with an error code of 500 when the attempt to curl the server was made. It was discovered through reviewing the error logs that no error log file was being written for PHP failures, and there was little information about the server's premature shutdown to be obtained in reading the default error log for Apache. The engineer decided to check the php.ini file's error log settings after realizing that the php errors were not being sent anywhere and discovered that all error logging had been disabled.
After being enabled, the Apache server's error logging was restarted to see if any issues were showing up in the log. The php log confirmed what was expected: the wp-settings.php file did not contain a file with the.phpp extension. This was obviously a typographical error that caused the site access error. Since the issue was only discovered in one server, it's possible that it was also duplicated in other servers. Fixing the file extension with puppet would be a simple solution that would also affect other servers. After the puppet code was quickly deployed and all misspelled file extensions were changed to the correct ones, the server was restarted, and the site and server loaded correctly.

#### Corrective and Preventive Measures

- Error logging ought to be enabled on all servers and websites in order to quickly discover problems in the event that they arise.
- Before going live on a multi-server configuration, all servers and sites should be checked locally. This will allow for the correction of faults and shorten the recovery time in the event that a site goes down.
