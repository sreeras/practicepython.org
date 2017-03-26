from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Solution 1
def overlap(a, b):
    overlapList= []
    for i in a:
        if (i in b) and not (i in overlapList):
            overlapList.append(i)
    return overlapList

print (overlap(a,b))

#Solution 2

print (set([i for i in a if i in b]))

#Solution 3

x = [randint(0,20) for i in range(randint(0,20))]
y = [randint(0,20) for i in range(randint(0,20))]

print (x, y)
print (overlap(x,y))
