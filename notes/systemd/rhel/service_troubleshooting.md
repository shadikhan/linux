# Service Troubleshooting

## Services Toolbox

- Tools will be relevant to systemd services.

``` bash
shad@linux:~/linux/notes/systemd$ systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; disabled; preset: enabled)
     Active: active (running) since Sun 2025-12-07 08:01:32 UTC; 11min ago
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 926 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 944 (sshd)
      Tasks: 1 (limit: 9444)
     Memory: 5.0M (peak: 7.5M)
        CPU: 583ms
     CGroup: /system.slice/ssh.service
             └─944 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

shad@linux:~/linux/notes/systemd$ sudo systemctl edit apache2
Successfully installed edited file '/etc/systemd/system/apache2.service.d/override.conf'.

# systemd stores the outputs of a lot of things that it runs and manages in the system journal.
# xe flag shows the most recent log entries with extra detail.
shad@linux:~/linux/notes/systemd$ journalctl -xe
 The job identifier is 1285.
Dec 07 08:15:43 linux sshd[2402]: Received disconnect from 193.46.255.99 port 33800:11:  [preauth]
Dec 07 08:15:43 linux sshd[2402]: Disconnected from authenticating user root 193.46.255.99 port 33800 [preauth]
Dec 07 08:15:52 linux sshd[2404]: Received disconnect from 101.36.113.241 port 33718:11: Bye Bye [preauth]
Dec 07 08:15:52 linux sshd[2404]: Disconnected from authenticating user root 101.36.113.241 port 33718 [preauth]
Dec 07 08:16:32 linux systemd[1]: Starting systemd-tmpfiles-clean.service - Cleanup of Temporary Directories...
 Subject: A start job for unit systemd-tmpfiles-clean.service has begun execution
 Defined-By: systemd
 Support: http://www.ubuntu.com/support
 
 A start job for unit systemd-tmpfiles-clean.service has begun execution.
 
 The job identifier is 1409.
Dec 07 08:16:32 linux systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
 Subject: Unit succeeded
 Defined-By: systemd
 Support: http://www.ubuntu.com/support
 
 The unit systemd-tmpfiles-clean.service has successfully entered the 'dead' state.
Dec 07 08:16:32 linux systemd[1]: Finished systemd-tmpfiles-clean.service - Cleanup of Temporary Directories.
 Subject: A start job for unit systemd-tmpfiles-clean.service has finished successfully
 Defined-By: systemd
 Support: http://www.ubuntu.com/support
 
 A start job for unit systemd-tmpfiles-clean.service has finished successfully.
 
 The job identifier is 1409.

# ss shows you all the open sockets on the system, along with the processes that own them (for local connections).
# Gives you a nice summary of tcp and udp connections, by ip addresses, what process is running. 
shad@linux:~/linux/notes/systemd$ sudo ss -tupnl
Netid         State          Recv-Q          Send-Q                   Local Address:Port                    Peer Address:Port         Process                                                                                                                               
udp           UNCONN         0               0                           127.0.0.54:53                           0.0.0.0:*             users:(("systemd-resolve",pid=533,fd=16))                                                                                            
udp           UNCONN         0               0                        127.0.0.53%lo:53                           0.0.0.0:*             users:(("systemd-resolve",pid=533,fd=14))                                                                                            
udp           UNCONN         0               0                        10.0.0.4%eth0:68                           0.0.0.0:*             users:(("systemd-network",pid=694,fd=21))                                                                                            
udp           UNCONN         0               0                            127.0.0.1:323                          0.0.0.0:*             users:(("chronyd",pid=925,fd=6))                                                                                                     
udp           UNCONN         0               0                                [::1]:323                             [::]:*             users:(("chronyd",pid=925,fd=7))                                                                                                     
tcp           LISTEN         0               4096                     127.0.0.53%lo:53                           0.0.0.0:*             users:(("systemd-resolve",pid=533,fd=15))                                                                                            
tcp           LISTEN         0               4096                           0.0.0.0:22                           0.0.0.0:*             users:(("sshd",pid=944,fd=3),("systemd",pid=1,fd=164))                                                                               
tcp           LISTEN         0               1024                         127.0.0.1:35231                        0.0.0.0:*             users:(("code-bf9252a2fb",pid=1453,fd=10))                                                                                           
tcp           LISTEN         0               4096                        127.0.0.54:53                           0.0.0.0:*             users:(("systemd-resolve",pid=533,fd=17))                                                                                            
tcp           LISTEN         0               511                                  *:80                                 *:*             users:(("apache2",pid=2922,fd=4),("apache2",pid=2921,fd=4),("apache2",pid=2919,fd=4))                                                
tcp           LISTEN         0               4096                              [::]:22                              [::]:*             users:(("sshd",pid=944,fd=4),("systemd",pid=1,fd=165))                                                                               

```

## Service Failure

``` bash
# This gives us: Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.
shad@linux:~/linux$ systemctl start apache2

shad@linux:~/linux$ journalctl --help | grep -e '-x ' -e '-u ' -e '-e '
  -u --unit=UNIT             Show logs from the specified unit
  -x --catalog               Add message explanations where available
  -e --pager-end             Immediately jump to the end in the pager


shad@linux:~/linux$ journalctl -xeu apache2
~
~
~
~
~
Dec 13 18:55:12 linux systemd[1]: Starting apache2.service - Apache is chill...
░░ Subject: A start job for unit apache2.service has begun execution
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A start job for unit apache2.service has begun execution.
░░ 
░░ The job identifier is 2159.
Dec 13 18:55:12 linux systemd[1]: Started apache2.service - Apache is chill.
░░ Subject: A start job for unit apache2.service has finished successfully
░░ Defined-By: systemd
░░ Support: http://www.ubuntu.com/support
░░ 
░░ A start job for unit apache2.service has finished successfully.
░░ 
░░ The job identifier is 2159.

# For us, we're good. Let's imagine that we got:
Dec 13 18:55:12 linux apache2[3000]: AH00526: Syntax error on line 47 of /etc/apache2/apache2.conf:
# Lol, classic apache misconfiguration.

# It even diagnosed the problem for us!
Dec 13 18:55:12 linux apache2[3000]: Port was replaced with Listen in Apache 2.0

shad@linux:~/linux$ cat /etc/apache2/apache2.conf 
Port 80

# Port used to be how apache specified what port to listen on.
# In Apache 2.0 and later, it's "Listen". So we just need to change that line.
Listen 80

# Now we see that the service is active (running).
shad@linux:~/linux$ sudo systemctl start apache2

# Some other services may also use syslog for their logging.
# We see some apache2 logs in /var/log/messages.
# Remember that not all services use systemd-journald for logging! Some log aggregators might raight to /var/log/.
# Note: /var/log/messages is a RHEL/CentOS log file. Ubuntu uses /var/log/syslog instead.
shad@linux:~/linux$ tail -n 30 /var/log/messages

## To see if a service is logging to journal (-p is --property):
shad@linux:~/linux$ systemctl show apache2 -p StandardOutput
StandardOutput=journal

## To generally see it's config:
shad@linux:~/linux$ systemctl cat apache2
```

## Port Permission Failure

``` bash
# This gives us: Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.
shad@linux:~/linux$ systemctl start apache2

shad@linux:~/linux$ journalctl -xeu apache2

# Something on the system has prevented apache from binding to port 8000.
# It is port 8000, which is not a privileged port, so it is not a permission issue with root vs non-root.
Dec 13 19:10:45 linux apache2[3500]: (13)Permission denied: AH00072: make_sock: could not bind to address [::]:8000
Dec 13 19:10:45 linux apache2[3500]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8000

# Probably SELinux is preventing it. Note, I'm on Ubuntu, which doesn't have SELinux by default.
# This is for a RHEL-based system with SELinux enabled.
# Note: /var/log/messages is a RHEL/CentOS log file. Ubuntu uses /var/log/syslog instead.
shad@linux:~/linux$ tail -n 30 /var/log/messages

Dec 13 19:10:45  setroubleshoot[4000]: SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 8000. If you believe that httpd should be allowed name_bind access on the tcp_socket port 8000 then you should report this as a bug. You can generate a local policy module to allow this access. 

# For this example, there was another typo in the apache config file, where we wrote "Listen 8000" instead of "Listen 80".
shad@linux:~/linux$ nano /etc/apache2/apache2.conf 
Listen 80

# Without SELinux, we can still have port problems
shad@linux:~/linux$ setenforce 0   # Temporarily disable SELinux (RHEL-based systems only)
shad@linux:~/linux$ nano /etc/apache2/apache2.conf 
Listen 22 # We know what this one is.. shhh

# This gives us: Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.
shad@linux:~/linux$ systemctl start apache2

# Different error this time, something is attached to port 22.
shad@linux:~/linux$ journalctl -xeu apache2
Dec 13 19:25:12 linux apache2[4000]: (98)Address already in use: AH00072: make_sock: could not bind to address [::]:22
Dec 13 19:25:12 linux apache2[4000]: (98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:22

# What's using port 22?
shad@linux:~/linux$ sudo ss -tupna | grep ":22"
tcp   LISTEN 0      4096         0.0.0.0:22          0.0.0.0:*     users:(("sshd",pid=1136,fd=3),("systemd",pid=1,fd=55))                               
tcp   ESTAB  0      164         10.0.0.4:22     108.28.48.51:51471 users:(("sshd",pid=1271,fd=4),("sshd",pid=1137,fd=4))                                
tcp   LISTEN 0      4096            [::]:22             [::]:*     users:(("sshd",pid=1136,fd=4),("systemd",pid=1,fd=56))
```

## Container Networking

- Better security practice to run container as services as unprivileged users. So that if it breaks out of the container, it can't do much damage to the host system as an unprivileged user.

``` bash

# Examples are using RHEL-based system with podman.
shad@linux:~/linux$ podman run -d -p 80:80 el-httpd

Error: rootlessport cannot expose privileged port 80, you can add 'net.ipv4.ip_unprivileged_port_start=80' to /etc/sysctl.conf (currently 1024) or chose a larger port number (>= 1024): listen tcp 0.0.0.0:80: bind: permission denied

# This works because 8080 is an unprivileged port (>= 1024).
shad@linux:~/linux$ podman run -d -p 8080:80 el-httpd

# To allow unprivileged users to bind to lower ports, we can change the kernel setting.
shad@linux:~/linux$ cat /proc/sys/net/ipv4/ip_unprivileged_port_start 
1024

# Note, only root can change this setting. Also, this change is temporary and will be reset on reboot.
# sysctl would ensure persistence across reboots.
root@linux:~/linux$ echo 79 > /proc/sys/net/ipv4/ip_unprivileged_port_start
shad@linux:~/linux$ ls -lash /proc/sys/net/ipv4/ | grep unpriv
0 -rw-r--r-- 1 root root 0 Dec 13 20:35 ip_unprivileged_port_start

# Now, we can bind to port 80 as an unprivileged user.
shad@linux:~/linux$ podman run -d -p 80:80 el-httpd

``` 

## Starting at boot

``` bash
# disabled means apache2 will not start at boot.
shad@linux:~/linux$ systemctl status apache2
● apache2.service - Apache is chill
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; disabled; preset: enabled)
    Drop-In: /etc/systemd/system/apache2.service.d
             └─override.conf
     Active: active (running) since Sat 2025-12-13 18:55:12 UTC; 1h 52min ago
       Docs: https://httpd.apache.org/docs/2.4/
    Process: 3816 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
   Main PID: 3832 (apache2)
      Tasks: 55 (limit: 9434)
     Memory: 7.3M (peak: 7.8M)
        CPU: 405ms
     CGroup: /system.slice/apache2.service
             ├─3832 /usr/sbin/apache2 -k start
             ├─3835 /usr/sbin/apache2 -k start
             └─3836 /usr/sbin/apache2 -k start

Dec 13 18:55:12 linux systemd[1]: Starting apache2.service - Apache is chill...
Dec 13 18:55:12 linux systemd[1]: Started apache2.service - Apache is chill.

# Two in one: enable makes it start at boot, --now starts it right now.
shad@linux:~/linux$ systemctl enable --now apache2
```

## Unprintable Characters

``` bash
# This gives us: Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.
shad@linux:~/linux$ systemctl start apache2

shad@linux:~/linux$ journalctl -xeu apache2
Dec 13 18:55:12 linux apache2[3000]: AH00526: Syntax error on line 47 of /etc/apache2/apache2.conf:
Dec 13 18:55:12 linux apache2[3000]: Port must be specified

# We saw this earlier...

# There is two spaces after "Listen" instead of one. But I don't think apache2 cares that much about whitespace...
shad@linux:~/linux$ cat /etc/apache2/apache2.conf 
Listen  80

shad@linux:~/linux$ nano /etc/apache2/apache2.conf 
Listen 80

# This gives us: Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.
shad@linux:~/linux$ systemctl start apache2

# Huh? That's clearly a space right?
shad@linux:~/linux$ journalctl -xeu apache2
Dec 13 18:55:12 linux apache2[3000]: AH00526: Syntax error on line 47 of /etc/apache2/apache2.conf:
Dec 13 18:55:12 linux apache2[3000]: Invalid command 'Listen\xa80', perhaps misspelled or defined by a module not included in the server configuration

# Show you unprintable characters like \xa0 (non-breaking space)
shad@linux:~/linux$ cat -vet /etc/apache2/apache2.conf | less
ListenM- 80$

# Starts up just fine.
shad@linux:~/linux$ systemctl start apache2
```

- Unprintable characters can make their way into your files. Common way to get this is editing files in Windows or using the integrated Github editor. Both those editors uses "Carriage Returned and Line Feed characters" (CRLF) to indicate the end of a line. ControlM (`^M$`) is the unprintable character for CR.
- The good news is that most linux services can handle CLRF characters just fine (output from unixtodos command).

Discussion about journal log and syslog
- journal logs can be ephemeral depending on configuration, syslog logs are usually persistent on disk.
- There is a daemon called `systemctl status rsyslog`, which will take log entries from the journal and write them to /var/log/syslog or /var/log/messages depending on your distribution. Or you can have it write to some where else.
