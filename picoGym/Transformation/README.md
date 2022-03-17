For this challenge the flag was compressed storing 2 consecutive characters in 2 bytes:

```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

We decoded it in `dec.py`.
