def greeting(name='아이유'):
    print(f'안녕, {name}')


pi = 3.141592

if __name__ == '__main__':
    print('main : 직접 실행되었습니다.')
    print(__name__)
else:
    print('모듈로 불러져서 실행되었습니다.')
    print(__name__)
