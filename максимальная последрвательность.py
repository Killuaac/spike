fst = -1
cr_len = 0
max_len = 0
part = int(input())

while part != 0:
    if fst == part:
         cr_len = cr_len + 1
    else:
        fst == part
        max_len = max(max_len, cr_len)
        cr_len = 1
    part = int(input())
max_len = (max_len, cr_len)
print(max_len)


