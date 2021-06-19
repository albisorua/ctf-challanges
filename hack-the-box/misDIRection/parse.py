
f = open("workspace.txt")
data = f.read()
data = data.split('\n')

n = len(data)

data = sorted(data, key=lambda k : int(k[2:]))
data = [el[:1] for el in data]
print(''.join(data))