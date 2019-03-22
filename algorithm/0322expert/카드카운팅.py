import sys
sys.stdin = open('카드카운팅_input.txt')

tc = int(input())
for T in range(1, tc+1):
    spade = []
    dia = []
    heart = []
    clover = []
    cards = list(input())
    S = [x for x in range(1, 14)]
    D = [x for x in range(1, 14)]
    H = [x for x in range(1, 14)]
    C = [x for x in range(1, 14)]
    for i in range(0, len(cards), 3):
        if cards[i] == 'S':
            num = int(cards[i+1] + cards[i+2])
            if num in spade:
                print('ERROR')
                break
            spade.append(num)
            S.pop(num-1)
        elif cards[i] == 'D':
            num = int(cards[i + 1] + cards[i + 2])
            if num in dia:
                print('ERROR')
                break
            dia.append(num)
            D.pop(num - 1)
        elif cards[i] == 'H':
            num = int(cards[i + 1] + cards[i + 2])
            if num in heart:
                print('ERROR')
                break
            heart.append(num)
            H.pop(num - 1)
        elif cards[i] == 'C':
            num = int(cards[i + 1] + cards[i + 2])
            if num in clover:
                print('ERROR')
                break
            clover.append(num)
            C.pop(num - 1)
    print(cards)
    print(len(D))