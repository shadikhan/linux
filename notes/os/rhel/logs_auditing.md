# [Understanding Linux logs and audits](https://www.youtube.com/watch?v=l095ciYQMYg)

## Exploring the VAR log directory 

``` bash
(.venv) shad@linux:/var/log$ ls
README                 auth.log       cloud-init-output.log  dmesg.0        dpkg.log.4.gz   lastlog      unattended-upgrades
alternatives.log       auth.log.1     cloud-init.log         dmesg.1.gz     fontconfig.log  libvirt      waagent.log
alternatives.log.1     auth.log.2.gz  cloud-init.log.1       dmesg.2.gz     journal         private      wtmp
alternatives.log.2.gz  auth.log.3.gz  cloud-init.log.2.gz    dmesg.3.gz     kern.log        syslog
alternatives.log.3.gz  auth.log.4.gz  cloud-init.log.3.gz    dmesg.4.gz     kern.log.1      syslog.1
alternatives.log.4.gz  azure          cloud-init.log.4.gz    dpkg.log       kern.log.2.gz   syslog.2.gz
apache2                btmp           cloud-init.log.5.gz    dpkg.log.1     kern.log.3.gz   syslog.3.gz
apport.log             btmp.1         dist-upgrade           dpkg.log.2.gz  kern.log.4.gz   syslog.4.gz
apt                    chrony         dmesg                  dpkg.log.3.gz  landscape       sysstat

# General system logs
(.venv) shad@linux:/var/log$ tail -n 5 /var/log/syslog
2026-02-02T02:52:02.844255+00:00 linux python3[846]: 2026-02-02T02:52:02.843840Z INFO Daemon Daemon Agent WALinuxAgent-2.15.0.1 launched with command '/usr/bin/python3 -u bin/WALinuxAgent-2.15.0.1-py3.12.egg -run-exthandlers' is successfully running
2026-02-02T02:55:01.610581+00:00 linux CRON[7983]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
2026-02-02T03:00:10.924452+00:00 linux systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
2026-02-02T03:00:10.929704+00:00 linux systemd[1]: sysstat-collect.service: Deactivated successfully.
2026-02-02T03:00:10.929848+00:00 linux systemd[1]: Finished sysstat-collect.service - system activity accounting tool.

# Apt logs
(.venv) shad@linux:/var/log$ tail -n 5 /var/log/apt/history.log

# Login logs
(.venv) shad@linux:/var/log$ tail -n 5 /var/log/auth.log
2026-02-02T03:09:05.547655+00:00 linux sshd[8288]: Connection closed by invalid user sol 80.94.92.171 port 59160 [preauth]
2026-02-02T03:10:01.621247+00:00 linux CRON[8389]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2026-02-02T03:10:01.623279+00:00 linux CRON[8389]: pam_unix(cron:session): session closed for user root
2026-02-02T03:12:47.681987+00:00 linux sshd[8396]: Invalid user ubuntu from 80.94.92.171 port 34104
2026-02-02T03:12:47.807276+00:00 linux sshd[8396]: Connection closed by invalid user ubuntu 80.94.92.171 port 34104 [preauth]
```

## Using Logger to write logs

``` bash
(.venv) shad@linux:/var/log$ logger "james harden"
(.venv) shad@linux:/var/log$ tail -n 1 /var/log/syslog
2026-02-02T03:16:42.921913+00:00 linux shad: james harden

(.venv) shad@linux:/var/log$ logger -p authpriv.warn "An auth event"
(.venv) shad@linux:/var/log$ tail -n 1 /var/log/auth.log
2026-02-02T03:18:31.712915+00:00 linux shad: An auth event

(.venv) shad@linux:/var/log$ logger --id=67 "another log"
(.venv) shad@linux:/var/log$ tail -n 1 /var/log/syslog
2026-02-02T03:42:25.515553+00:00 linux shad[67]: another log
```

## Syslog configuration

``` bash
(.venv) shad@linux:/var/log$ cat /etc/rsyslog.d/50-default.conf
#  Default rules for rsyslog.
#
#                       For more information see rsyslog.conf(5) and /etc/rsyslog.conf

#
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log


```