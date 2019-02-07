# 0207 DB(ORM= Object Related Mapping)

>touch app.py 로 app.py 생성
>
>from flask import Flask
>
>from flask_sqlalchemy import SQLAlchemy
>from flask_migrate import Migrate
>
>위 두 줄을 실행하기 위해서 bash 에 install 해준다.
>

>```bash
>pip install flask_sqlalchemy flask_migrate
>```

>```bash
>flask db init
>
>flask db migrate # class 내용을 db에 반영하기 위해 준비
>
>flask db upgrade # migration 파일을 실제 db에 반영
>```
>
>그 후 `sqlite3 db_flask.sqlite3`  를 해 주면 table에 user가 생긴다.
>
>다른 터미널을 열어서 python을 치고 from app import * 을 해준다.
>
>그 후  User를 쳐주면 클래스로 app.User가 뜰 것이다.
>
>클래스에 값을 추가하려면
>
>```python
>user = User(username='재찬', email = 'lee@lee')
>db.session.add(user) # insert 명령어와 같다. user table 에 값을 추가해준다
>db.session.commit() # commit 즉 반영
>```
>
>그 후 sqlite3 터미널에서 `SELECT * FROM user;` 시 만든 값이 들어가있다.
>
>값을 더 직관적으로 보기 위해서 `.headers on` , `.mode column` 을 해주자.
>
>
>
>__python 터미널__
>
>에서`users = User.query.all()` 을 해주면 db에 저장 돼 있는 값을 users에 리스트로 저장 
>
>그 후 users[0], users[1] 이런식으로 값을 불러 올 수 있다.
>
>
>
>__bash__
>
>` User.query.filter_by(username='영우').all()` 를 해주면 username이 영우인것만 가져와준다.
>
>`User.query.get(1)` , `User.query.get(2)` 를 해주어 값을 가져올 수도 있다.
>
>`db.session.delete(user)`, `db.session.commit()` 을 해주면 user (신욱) 의 값을 없앨 수도 있다.
>
>`u1 = User.query.get(2)` 으로 값을 넣고 `u1.username = 'young'` `db.session.commit()` 을 해주면
>
>yoonwoo가 young으로 업데이트 돼 있다.



# ORM(flask-sqlalchemy) by 타키쌤 정리

1. 기본 설정

```bash
pip install flask_sqlalchemy flask_migrate
```

```python
# touch app.py로 python 파일 생성 후
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model): # 괄호안의 db모델은 db 설정을 상속받는것
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30))
    created_at = db.Column(db.String(80), nullable=False)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now().strftime("%D")

    def __repr__(self):
        return f'{self.id}: {self.username}'
```

2. flask db 설정

   * 초기 설정(`migration` 폴더 생성)

   ```
   $ flask db init
   ```

   * migration 파일 생성

   ```
   $ flask db migrate
   ```

   * db 반영

   ```
   $ flask db upgrade
   ```


3. 활용법

   1. Create

   ```python
   # user 인스턴스 생성
   user = User(username='윤영우', email='yoonwoo@gmail.com')
   # db.session.add 명령어를 통해 추가
   	# INSERT INTO user (username, email); 위와 같은말
   	# VALUES ('윤영우', 'yoonwoo@gmail.com');
   db.session.add(user)
   # db에 반영
   db.session.commit()
   ```

   2. Read

   ```python
   # SELECT * FROM user;
   users = User.query.all()
   # get 메소드는 primary key로 지정된 값을 통해 가져온다.
   user = User.query.get(1)
   # 특정 컬럼의 값을 가진 것을 가져오려면 다음과 같이 쓴다.
   user = User.query.filter_by(username='윤영우').all() # 전부
   user = User.query.filter_by(username='윤영우').first() # 하나만 (LIMIT 1과 비슷)
   ```

   3. Update

   ```python
   user = User.query.get(1)
   user.username = '윤영우'
   db.session.commit()
   ```

   4. Delete

   ```python
   user = User.query.get(1)
   db.session.delete(user)
   db.session.commit()
   ```



`from flask import Flask, render_template, request, redirect, flash`

으로 render-template과 request, redirect, flash 등을 사용하게 했다.

그리고 `@app.route('/')` 로 서버의 메인 페이지를 만든다.

서버를 여는 코드는 예전 app.py에서 따와서 똑같다.

```python
# 서버
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
```



```python
# 서버의 메인 페이지
@app.route('/')
def index():
    users = User.query.all()
    # type(users) : list 타입
    # list element : user 인스턴스
    return render_template('index.html', users=users)
    
@app.route('/users/new')
def new_user():
    return render_template('new.html')
    
@app.route('/users/create', methods=["POST"])
def create_user():
    username = request.form.get('username') # 이재찬
    email = request.form.get('email') # lee@lee
    # user = User(username='이재찬', email='lee@lee')
    user = User(username=username, email=email) # 왼쪽이 클래스 오른쪽이 '이재찬'
    db.session.add(user)
    db.session.commit()
    
    # return render_template('create.html', username = user.username, email = user.email)
    return redirect('/')
```











## Template Inheritance(템플릿 상속)

### Base Template

```html
<!doctype html>
<html>
  <head>
    {% block head %}
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
  </head>
  <body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
      {% block footer %}
      &copy; Copyright 2010 by <a href="http://domain.invalid/">you</a>.
      {% endblock %}
    </div>
  </body>
</html>
```

### Child Template

```html
{% extends "layout.html" %}
{% block title %}Index{% endblock %}
{% block head %}
  {{ super() }}
  <style type="text/css">
    .important { color: #336699; }
  </style>
{% endblock %}
{% block content %}
  <h1>Index</h1>
  <p class="important">
    Welcome on my awesome homepage.
{% endblock %}
```











### 암호화(부가적)

```
pip install werkweug
```

```python
from werkzeug.security import generate_password_hash, check_password_hash

a = 'hihi'
# 암호화
hash = generate_password_hash(a)
print(hash)
# 차이점 확인
check_password_hash(hash, 'hihi')
check_password_hash('hihi', hash)
```























