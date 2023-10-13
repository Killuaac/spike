fst = int(input())
sec = int(input())

if fst < sec:
    fst, sec = sec, fst
part = int(input())
while part != 0:
    if part > fst:
        sec, fst = fst, sec
    elif part > sec:
        sec = part
    part = int(input())
print(sec)
