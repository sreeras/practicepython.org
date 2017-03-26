a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

reduced = []
for i in a:
    if i < 5:
        reduced.append(i)
print(reduced)

print([i for i in a if (i < 5)])
