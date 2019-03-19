# 0319 django 처음부터 복습

```bash
django-admin startproject django_fbv
cd django_fbv

# 먼저 git ignore ( django )
vi .gitignore
# 그 후 i 누르고 ctrl+v 후 esc , :wq!

git init
git add .
git commit -m '00|django startproject|'
```

```bash
 python manage.py startapp boards
 git add .
 git commit -m '01|startapp boards'
 
 # git commit 메시지 잘못입력시
 git commit --amend
 # 그 후 메시지명 고치고 ctrl+x , Y 후 엔터
```

```python
# settings.py 수정
ALLOWED_HOSTS = ['*']
INSTALLED_APPS
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
git add .
git commit -m '02|settings.py|'
```

```python
# models.py 만들기
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    hit = models.IntegerField(default=0) # 조회수 default=0을 이유는 첫저장시 not null때문
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): # 얘는 보여주기 위한 것이라 수정해도 migration 안해줘도 됨
        return f'<Board ({self.id})> : {self.title}'  
```

```python
from .models import Board # 클래스 가져오기
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'hit', 'created_at', 'updated_at']
    
admin.site.register(Board) #(클래스명)

git add .
git commit -m '03|Board model 생성|'
```

```bash
# migration
python manage.py makemigrations
python manage.py migrate

git add .
git commit -m '04|migration|'

# migration 해준 후 python.manage.py createsuperuser 로 admin 들어가서 잘만들어지는지 확인해보면 좋다.
```

```python
# urls.py -> settings.py 와 같이 있는 바깥 urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
]

# urls.py를 views.py 와 같은경로에 생성 후

from django.urls import path
from . import views # . import 주의 .models 와 달리 from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name="index")
]
```

```python
# views.py 작성

from django.shortcuts import render
from .models import Board # 클래스가 index에서 사용되므로 .models 에서 클래스를 불러온다.

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context) # templates 안에 boards안
```

```html
base.html 작성

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %} FBV</title>  # title 작성시
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

```html
index.html 작성

{% extends 'boards/base.html' %}
{% block body %}
<h1>게시글 목록</h1>
{% for board in boards %}
    <p>{{ board.pk }}</p>
    <p>{{ board.title }}</p>
    <hr>
{% endfor %}

{% endblock %}

git add .
git commit -m '05|CRUD-index|'
```

```python
# urls.py create path
path('new/', views.create, name="create")

# views.py 안에 new 작성

def create(request):
    if request.method == "POST":
        board = Board()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:index')
    return render(request, 'boards/create.html')

# index.html
<a href= "{% url 'boards:create' %}">글 쓰러가기</a>

# create.html

{% extends 'boards/base.html' %}
{% block body %}
<form method="POST">
    {% csrf_token %}
    <input type="text" name="title">
    <textarea name="content"></textarea>
    <input type="submit">
</form>

{% endblock %}


# 검증작업을 위해 forms.py 생성
from django import forms

class BoardForm(forms.Form):
    title = forms.CharField() # models 와 달리 max_length 안해줘도됨
    content = forms.CharField()
    
# 그 후
from .forms import BoardForm
# 앞으로는 이렇게 작성할 것!
def create(request):
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = Board()
            board.title = board_form.cleaned_data.get('title')
            board.content = board_form.cleaned_data.get('content')
            board.save()
            # board.title = request.POST.get('title')
            # board.content = request.POST.get('content')
            return redirect('boards:index')
    else:
        board_form = BoardForm()
    context = {'board_form': board_form}
    return render(request, 'boards/create.html', context)

# forms.py 에 작성된 title, content 는 사이트에서 자동으로 
Title :
Content : 로 나온다.
# 이것은 labal로 저절로 감싸지는 forms 의 기능이며
# label='제목' 으로 하면 label 명이 바뀌어서 나온다.

# forms.py
class BoardForm(forms.Form):
    title = forms.CharField(label='제목', max_length=10, 
                            error_messages={'required': '제목을 반드시 입력해주세요.'})
    						content = forms.CharField(label='내용', 
                            error_messages={'required': '내용을 반드시 입력해주세요.'},
                            widget=forms.Textarea(attrs={'placeholder': '내용을 입력해줘!',
                            'class': 'input-box'
                                            }))
        
git add .
git commit -m '06|CRUD-C|'
```

```html
index.html
<a href="{% url 'boards:detail' board.pk %}">글 보러가기</a>

url 설정
path('<int:board_pk>/', views.detail, name="detail"),

views.py 설정
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
    
detail.html 작성

{% extends 'boards/base.html' %}

{% block body %}
<h1>{{ board.pk }}번째 글</h1>
<h2>{{ board.title }}</h2>
<p>조회수 : {{ board.hit }}</p>
<hr>
<p>{{ board.content }}</p>
{% endblock %}
```

```python
# views.py에 get_object_or_404 로 없는 id값의 주소로 갈 때 404 페이지 뜨게 해줌
from django.shortcuts import render, redirect, get_object_or_404

def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk) # 앞으로 이렇게 작성
    board.hit += 1 # 조회수 증가해주는 것
    board.save()
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
```

```python
# 추가적으로 models.py 에 작성
from django.urls import reverse # 중요!

    def get_absolute_url(self):
        return reverse('boards:detail', args=[self.pk])
   
그 후 views.py 에 create 부분
return redirect(board) 으로 바꿔도 이용가능

git add .
git commit -m '07|CRUD-R|'
```

```html
detail.html 작성

삭제 버튼을 POST로 보내자
<form action="{% url 'boards:delete' board.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
</form>
```

```python
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else:
        return redirect(board)

git add .
git commit -m '08|CRUD-D|'
```

```python
# edit.html 작성 시 edit.html과 create.html 이 똑같에 생겨서 둘을 합쳐
# form.html 이라는 하나의 html로 통합할 수 있다!

# views.py

def edit(request, board_pk):
    # 1. board_pk에 해당하는 오브젝트르 가져온다.
    #    만약에 없으면 404 에러
    #    만약에 있으면 board = Board.objects.get(pk=board_pk)와 동일.
    board = get_object_or_404(Board, pk=board_pk)
    # 2-1. POST 요청이면 (사용자가 form을 통해 데이터를 보내준 것.)
    if request.method == "POST":
        # 사용자 입력값(request.POST)을 BoardForm에 전달해주고, 
        board_form = BoardForm(request.POST)
        # 검증 (유효성 체크)
        if board_form.is_valid():
            board.title = board_form.cleaned_data.get('title')
            board.content = board_form.cleaned_data.get('content')
            board.save()
            return redirect(board)
    # 2-2: GET 요청이면 (수정하기 버튼을 눌렀을 때)
    else:
        # BoardForm을 초기화(사용자 입력값을 넣어준 상태)
        # board_form = BoardForm(initial=board.__dict__) 이렇게 작성해도 가능
        board_form = BoardForm(initial={'title': board.title, 'content': board.content})
    # context에 담겨 있는 board_form은 아래와 같이 가능함.
    # 1 - POST 요청에서 검증에 실패하였을 때, 오류 메시지가 포함된 상태
    # 2 - GET 요청에서 초기화된 상태
    context = {'board_form': board_form}
    return render(request, 'boards/form.html', context)

git add .
git commit -m '09|CRUD-U|'
```

```python
# forms.py 새로운 것

from .models import Board

class BoardForm(forms.ModelForm):                                      
    class Meta:
        model = Board
        # fields = '__all__' # 모든 값을 받아올 때
		fields = ['title', 'content'] # 받아오고 싶은 값만 받아 올 때
#이걸 써주면
#create 를 이렇게 바꿀 수 있다.
if board_form.is_valid():
            # board = Board()
            # board.title = board_form.cleaned_data.get('title')
            # board.content = board_form.cleaned_data.get('content')
            # board.save() # 이 4줄을 밑 1줄로 대체가능!
            board = board_form.save()
            return redirect(board)
# edit 는

board_form = BoardForm(request.POST, instance=board)
        if board_form.is_valid():
            board = board_form.save()
            return redirect(board)
    else:
        board_form = BoardForm(instance=board)

# 또 forms.py 보드밑에 추가 작성할수있다.
class BoardForm(forms.ModelForm):                                      
    class Meta:
        model = Board
        fields = ['title', 'content']
        widgets = {'title': forms.TextInput(attrs={
            'placeholder':'제목을 입력해주세요.', 'class': 'title'}),
                   'content': forms.Textarea(attrs={
            'placeholder':'내용을 입력해주세요.', 'class': 'content'})
        }
        error_messages = {'title': {
            'required': '제목을 반드시 입력해주세요.'
        }, 'content': {
            'required': '내용을 반드시 입력해주세요.'
        }
    }
git add .
git commit -m '10|ModelForm 적용|'
```

```html
form.html 로 통합하고 생성과 수정을 구분하기 위해서 작성하는 문법

{% if request.resolver_match.url_name == 'create' %}
    <h1>글 생성</h1>
{% else %}
    <h1>글 수정</h1>
{% endif %}

git add .
git commit -m '11|form.html 분기|'
```

```bash
pip freeze > requirements.txt	# freeze 해서 txt파일에 현재 사용버전이 저장됨

pip install django-crispy-forms 로 설치
그 후 settings.py 에 # app등록 꼭 해주기

# 적용 form.html
{% extends 'boards/base.html' %}

{% block body %}
{% load crispy_forms_tags %}
{% if request.resolver_match.url_name == 'create' %}
    <h1>글 생성</h1>
{% else %}
    <h1>글 수정</h1>
{% endif %}

<form method="POST">
    {% csrf_token %}
    {{ board_form|crispy }}
    <!--<input type="text" name="title">-->
    <!--<textarea name="content"></textarea>-->
    <input type="submit">
</form>

{% endblock %}

git add .
git commit -m '12|django-crispy-forms|'
```

```html
form.html 에서 추가적으로

{{ board_form|crispy }} 로 1줄로 되면 div를 씌우든 활용을 할 때 힘들기 때문에
반복문을 쓰기 위해서 밑에처럼 for문을 돌려서 활용할 수 있다.
<div class="row">
{% for field in board_form %}
	<div class="col-6">
    	{{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
</div>

git add .
git commit -m 'form 추가 활용법'
```

