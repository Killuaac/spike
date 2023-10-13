mass = [1, 2, 4, 6, 23, 32, 532, 11]
for i in range(1, len(mass)):
    if mass[i] > mass[i - 1]:
        print(mass[i])
