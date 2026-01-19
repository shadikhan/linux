# [Understanding Logging in Linux](https://www.youtube.com/watch?v=6uP_f_z3CbM)

## nice to know

- `tail -f <logfile>` - follow a log file in real-time.
- `tail -n 100 <logfile>` - show last 100 lines of a log file.
- `journalctl -xeu <service> -f` - follow logs for a specific systemd service in real-time

## apt logs (ubuntu)

``` bash
# Install cowsay to generate some log entries
(.venv) shad@linux:/var/log$ sudo apt install cowsay

# history.log - high-level transactions. What changed and who did it?
(.venv) shad@linux:/var/log$ cat /var/log/apt/history.log

Start-Date: 2026-01-18  05:26:03
Commandline: apt install cowsay
Requested-By: shad (1000)
Install: cowsay:amd64 (3.03+dfsg2-8)
End-Date: 2026-01-18  05:26:10

# term.log - Execution details. What happened during the install?
(.venv) shad@linux:/var/log$ cat /var/log/apt/term.log

Log started: 2026-01-18  05:26:03
Selecting previously unselected package cowsay.
(Reading database ... 104751 files and directories currently installed.)
Preparing to unpack .../cowsay_3.03+dfsg2-8_all.deb ...
Unpacking cowsay (3.03+dfsg2-8) ...
Setting up cowsay (3.03+dfsg2-8) ...
Processing triggers for man-db (2.12.0-4build2) ...
Log ended: 2026-01-18  05:26:10

# dpkg logs - Package state
(.venv) shad@linux:/var/log$ grep "cowsay" /var/log/dpkg.log
2026-01-18 05:26:05 install cowsay:all <none> 3.03+dfsg2-8
2026-01-18 05:26:05 status half-installed cowsay:all 3.03+dfsg2-8
2026-01-18 05:26:05 status unpacked cowsay:all 3.03+dfsg2-8
2026-01-18 05:26:05 configure cowsay:all 3.03+dfsg2-8 <none>
2026-01-18 05:26:05 status unpacked cowsay:all 3.03+dfsg2-8
2026-01-18 05:26:05 status half-configured cowsay:all 3.03+dfsg2-8
2026-01-18 05:26:05 status installed cowsay:all 3.03+dfsg2-8
```

## wtmp

``` bash
# Binary log, not a simple text file
# Indicates that we need to use a command to view that log file properly
(.venv) shad@linux:/var/log$ cat /var/log/wtmp

# wtmp - tracks logins, logouts, system boots, and shutdowns
(.venv) shad@linux:/var/log$ last
reboot   system boot  6.14.0-1017-azur Sun Jan 18 04:15   still running
reboot   system boot  6.14.0-1017-azur Tue Dec 30 21:34 - 08:01  (10:26)
reboot   system boot  6.14.0-1014-azur Thu Dec 18 19:48 - 08:01  (12:12)
reboot   system boot  6.14.0-1014-azur Mon Dec 15 18:31 - 08:01  (13:30)
reboot   system boot  6.14.0-1014-azur Mon Dec 15 02:35 - 08:00  (05:25)
reboot   system boot  6.14.0-1014-azur Sat Dec 13 18:21 - 08:00  (13:39)
reboot   system boot  6.14.0-1014-azur Wed Dec 10 20:52 - 08:00  (11:08)
shad     pts/0        <hidden ip>    Tue Dec  9 19:05 - 22:04  (02:59)
reboot   system boot  6.14.0-1014-azur Tue Dec  9 19:05 - 08:00  (12:55)
reboot   system boot  6.14.0-1014-azur Sun Dec  7 08:01 - 08:00  (23:59)
reboot   system boot  6.14.0-1014-azur Sat Dec  6 18:53 - 08:00  (13:07)
reboot   system boot  6.14.0-1014-azur Fri Dec  5 18:06 - 08:00  (13:54)
reboot   system boot  6.14.0-1014-azur Thu Dec  4 03:36 - 08:01  (04:24)
shad     pts/0        <hidden ip>    Thu Dec  4 03:34 - 03:36  (00:01)
shad     pts/0        <hidden ip>    Thu Dec  4 03:24 - 03:24  (00:00)
...
wtmp begins Fri Oct 17 20:42:28 2025

```

## btmp

``` bash
# Binary log, not a simple text file
(.venv) shad@linux:/var/log$ sudo cat /var/log/btmp

# btmp - tracks failed login attempts
# below happened when I tried to login to the server with a wrong user
(.venv) shad@linux:/var/log$ sudo lastb
linux    ssh:notty    <hidden ip>     Sun Jan 18 06:04 - 06:04  (00:00)
```

## auth.log

``` bash
# auth.log - authentication-related events
(.venv) shad@linux:/var/log$ sudo cat /var/log/auth.log
2026-01-19T02:13:06.149427+00:00 linux sshd[9333]: Invalid user goat from <hidden-ip> port 64183
2026-01-19T02:13:06.265316+00:00 linux sshd[9333]: Connection reset by invalid user goat <hidden-ip> port 64183 [preauth]
2026-01-19T02:13:17.102485+00:00 linux sshd[9335]: Accepted publickey for shad from <hidden-ip> port 64185 ssh2: RSA SHA256:<hidden>
2026-01-19T02:13:17.104496+00:00 linux sshd[9335]: pam_unix(sshd:session): session opened for user shad(uid=1000) by shad(uid=0)
2026-01-19T02:13:17.110128+00:00 linux systemd-logind[805]: New session 16 of user shad
```

## syslog

``` bash
# General system activity log (ex. hardware issues, system events, etc.)
(.venv) shad@linux:/var/log$ tail -n 25 /var/log/syslog
```

## dmesg

``` bash
# Kernel ring buffer - boot and hardware related messages
(.venv) shad@linux:/var/log$ sudo dmesg | tail -n 25
```
