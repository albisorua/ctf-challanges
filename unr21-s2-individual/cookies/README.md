Analysing the binary we observe the followings:

1. Is protected by a canary (using `checksec`).

2. The vulnerable function is executing 2 reads and 2 printfs.

What we could do is to leak the canary using a payload of this form:

```
<num> * b'A' + b'%s'
```

And reading the canary since we were given full control over `printf`'s
arguments. After we read the first time we inject the leaking mechanism
and then on the second read we realise the overflow with a address that
jumps inside the `getshell` function.

The flag was:

```
CTF{1f94c05a1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```
