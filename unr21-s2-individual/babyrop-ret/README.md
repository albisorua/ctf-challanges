Babyrop needed a rop-chain attack. Fortunately we were given some `pops` for
`rdi`, `rsi` and `rdx` that we could use in order to exploit the program.
The only thing that we didn't had was a gadget that allowed us to write in
`rax` the number for the execve syscall, but we were still able to call
the syscall for read and we will end up with the number of bytes that were
read in `rax`.

Only one thing remains, to write the string for the sh command. This step
can be combined with the write for `rax`. We just have to put at the start
of our input the following `'/bin/sh\x00' + (0x3b - 0x8) * b'A'`.

In order to find a good memory area to write I used gdb peda and the command
`vmmap` in order to identify a good area to write. `0x4040000` was a good
candidate. After getting all the pieces of the puzzle in place and running
the payload on the remote host I got the shell and found the flag using
the following command:

```
find / -name flag 2>/dev/null
```

The flag was:

```
CTF{2018f151xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
```

Also a good resource:

https://book.hacktricks.xyz/exploiting/linux-exploiting-basic-esp/rop-syscall-execv
