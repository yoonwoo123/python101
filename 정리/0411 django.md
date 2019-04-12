# 0411 django

### Review

- startapp users 를 만든 후 settings.py 에 추가

- urls.py ( 바깥 ) 에 들어가서 'users/', include('users.urls') 추가

- 안쪽에 urls.py 생성 후 from django.urls import path, from . import views, urlpatterns를만듬

- def index(request) 생성

  ```python
  # views.py 
  from django.shortcuts import render
  from django.contrib.auth import get_user_model
      
  def index(request):
      User = get_user_model()
      users = User.objects.all()
      context = {'users':users}
      return render(request, 'users/index.html', context)
  
  def detail(request, user_pk):
      User = get_user_model()
      user = User.objects.get(pk=user_pk)
      context = {'user_detail': user}
      return render(request, 'users/detail.html', context)
  ```

  

  ```html
  # index.html
  {% extends 'boards/base.html' %}
  {% block body %}
  	<h1>
          회원명부
  </h1>
  	{% for user in users %}
  		<a href = "{% url 'users:detail' user.pk %}">{{ user }}</a>
  	{% endfor %}
  ```

  

    ```html
  # detail.html
  {% extends 'boards/base.html' %}
  {% block body %}
      <h1>프로필</h1>
      <p>{{ user_detail.pk }}</p>
      <p>{{ user_detail.username }}</p>
      <p>{{ user_detail.email }}</p>
      {% for board in user_detail.board_set.all %}
          <p> {{ board.title }} </p>
  	{% empty %}
          <p> 글을 작성해주세요..</p>
      {% endfor %}
  {% endblock %}
    ```

  

```python
# accounts/templatetags/gravatar.py

import hashlib
# 장고의 템플릿 내놔
from django import template

# 템플릿 라이브러리 가져와
register = template.Library()

# 필터로 makehash 함수를 추가해
@register.filter
def makehash(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
```

---

## Instagram

```bash
django-admin startproject instagram
cd instagram
vi .gitignore (gitignore의 django복붙해서 붙여넣기 후 esc , :wq!)
pyenv virtualenv 3.6.7 insta-venv
pyenv local insta-venv
pip list ( pip 의 정보를 확인 할 수 있다.)
pip install --upgrade pip
pip install django==2.1.8
pip freeze > requirements.txt
git add .
git commit -m 'gitignore|requirements.txt'
```



```python
# models.py
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return f'POST : {self.pk}'
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
python manage.py makemigrations
python manage.py migrate
git add.
git commit -m 'Post model'
```



```python
# admin.py
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
    
admin.site.register(Post, PostAdmin)

후 서버를 켜서 admin에 들어가 Posts 가 잘 나오는지 확인
```



```python
# settings.py

TEMPLATES 에 있는 DIRS 를
```



