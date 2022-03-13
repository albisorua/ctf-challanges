We start debugging with `x64dbg` and at some point we notice those lines:

```
00007FF6D5245D8F | FF15 93320200            | call qword ptr ds:[<&GetCommandLineW>]                                                                                                      |
00007FF6D5245D95 | 45:33C9                  | xor r9d,r9d                                                                                                                                 |
00007FF6D5245D98 | 4C:8D4424 58             | lea r8,qword ptr ss:[rsp+58]                                                                                                                |
00007FF6D5245D9D | 48:8BD0                  | mov rdx,rax                                                                                                                                 | rax:L"\"C:\\Users\\andre\\Downloads\\src.exe\""
00007FF6D5245DA0 | 48:8D8C24 00010000       | lea rcx,qword ptr ss:[rsp+100]                                                                                                              |
00007FF6D5245DA8 | 48:8D4424 70             | lea rax,qword ptr ss:[rsp+70]                                                                                                               |
00007FF6D5245DAD | 48:894424 48             | mov qword ptr ss:[rsp+48],rax                                                                                                               |
00007FF6D5245DB2 | 48:8D8424 90000000       | lea rax,qword ptr ss:[rsp+90]                                                                                                               |
00007FF6D5245DBA | 48:894424 40             | mov qword ptr ss:[rsp+40],rax                                                                                                               |
00007FF6D5245DBF | 48:897C24 38             | mov qword ptr ss:[rsp+38],rdi                                                                                                               |
00007FF6D5245DC4 | 48:897C24 30             | mov qword ptr ss:[rsp+30],rdi                                                                                                               |
00007FF6D5245DC9 | 897C24 28                | mov dword ptr ss:[rsp+28],edi                                                                                                               |
00007FF6D5245DCD | 895C24 20                | mov dword ptr ss:[rsp+20],ebx                                                                                                               |
00007FF6D5245DD1 | FF15 01330200            | call qword ptr ds:[<&CreateProcessW>]
```

Those were creating a process that was running behind a binary created from a python wheel.
We notice this by calling `strings` command on `src.exe`. We extract that data using:

```
https://github.com/extremecoders-re/pyinstxtractor
```

We issue this command:

```
python3.7 pyinstractor/pyinstractor.py src.exe
```

And we get the `.pyc` file. From that we use:

```
uncompyle6 -o . src.pyc
```                    

And we get the `src.py`:

```
# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.10 (default, Sep 28 2021, 16:10:42)
# [GCC 9.3.0]
# Embedded file name: src.py
from Crypto.Cipher import Salsa20
k = bytes([202, 254, 186, 190, 80, 114, 97, 105, 115, 101, 84, 104, 101, 83, 117, 110])
no = bytes([76, 105, 118, 105, 97, 110, 222, 173])
cipher = Salsa20.new(key=k, nonce=no)
flag = [17, 223, 36, 154, 167, 98, 74, 38, 104, 27, 127, 85, 67, 37, 202, 173, 164, 152, 105, 244, 239, 123, 100, 178, 106, 212, 197, 10, 226, 141, 45, 74]
input = input('Enter the password: ').strip()
print(input)
encrypted = cipher.encrypt(input.encode('utf-8'))
if encrypted == bytes(flag):
    print('O_O...Nice man xD...now that you learned some tricks, go get your points :D')
else:
    print('Nope...good luck reversing this')
```                                       

The flag was encrypted with `Salsa20`. We decrypt it and we get:

```
UNBR{Nicee_u_know_sum_py_trickz}
```
