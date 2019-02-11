# C9 settings

1. python 설치

   ```bash
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   
   source ~/.bashrc
   pyenv install 3.6.7
   pyenv global 3.6.7
   python -V
   pip install --upgrade pip
   pip install flask
   pip install requests
   ```

2.

```bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```



3. django 깔기

```bash
git config --global user.name yoonwoo
git config --global user.email lkkjasd@naver.com
pyenv virtualenv django-venv # (가상환경 만듬)
pyenv local django-venv	# (장고 열어줌)
pip install django # (장고 설치)
```

4. 장고 폴더 만들기

```bash
django-admin startproject django_intro
cd django_intro
ls # ls 시 manage.py* 가 있어야함
# 서버를 열기 전에 settings.py에 들어가서 ALLOWED_HOST 를 '*' 로 바꾸고 저장해줘야한다.
python manage.py runserver 0.0.0.0:8080
```



# Django

## 1. 시작하기

1. 프로젝트 시작하기

```bash
$ django-admin startproject 프로젝트이름
```

아래와 같이 프로젝트 구조가 만들어진다.

```blank
├── db.sqlite3
├── django_intro
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

지금부터 pwd 는`~/workspace/django_intro` 이다.

2. 서버 실행하기

   * `settings.py`

   ```python
   ALLOWED_HOST = ['*']
   # c9에서는 host - 0.0.0.0, port - 8080만 활용할 수 있기 때문에 위와 같이 설정한다.
   ```


```bash 
python manage.py runserver 0.0.0.0:8080
```

앞으로 모든 장고 명령어는 프로젝트를 만들 때를 제외하고 `python manage.py`를 활용한다.

따라서, 반드시 `pwd` 와 `ls` 를 통해 현재 bash(터미널) 위치를 확인하자!!

3.  이그노어

   www.gitignore.io 에 들어가 django 검색 후 나오는 코드 전체 복사후

   `vi .gitignore` 에 들어가 복붙 후 esc , :wq! 로 나와준다.

   그 후 커밋한다. ( git add . , git commit -m '~~')



@app.route('home')

def index():

​	return 'hello'



## 2. Hello, django

>Django 프로젝트는 여러가지 app의 집합이다.
>
>각각의 app은 MTV 패턴으로 구성되어 있다.
>
>M (Model) : 어플리케이션의 핵심 로직의 동작을 수행한다. 
>
>T (Template) : 사용자에게 결과물을 보여준다.
>
>V (View) : 모델의 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
>**일반적으로 MVC 패턴으로 더 많이 사용된다.** (Mode, View, Controller)



### 1. 기본 로직

앞으로 우리는 1. 요청 url 설정(`urls.py`) 2. 처리 할 view 설정(`view.py`) 3. 결과 보여줄 template 설정

(`templates/`) 으로 작성할 것이다.

1. url 설정

```python
   # django_intro/urls.py
   from django.contrib import admin
   from django.urls import path
   # home 폴더 내에 있는 views.py를 불러온다.
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 요청이 home/으로 오면, views의 index 함수를 실행시킨다.
       path('home/', views.index),
   ]
```

    ```bash
python manage.py startapp 쓰고싶은이름 하면 migrations 가 만들어진다.
    ```



2.  view 설정

```python
# home/views.py
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello, django!')
```

* 주의할 점은 선언된 함수에서 `request` 를 인자로 받아야 한다.
  * request는 사용자(클라이언트)의 요청 정보와 서버에 대한 정보가 담겨 있다.
  * Django 내부에서 해당 함수를 호출하면서 정보를 넘겨주기 때문에 반드시 명시해줘야한다.



### 3. Template (MTV - T)

> Django에서 활용되는 Template은 DTL(Django Template Language) 이다.
>
> jinja2와 문법이 유사하다.

1. 요청 url 설정

 ```python
path('home/dinner/', views.dinner)
 ```

2. view 설정

```python
def dinner(request):
	box = ['치킨', '밥', '피자']
	dinner = random.choice(box)
	return render(request, 'dinner.html', {'dinner': dinner})
```

 * Template을 리턴하려면, `render`를 사용해야 한다.

    ![제목 없음](image/제목 없음-1549863604327.png)

    * `request` (필수)
    * `template` 파일 이름 (필수)
    * `template 변수 (선택) ` : `dictionary` 타입으로 구성해야 한다

3. Template 설정

```bash
$ mkdir home/templates
$ touch home/templates/dinner/
```

```html
<!-- home/templates/dinner.html--!>
<h1> {{dinner}} </h1>
```

### 4. Variable Routing

1. url 설정

```python
path('home/you/<name>', views.you),
path('home/cube/<int:num>', views.cube),
```

2. view 파일 설정

```python
def you(request, name):
    return render(request, 'you.html', {'name': name})
```

3. 템플릿 파일 설정

```django
<h1>{{ name }}, 안녕!!! </h1>
```

### 5. From data

1. `ping`

   1. 요청 url 설정

   ```python
   path('home/ping/', views.ping)
   ```



   2. view 설정

   ```python
   def ping(request):
       return render(request, 'ping.html')
   ```

   3. template 설정

   ```django
   <form action='/home/pong/'> <!-- action은 무조건 양쪽끝을 '/' 로 닫아줘야함 -->
       <input name="message" type = "text">
       <input type="submit">
   </form>
   ```


2. `pong`

   1. 요청 url 설정

   ```python
   path('home/pong/', views.pong)
   ```

   2. view 설정

   ```python
   def pong(request):
       message = request.GET.get('message')
       return render(request, 'pong.html', {'message': message})
   ```

   3. template 설정

   ```django
   <h1> {{ message }} </h1>
   ```


3. POST 요청 처리

   1. 요청 FORM 수정

      ```django
      <form action="/home/pong/" method="POST">
          {% csrf_token %}
      </form>
      ```

   2. view 수정

      ```python
      def pong(request):
          message = request.POST.get('message')
      ```

   * `csrf_token` 은 보안을 위해 django에서 기본적으로 설정되어 있는 것이다.
     * CSRF 공격 : Cross Sites Request Forgery
     * form을 통해 POST 요청을 보낸다는 것은 데이터베이스에 반영되는 경우가 대부분인데, 해당 요청을 우리가 만든 정해진 form에서 보내는지 검증하는 것.
     * 실제로 input type hidden으로 특정한 hash 값이 담겨 있는 것을 볼 수 있다.
     * `settings.py` 에 `MIDDLEWARE` 설정에 보면 csrf 관련된 내용이 설정된 것을 볼 수 있다.