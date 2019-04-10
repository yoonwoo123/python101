# 0410 django

Java 에는 파이썬의 딕셔너리와 같은 Hash 라는 것을 쓰는데

단방향으로 전달하는 기능으로 즉 암호화의 기능을 갖고 있다. ( 역산이 힘드므로)

MD5 라는것은 역산이 가능해져서 도태되었고 요즘은 __SHA256__  을 쓴다. 

단방향 해시 함수를 보완하기 위해 salting(소금치기) 이 있다.



## 솔팅(salting)

솔트(salt)는 단방향 해시 함수에서 다이제스트를 생성할 때 추가되는 바이트 단위의 임의의 문자열이다. 그리고 이 원본 메시지에 문자열을 추가하여 다이제스를 생성하는 것을 솔팅(salting)이라 한다. 예를 들어 다음과 같이 "redfl0wer"에 솔트인 "8zff4fgflgfd93fgdl4fgdgf4mlf45p1"를 추가해 다이제스트를 생성할 수 있다.



___

### 라인 면접 질문

* __HTTP Method랑 REST API의 어떤 행위와 매칭이 되는가?__

  C - POST

  R - GET

  U - PUT

  D - DELETE



* __Naver.com 에 들어가는 일련의 과정을 설명해 주세요.__

​	DNS 서버(?) 니까 실제 IP주소를 찾아갈 것이고, 웹 서버에서 받아서 처리를 할텐데

​	네이버닷컴이니까 로그인같은 인증이 아닌 단지 메인 페이지를 보여주는 것이라면

​	먼저 DOM 트리를 만들고 CSS 마크업을 처리하여 메인페이지를 띄워줄 것이다.

---



## ** require_POST - 시험에 출제

404 = Not found   get_object_404

405 = Method not allowed



### require_safe

---



유저 목록(유저 index)



프로필 페이지(유저 detail)

​	- gravatar 이미지

​	- 이메일

​	- username 

​	- 그 사람이 쓴 글

-댓글까지