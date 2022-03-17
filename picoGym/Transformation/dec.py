enc = open('enc', 'r').read().rstrip()

flag = []

for ch in enc:
    flag.append(chr(ord(ch) >> 8))
    flag.append(chr(ord(ch) & 0xff))

print(''.join(flag))
