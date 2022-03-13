The idea for a good one was to observe the the flag located at the `enc_flag`
label in gdb peda was pointing to your encrypted flag. The flag had the length
0x45 and in order to decrypt it each character had to be xored with the length
an there was the flag.

```
CTF{fc3a41xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
