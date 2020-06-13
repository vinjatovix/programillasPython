x = 1
y = 1
z = 0
j = []
for i in range(30000):
    if '1337' in str(x):
        j.append(i)
        j.append(x)

    z = x + y
    x = y
    y = z

print(j)
