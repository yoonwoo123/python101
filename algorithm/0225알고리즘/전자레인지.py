T = int(input())
A = 300
B = 60
C = 10
flag = 0
if T // A > 0:
    a_but = T // A
    T = T % A
else:
    a_but = 0

if T // B > 0:
    b_but = T // B
    T = T % B
else:
    b_but = 0

if T % C != 0:
    flag = 1

if T // C > 0:
    c_but = T // C
else:
    c_but = 0

if flag == 0:
    print(f'{a_but} {b_but} {c_but}')
else:
    print(-1)