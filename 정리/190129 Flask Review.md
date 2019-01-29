# 190129 Flask Review

variable 변수에서

html에 name = "name" name = "msg" 로 왼쪽의 값은 고정된 값으로 변하지 않고 

오른쪽이 찾고자 하는 변수 이름이다.



get은 오류를 내지않고 None 을 반환하기 때문에 서버종료를 방지할 수 있다.

또 None값이 나온다면 키 접근을 잘못했거나 딕셔너리를 잘못 만들거나 오타인지 확인해야한다.

```python
#app.py

# request.args = {'name' : '재찬', 'msg': '안녕'}
name = request.args.get('name')
msg = request.args.get('msg') 
```

```html
<!--ping.html-->

<form action="/pong">
    <input type="text" name = "name">
    <input type="text" name = "msg">
    <!--{'name' : '재찬', 'msg': '안녕'}-->
    <input type="submit">
</form>
```



# 190129 Flask 수업 내용

for i in range(timeline|length) :  이런식으로 range len 를 돌린다.

---



return redirect('/timeline') 을 넣으면 넣은 구문을 실행한 후 /timeline으로 돌아온다. 

위에 from flask import redirect를 써줘야한다.



# DB

간단하게 말해 데이터의 집합체

우리가 쓰는 것은 local 형식의 SQL

수업이 끝날 때쯤 mySQL 을 설치할 예정이다.



### 스키마

미리 데이터에 어떠한 값(int, text 등)과 길이가 들어갈 지 구조와 제약조건을 걸어 놓은 것



### 테이블

하나의 데이터 베이스 안에 여러개의 테이블이 있다.

각 열(column)에는 고유한 데이터 형식이 지정되고 행(row)는 레코드라고 불린다.

__PK(기본키) : 각 행의 고유값으로 Primary Key로 불린다. 반드시 설정하여야하며, 데이터베이스 관리 및 관계설정시 중요하게 활용된다.__



## SQL

__SQL__는 관계형 데이터베이스 관리시스템의 데이터를 관리하기 위해 설계된 __특수 목적의 프로그래밍 언어__이다.



__SQL__ 문법은 크게 3가지로 나뉜다.

* DDL - 데이터 정의 언어: CREATE, DROP , ALTER
* DML - 데이터 조작 언어: INSERT, UPDATE, DELETE, SELECT
* DCL  - 데이터 제어 언어: GRANT, REVOKE, COMMIT, ROLLBACK



## 01 Hello World DB

키워드(SELECT문)     키워드

SELECT * FROM _table_

여기서 *은 '모든'을 의미함 즉 table의 모든 데이터를 가져와라

---

CREATE TABLE classmates (        ...> 는 엔터
   ...>id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name VARCHAR(30) NOT NULL
   ...> );

---

.tables 입력시

현재 있는 테이블인 classmates 가 출력된다.

---

.schema classmates 하면 위에 입력한 값이 나온다.

CREATE TABLE classmates (        ...> 는 엔터
   ...>id INT PRIMARY KEY,
   ...> name VARCHAR(30)
   ...> );

---

DROP TABLE classmates 를 하면 테이블을 없앨 수 있다.

---

크게 4가지로 생각 할 수 있다.

C  reate

R  ead

U  pdate

D  elete

---

### data 추가하기

```python
INSERT INTO classmates(name, age, address) -- (id, name, age, address) 
-- 모든 값을 넣을 때는 column을 명시할 필요 없이 순서만 지키면 된다.
VALUES('홍길동', 30, '서울');
```

```python
-- 컬럼명 표기
.headers on
-- 표처럼 표기
.mode column
```



---






### data 가져오기 (table에서)

SELECT * FROM  _table_  (뒤에 LIMIT 숫자 를 쓰면 그 숫자개수만큼만 가져온다.)

SELECT * FROM  _table_ (뒤에 LIMIT 숫자 OFFSET 숫자 하면 OFFSET에 적혀있는 순서의 데이터를 LIMIT개만)

---

### data 삭제하기

DELETE FROM _table_ WHERE id =3;

이런식으로 특정한 유니크값인 id를 지정해서 삭제할 수 있다.

---

### data 업데이트하기

UPDATE  _table_ SET column1 = value1, column2 = value2, ... WHERE condition(id = 2); 

---

### 갯수,평균,최대,최소 구하기

SELCET count(age) FROM _table_ ;

SELCET AVG(age) FROM _table_ ;

SELCET MAX(age) FROM _table_ ;

SELCET MIN(age) FROM _table_ ;

---

### 원하는 값 찾기

WHERE column LIKE

2% : 2로 시작하는 값

%2 : 2로 끝나는 값

%2% : 2가 중간에 들어가는 ㄱ밧

_2% : 아무값이나 들어가고 두번째가 2로 시작하는 값

1____: 1로 시작하고 4자리인 값

`2_%_%` 는 2로 시작하면서 적어도 3자리인 값

`2__%`랑도 같다. 

---

### 정렬

SELECT * FROM  _table_ ORDER BY 값 ASC/ DESC (오름, 내림)

 

---

15workshop 할 때 sqlite3 15workshop.sqlite3 로 만들고 제출















