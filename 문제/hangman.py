def isanswer(answer, letters):
    return not (set(answer) - set(letters))

def status(answer, letters):
    for i in answer:
        if i not in letters:
            answer = answer.replace(i, ' _')
    return answer

def hangman(answer):
    attempt = 8
    letters = []
    print('행맨 게임을 시작해봅시다!')
    print(f'남은 시도 {attempt}')
    while True:
        char = input('알파벳 1개를 입력하세요.: ')
        if isanswer(answer, char):
            print('짝짝짝 맞췄습니다.')
            break
        if char in answer: 
            print(f'맞췄습니다! {answer.count(char)}개가 있네요.')
            letters.append(char)
            print(status(answer, letters))
            print(f'남은 시도 {attempt}')
        elif char not in answer and char.isalpha()==True and len(char)==1:
            print(f'땡!')
            print(status(answer, letters))
            attempt -= 1
            print(f'남은 시도 {attempt}')

        if len(char) > 1 or char.isalpha() == False:
            print('알파벳으로 1개만 입력하라고!')
        
        
        if isanswer(answer, letters):
            print('짝짝짝 맞췄습니다.')
            break
        if attempt == 0:
            break

if __name__ == '__main__':
    hangman('software')