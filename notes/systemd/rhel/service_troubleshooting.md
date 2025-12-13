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

