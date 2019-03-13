# 0218 Django CRUD 정리 + 0219

## MODEL 기초

1. boards app 설정

   ```bash
   $ python manage.py startapp boards
   ```

2. app 등록

   ```python
   # settings.py
   INSTALLED_APPS = [
       # ...
       'boards',
   ]
   ```

3. Model 생성

   ```python
   # boards/models.py
   class Board(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = model.DateTimeField(auto_now_add=True)
       
   #ex)
   class Student(models.Model):
       name = models.CharField(max_length=20) # max_length 는 무조건 넘겨줘야함
       email = models.CharField(max_length=30)
       birthday = models.DateField(max_length=30)
       age = models.IntegerField(max_length=30)
       
       def __str__(self):#admin에 보이는 내용이 object01 이런식으로 안나오고 Student로 뜸
           return f'{self.name}'
       
   # admin.py 작성양식
   from django.contrib import admin
   from .models import Job, Student # ***현재파일의 모델스의 클래스명을 불러온다.
   # Register your models here.
   class JobAdmin(admin.ModelAdmin):
       list_display = ['id', 'name', 'pastjob',]
   admin.site.register(Job, JobAdmin)
   
   class StudentAdmin(admin.ModelAdmin):
       list_display = ['id', 'name', 'email', 'birthday', 'age',] # *리스트 보기편하게
   admin.site.register(Student, StudentAdmin)
   ```

   * DB의 컬럼과, 어떠한 타입으로 정의할 것인지에 대해 `django.db.models` 를 활용해서 `Board` 클래스를 만든다.

4. Migration 파일 생성

   ```bash
   $ python manage.py makemigrations
   ```

   * DB에 반영하기 전에, 현재 등록된 APP의  `models.py` 를 바탕으로 DB 설계도를 작성한다.

   * `migrations` 폴더에 `0001_initial.py` 파일들이 생성된다.

   * `id` : primary key는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.

     ```python
     class Board(models.Model):
     	id = models.AutoField(primary_key=True)
     ```
     ```
     
     ```

5. DB에 반영

   ```bash
   $ ptyhon manage.py migrate
   ```

   * 실제 쿼리문을 확인하는 방법

     ```bash
     $ python manage.py sqlmigrate boards 0001
     ```

     * App이름(boards)와 migration버전(0001, 0002, ..)으로 명령어를 입력하면, 실제 데이터베이스에 적용되는 sql 쿼리를 확인할 수 있다.
     * `sqlmigrate` 명령어는 실제로 디비에는 반영되지 않는다. (단순 쿼리 확인)

## 장고 orm 활용하기

> 시작하기에 앞서서 django shell에서 모델과 관련된 메소드를 활용하여 데이터베이스 조작을 해보자!

1. `django shell` 활용하기

   ```bash
   $ python manage.py shell
   ```

   * 이 경우에는 내가 활용할 모듈 혹은 파일을 직접 import 해야한다. 번거로우니까

     `django_extensions` 을 깔아서 활용하자!

   ```bash
   $ python pip install django_extensions # 장고작성 편하게 해주는 플러그인
   ```

   * 해당 모듈을 활용하기 위해서는 `settings.py` 에 APP 등록을 해야한다.

     ```python
     # settings.py
     INSTALLED_APPS = [
         ...
         'django_extensions',
         'boards',
     ]
     ```

   * `shell_plus` 실행!

     ```bash
     $ python manage.py shell_plus
     ```

     * 실행하면, `INSTALLED_APPS` 에 설정된 내용들이 자동 import 된다.  

2. 메소드 정리

   1. CRUD - C

      ```python
      # models.py 에 클래스를 만들 때 작성하는 내용
      # 첫번째 방식
      board = Board()
      board.title = '1번제목'
      board.content = '1번내용'
      board.save()
      
      # 두번째 방식
      board = Board(title='1번제목', content='1번내용')
      board.save()
      
      # 세번째 방식
      board = Board.objects.create(title='1번제목', content='1번내용')
      ```

      * `save()`

        ```python
        board = Board(title='1번제목', content='1번내용')
        board.id #=> None
        board.created_at #=> None
        board.save()
        board.id #=> 1
        board.created_at #=> datetime.datetime(2019, 2, 18, 16, 20)
        ```

        * `save()` 메소드를 호출해야, DB에 저장된다. DB에 저장되면서 `id`와 `created_at`에 값이 부여된다.
        * `save()` 전에 `full_clean()` 메소드를 통해 현재 board 객체가 validation(검증)에 적합한지를 알아 볼 수 있다.

   2.  CRUD - R

      1. `all()`

         ```python
         Board.objects.all()
         #=> <QuerySet [<Board: 1: 안녕?>, <Board: 2: 2번글>, <Board: 3: 3번글>]>
         ```

      2. `get(pk=value)`

         ```python
         Board.objects.get(pk=1)
         # Board.objects.get(id=1)
         #=> <Board: 1: 안녕?>
         ```

         * `get()` 은 데이터베이스에 일치하는 값이 없으면, 오류가 발생한다.
         * 또한, 여러개의 값이 존재하면 , 오류가 발생한다.
         * 따라서 !!!! `id` 즉, Primary Key에만 사용하자 !
         * 리턴값은 board 오브젝트이다! (`filter()`, `all()`은 모두 queryset이 리턴된다.)

      3.  `filter(column=value)`

         ```python
         Board.objects.filter(title='안녕?')
         #=> <QuerySet [<Board: 1: 안녕?>]>
         Board.objects.filter(id=1)
         #=> <QuerySet [<Board: 1: 안녕?>]>
         
         # 더블언더스코어(__) 활용
         Board.objects.filter(title__contains='번글')
         #=> <QuerySet [<Board: 2: 2번글>, <Board: 3: 3번글>]>
         ```
      
         * 데이터베이스에서 찾았을 때, 결과가 하나이더라도 리턴값은 QuerySet이다.
      
           결과가 없어도 비어있는 QuerySet을 리턴한다!!

3. CRUD - D

   ```python
   board = Board.objects.get(pk=1)
   board.delete()
   #=> (1, {'boards.Board': 1})
   ```

4.  CRUD - U

   ```python
   board = Board.objects.get(pk=1)
   board.title = '수정수정'
   board.save()
   ```

   * save()` 메소드는 board 오브젝트에 id가 없을 때에는 값을 추가하고, 있으면 수정한다.

5.  추가 메소드

   ```python
   # 정렬
   Board.objects.order_by('title') # 오름차순
   Board.objects.order_by('-title') # 내림차순
   
   # 특정 단어 기준 탐색
   Board.objects.filter(title__contains='글') # 제목에 글이 들어간 모든 데이터
   Board.objects.filter(title__startswith='1') # 제목에 1로 시작하는 모든 데이터
   Board.objects.filter(title__endswith='글') # 제목에 글로 끝나는 모든 데이터
   Board.objects.filter(title__endswith='글')[0] #기본적으로 리스트이기 때문에 저렇게 값을 하나만 꺼낼수도 있음.
   ```


6. 장고에 id 만들기 > id를 admin으로 하여서 `admin/` 을 붙이면 Django 사이트로 이동된다.

   ```bash
    $ python manage.py createsuperuser
   ```





## 새로운 앱을 만들고 해야할 일

1. 만약 django-intro/장고CRUD 안에서 `python manage.py startapp jobs` 라고 선언해서 jobs를 만들어줬다면 메인 파일인 django_crud안에 있는 `settings.py`의 `INSTALLED_APPS` 에  `'jobs'` 를 추가했다고

   알려준다. 

2.  그리고 django_crud안에 있는 `urls.py` 에 include해준다.

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('boards/', include('boards.urls')),
       path('jobs/', include('jobs.urls')),
   ]
   ```

