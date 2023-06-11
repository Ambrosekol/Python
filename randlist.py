import random
newList = []
[newList.insert(i, random.randrange(1, 10)) for i in range(5)]
print(newList)

end = len(newList) - 1

while end > 1:
    beg = 0
    while beg < end:
        if newList[end] > newList[beg]:
            temp = newList[end]
            newList[end] = newList[beg]
            newList[beg] = temp
        beg += 1
    end -= 1

print(newList)
newList.reverse()
print(newList)