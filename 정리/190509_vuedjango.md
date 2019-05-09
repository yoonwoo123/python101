190509

# vuedjango

vue.js 랑 django랑 분리된 형태를 보여준다.

오브젝트 - local storage - firebase -> django api?



- vue-router vue resource - evan you (이거 쓰지말래) / axios쓰래



## 시작

- `django/music_api`
  - musics 목록 받아오기

```js
<script>
    const djangoUrl = "http://django-intro-injeong.c9users.io:8080/api/v1/musics"
axios.get(djangoUrl)
    .then(response => {
    console.log(response)
})

</script>
```

=> CORS error (HTTP 접근 제어) `error`

스크립트 태그 내에서 다른 origin 으로 요청을 보내는건 금지되어 있다.

ajax가 들어오면서 태그에서 요청오는게 생겼는데 이때 이걸 막는거!

- [오류 해결](<https://github.com/ottoyiu/django-cors-headers>)

`django에서 CORS 정책을 관리하면 된다.(원하는 곳만 요청 받아주면 된다.)`

`django`

```bash
$ pip install django-cors-headers
```

`settings.py`

```python
# 내가 만든 앱 위에!
INSTALLED_APPS = [
    'corsheaders',
]

# 문서가 하라는 위치에!
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 추가
    'django.middleware.common.CommonMiddleware',
]

# config 설정 : 마지막에
CORS_ORIGIN_ALLOW_ALL = True
# 만약에 특정한 오리진만 허용하려면
# CORS_ORIGIN_WHITELIST = [
#     'localhost: 8080',
#     'naver.com',
#     ]
```

- 오류 해결!

```html
<div id="app">
</div>
<script>
    const app = new Vue ({
        el: "#app",
        data: {
            musics: {

            }
        },
        methods: {
            getMusics : function() {
                const djangoUrl = "http://django-intro-injeong.c9users.io:8080/api/v1/musics/"
                // axios를 통한 요청은 promise 객체를 리턴
                axios.get(djangoUrl)
                // resolve 되면 (성공하면), then으로 처리
                    .then(response => {
                    console.log(response)
                }) // 반드시 에러메세지 해주세요!
                // reject 되면 (실패하면), catch로 처리
                    .catch(error => {
                    console.log(error)
                })

            }
        }
    })

</script>
```



- django에서 music 목록 새로고침하면 바로 실행되도록!

```js
// 새로고침하면 실행 됨.
mounted: function() {
    this.getMusics()
},
    methods: {
        getMusics : function() {
            const djangoUrl = "http://django-intro-injeong.c9users.io:8080/api/v1/musics/"
            // axios를 통한 요청은 promise 객체를 리턴
            axios.get(djangoUrl)
            // resolve 되면 (성공하면), then으로 처리
                .then(response => {
                this.musics = response.data
            })
            // 반드시 에러메세지 해주세요!
            // reject 되면 (실패하면), catch로 처리
                .catch(error => {
                console.log(error)
            })

        }
    }
```

- 댓글까지 가져오기

```html
<h1> 노래 목록 </h1>
<div v-for="music in musics">
    <b>{{ music.id }}</b> {{ music.artist_name }} : {{ music.title }}
    <div v-for="comment in music.comment_set">
        <p>댓글 : {{ comment.content }}</p>
    </div>
    <hr>
</div>
```



- vue devtools - 파일 url 허용 : 바뀌는 내용을 볼 수 있다.



- 댓글 작성

```js
addnewComment: function(music) {
    const musicId = music.id
    // django라면 form에서 받아서 저장할 정보 == data
    // 그래서 굳이 music id 를 넘기지 않아도 된다.
    const data = {'content': music.newComment}
    axios.post(`http://django-intro-injeong.c9users.io:8080/api/v1/musics/${musicId}/comments/`, data)
        .then(response => {
        music.comment_set.push(response.data),
            music.newComment = ''
    })
        .catch((error) => {
        console.log(error)
    })

}
```



- html을 github에 올리고 django를 헤로쿠에 올려서 돌려놓으면 언제든지 열어서 실행할 수 있다.



- B반 교재에서 router 대신에 axios로 한거일 뿐 나머지 똑같!



- 댓글 삭제

```js
deleteComment: function(music, comment) {
    const musicId = music.id
    const commentId = comment.id
    axios.delete(`http://django-intro-injeong.c9users.io:8080/api/v1/musics/${musicId}/comments/${commentId}/`)
        .then(
        music.comment_set.pop()
    )
        .catch((error) => {
        console.log(error)
    })
}
```



