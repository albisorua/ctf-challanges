In order to break this wireless communication just use aircrack-ng:

```
aircrack-ng -z -w /usr/share/wordlists/rockyou.txt neighborhood.pcap
```

And you get:

```

                               Aircrack-ng 1.6 

      [00:00:02] 2587/10303727 keys tested (1571.93 k/s) 

      Time left: 1 hour, 49 minutes, 13 seconds                  0.03%

                          KEY FOUND! [ mickeymouse ]


      Master Key     : 38 1B CF B7 B7 2C C4 31 C8 25 1F 27 75 EB CF 3B 
                       F3 F6 79 93 A4 94 9D 09 A7 76 41 5D 40 85 2B F6 

      Transient Key  : B7 43 A8 4F 87 16 2F 8E 07 9F 02 18 D5 B2 6C FE 
                       20 A7 BD C7 D1 5B 05 80 1F 32 23 92 0A F1 73 F4 
                       51 F5 5A 22 7E 3F D8 0E 9C 84 47 D1 91 FA 33 9D 
                       B2 D2 C4 7F 52 F4 6C F2 F7 89 14 1A 4B DE F6 00 

      EAPOL HMAC     : ED BF 01 1B CB C6 19 4B 8B 84 7E 43 6E 5A CC 4F 
```

The password was `mickeymouse` and the flag:

```
CTF{d0ff2794xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
