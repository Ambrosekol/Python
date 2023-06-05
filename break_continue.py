i = 1
while i < 30:
    if (i % 2) == 0:
        i += 1;
        continue
    if (i == 15):
        break
    print("Odd number {} ".format(i))
    i += 1;