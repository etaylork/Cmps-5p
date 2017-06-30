f = open('VectorTest.py', 'r')
L = f.readlines()
f.close()

print(L)
L.reverse()

g = open('Matrix.py.bak', 'w')
for line in L:
    g.write(line)
g.close()
