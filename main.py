result = [[] for _ in range(4)]

for i in range(101):
    result[i % 4].append(i)

print(result)
