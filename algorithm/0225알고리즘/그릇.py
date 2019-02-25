dishes = input()
# dishes = '()()()(((())()'
s = []
cnt = 0
for dish in dishes:
    if dish == '(':
        if len(s) > 0 and s[-1] == '(':
            cnt += 5
            s.append(dish)
        else:
            cnt += 10
            s.append(dish)
    if dish == ')':
        if len(s) > 0 and s[-1] == ')':
            cnt += 5
            s.append(dish)
        else:
            cnt += 10
            s.append(dish)
print(cnt)

# ( 가 들어갈때 (가 전에 이미있으면 +=5  그렇지않으면 += 10
# )는 무조건 += 10