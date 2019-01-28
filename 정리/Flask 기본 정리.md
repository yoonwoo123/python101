# Flask 19/01/28



cloud9 에서 new project 클릭 후 팀을 설정하지 않고 blank로 만든다.

만든 후에 zzu.li/c9 에 들어가서 1~10번째줄까지 복사 (--upgrade pip까지) 후 bash에 붙여넣으면

저절로 python이 설치된다.

그 후 upgrade pip 이 뜨면 엔터 한번 더



설치 후 댓글에 적혀있는 3줄을 복사 후 붙여 넣기 한다.

그 후 엔터 한번 더

그 후 pyenv virtualenv 3.6.7 flask-venv 엔터

pyenv local flask-venv 를 해준 후 엔터 시 (flask-venv) nickname:~/workspace 로 바뀌었다면 성공!



그 후 pip install flask를 입력해주고 엔터



pip install --upgrade pip 엔터

pip freeze > req.txt 엔터 그러면 req.txt 파일이 생긴다.



flask run -h $IP -p $PORT 으로 서버를 키고 ctrl + c 로 나올 수 있다.

```python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/hi')    
def hi():
    return '안녕, 지원'

# 5월 20일부터 d-day를 출력하는 것을 만들어주세요.
@app.route('/dday')
def dday():
    now = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    d = vacation - now
    # return은 반드시 string으로 되어야 한다!
    return f'{d.days}일 뒤에 놀러가자'

@app.route('/hi/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)
    
# 세제곱의 결과를 출력해볼게요!
@app.route('/math/<int:num>')
def math(num):
    a = num**3
    return f'{a}이 나옵니다'
    #혹은 return str(a) 로 출력 무조건 string으로 출력해야되기 때문이다.



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
```



