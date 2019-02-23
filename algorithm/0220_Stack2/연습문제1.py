str = '2+3*4/5'
s = []
for i in range(len(str)):
    if str[i] == "+" or str[i] == "-" or str[i] == '*' or str[i] == '/':
        s.append(str[i])
    else:
        print(str[i], end='')
while len(s) > 0:
    print(s.pop(), end='')