We have to install uncompyle6:

```
pip install uncompyle6
```

After running:

```
uncompyle6 -o . chall.cpython-36.pyc
```

We get this:

```
# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.10 (default, Sep 28 2021, 16:10:42)
# [GCC 9.3.0]
# Embedded file name: ./chall.py
# Compiled at: 2021-09-23 00:48:10
# Size of source mod 2**32: 1508 bytes
import hashlib
version = 'Python 3.6.9'

def sauhd982w1d3jg23fwue(O0O0000O000O0OO0O, O000OO0O0OO0OOO00=2):
    O0O00O00O000OOOO0 = O0O0000O000O0OO0O.encode('utf-16-be')
    OO0O000OO0OO0OOOO = []
    for OOO0O0OOOOOOOOO0O in range(0, len(O0O00O00O000OOOO0), O000OO0O0OO0OOO00):
        OO0O0O0OO0O0OO000 = O0O00O00O000OOOO0[OOO0O0OOOOOOOOO0O:OOO0O0OOOOOOOOO0O + O000OO0O0OO0OOO00]
        OO0O000OO0OO0OOOO.append(int.from_bytes(OO0O0O0OO0O0OO000, 'big'))

    return str(OO0O000OO0OO0OOOO)[1:-1]


def crazy_lol():
    if 'aaaaaaaaaaaaaaaaaaaa' is 'aaaaaaaaaaaaaaaaaaaa':
        if 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa':
            return 'yuli'
        else:
            return 'w3y'
    else:
        return 'opl'


wufcwruewfhdwb = crazy_lol()
uehrgeriufqodhqf = 'xWjoy'
ourhecnuqwhdi = 'L3Hu'
uwoehsdia9j02m20 = sauhd982w1d3jg23fwue('ă')
fh983hf29hd28fh93 = 'ABvS'
jd2w0d9j20dwj22djc3grh = 'fmVeZ'
password = wufcwruewfhdwb + uehrgeriufqodhqf + ourhecnuqwhdi + uwoehsdia9j02m20 + fh983hf29hd28fh93 + jd2w0d9j20dwj22djc3grh
password_input = input('Enter password to get the correct flag: ')
if password == password_input:
    print('CTF{' + hashlib.sha256(password.encode('utf-8')).hexdigest() + '}')
else:
    print('CTB{' + hashlib.sha256(password_input.encode('utf-8')).hexdigest() + '}')
```

After executing it we get:
```
yulixWjoyL3Hu259ABvSfmVeZ
```

The right string was starting with `w3y` not `yuli`.

```
CTF{b5858f16d9e3174a367ad5beecb171dcd8e2494d6edcc7a8caa7be2082a2a31f}
```
