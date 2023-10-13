mass = [1, 2, 4, 6, 23, 32, 532, 11]
maximum = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[maximum]:
        index_of_max = i
print(a[maximum], maximum)
