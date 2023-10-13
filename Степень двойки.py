n = int(input())
i = 2
step = 1
while i <= n:
    i *= 2

    step += 1

print(i // 2, step - 1)
