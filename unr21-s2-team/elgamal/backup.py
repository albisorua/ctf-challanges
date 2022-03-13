from pwn import *
from gmpy2 import *

def elgamal_gen_x_and_h(q, g):
    x = random.randrange(1, q-1)
    if x%2 == 0:
        x = x+1

    h = pow(g, x, q)
    return (h, x)

def elgamal_encrypt(q, g, h, m):
    y = random.randrange(1, p)
    c1 = pow(g, y, q)
    s = pow(h, y, q)
    c2 = s * m % q
    return (c1, c2)

def elgamal_decrypt(q, g, x, c):
    (c1, c2) = c
    s = pow(c1, q-x, q)
    m = c2 * s % q
    return m

io = remote("34.159.190.67", 30289)

msg = io.recvuntil(b'? ')

msg = msg.split(b"\n")[-1]

print(msg)

msg = msg.split(b' ')

q = int(msg[1][2:].decode('utf-8'))

g = int(msg[3][2:7].decode('utf-8'))

print(q, g)

(h, x) = elgamal_gen_x_and_h(q, g)

print(h, x)

io.sendline(str(x))

msg = io.recvuntil(b"h: ")

print(msg)

io.sendline(str(h))

msg = io.recvuntil(b": ")

print(msg)

m = int("0x6869", 16)

print(m)

io.sendline(str(m))

msg = io.recvuntil(b"? ")

y = random.randrange(1, q)

print(y)

io.sendline(str(y))

msg = io.recvuntil(b"s: ")

print(msg)

s = pow(h, y, q)

print(s)

io.sendline(str(s))

msg = io.recvuntil(b"c1: ")

print(msg)

c1 = pow(g, y, q)

print(c1)

io.sendline(str(c1))

msg = io.recvuntil(b"c2: ")

print(msg)

c2 = s * m % q

print(c2)

io.sendline(str(c2))


# Just a message
msg = io.recvline()

print(msg)

# New public key
msg = io.recvline()

msg = msg.split(b"=")[1].lstrip(b" (").rstrip(b")\n").split(b", ")

public = [int(el.decode("utf-8")) for el in msg]

q = public[0]
g = public[1]
h = public[2]
print(q, g, h)

#print(msg)

# Ciphertext
msg = io.recvline()

msg = msg.split(b"=")[1].lstrip(b" (").rstrip(b")\n").split(b", ")

cipher = [int(el.decode("utf-8")) for el in msg]

c1 = cipher[0]
c2 = cipher[1]

print(c1, c2)

#print(msg)

# Private key
msg = io.recvline()

msg = msg.split(b": ")[1].rstrip(b"\n")

x = int(msg.decode("utf-8"))

print(x)

#print(msg)

s = pow(c1, x, q)
print(s)
msg = io.recvuntil(b": ")

io.sendline(str(s))

msg = io.recvuntil(b"s_inv: ")

print(msg)

s_inv = pow(s, -1, q)

print(s_inv)

io.sendline(str(s_inv))

msg = io.recvuntil(b": ")

m = bytes.fromhex(hex(c2 * s_inv % q)[2:]).decode('ASCII')

print(m)

print(msg)

io.sendline(m)

msg = io.recvline()

print(msg)

io.close()
