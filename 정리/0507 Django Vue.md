# 0507 Django Vue

---

### 시험에 나올만한 것들

```
NaN
NaN
typeof NaN
"number"
NaN === NaN
false
NaN === 'asdf'
false
NaN === 1
false
isNaN(NaN)
true
isNaN(0)
false
typeof Infinity
"number"
typeof []
"object"
typeof () => {}
VM286:1 Uncaught SyntaxError: Malformed arrow function parameter list
typeof {}
"object"
typeof [1, 2, 3]
"object"
typeof true
"boolean"
typeof typeof 'asdf'
"string"
1 + '1'
"11"
2 * '12'
24
parseInt('123')
123
typeof function() {}
"function"
typeof (() => {})
"function"
'a'.repeat(2) 
'aa'
```

---

## 01_vue.html 추가

```html
<body>
    <!--MVVN-->
    <!-- v-____ 브이 하이픈은 디렉티브(Directive)
        vue의 element에 지시를 하는 문법
        값에 해당하는 부분 (="_______") 자바스크립트 문법을 사용 할 수 있따.
    -->
    <div id="app">
        <!-- v-on: 이벤트 리스너를 등록 
            축약형 : @____
        -->
        <!-- v-once : 렌더링 되었을 때의 값,
            이후에 data값이 바뀌더라도 바뀌지 않음
        -->
        <button v-on:click='plus'>v-on:click</button>
        <button @click='plus'>@click</button>
        {{ message }} - {{ count }}
        <span v-text= "htmlMessage"></span> <!--해당하는 값을 그대로 출력-->
        <span v-html= "htmlMessage"></span> <!--태그가 있으면 html로 출력-->
        <!--v-if는 렌더링을 할지 말지 결정함
            html 태그 자체를 보여줄지 말 지
        -->
        <h1 v-once v-text="count"></h1>
        <span v-if="count > 5">5보다 큼!</span>
        <h1 v-else-if=" count === 5"> 5!!!!!!!!! </h1>
        <span v-else="count < 5">5 보다 작음 !</span>
        <!--v-show는 렌더링을 무조건 하고, css로 화면에 보여줄지 말지를 결정함.-->
        <h1 v-show="isTrue">!!</h1> <!--v-if와 비슷함-->
        <li v-for="hero in myArray">
            {{ hero }}
        </li>
        <a v-bind:href="urlLink">구글</a>
        <a :href="urlLink">구글</a>
        <input v-model="blahblah"><br>
        {{ blahblah }} <br>
        {{ blahblah + '!!!!!' }} <br>
        {{ reverseBlahblah }} <br>
        <select v-model='lunch'>
            <option value="특식">특식</option>
            <option value="한식">한식</option>
            <option value="가운데">가운데</option>
        </select>
        <h1>{{ lunch }}</h1>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // 특정한 값 가져올 때
        // app.$el (new Vue 전부를 선택한다.)
        // app.$data.message === app.message (기본형과 축약형)
        const app = new Vue ({
            // element: 실제 Vue와 연결 할 element
            el: "#app",
            // app (vue 인스턴스)의 속성을 가지게 된다.
            data: {
                lunch: '뭐먹지',
                blahblah: '',
                message: 'Hello, Vue!',
                htmlMessage: '<p>안녕</p>',
                count: 0 ,
                isTrue : false ,
                myArray: [
                        '캡틴아메리카' ,
                        '헐크' ,
                        '아이언맨'
                    ],
                urlLink: "https://google.com"
            },
            methods: {
                plus: function() {
                    this.count ++
                },
                today: function() {
                    return new Date()
                }
            },
            // computed: 캐싱! 
            computed: {
                reverseBlahblah: function() {
                    return this.blahblah.split('').reverse().join('')
                },
                computedToday: function() {
                    return new Date()
                }
            }
        })

    </script>
</body>
```

### 시험 | app.today() 와 app.computedToday 의 차이점

`app.today()` method 는 값을 호출할 때 마다 값을 계산해서 알려주고

`app.computedToday` 는 computed ( 캐싱 ) 값을 계산된 결과를 저장해놓고 그것만 불러옴

```
ex)
app.today()
Tue May 07 2019 10:24:03 GMT+0900 (한국 표준시)
app.computedToday
Tue May 07 2019 10:24:09 GMT+0900 (한국 표준시)
app.computedToday
Tue May 07 2019 10:24:09 GMT+0900 (한국 표준시)
app.today()
Tue May 07 2019 10:24:29 GMT+0900 (한국 표준시)
```

## 04_qna.html

```html
<body>
    <div id="app">
        <h1 v-text="title"></h1>
        <input v-model="question"><br>
        <h2> {{ answer | answerCapital }} </h2>
        <img v-bind:src="imageUrl">
    </div>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
    const app = new Vue({
        el: '#app',
        data: {
            title: '무엇이든 물어오세요.',
            question: '',
            answer: '질문을 해주세요...',
            imageUrl: ''
        },
        
        methods: {
            getAnswer: function() {
                if (this.question[this.question.length-1] === '?') {
                    axios.get('https://yesno.wtf/api')
                    .then(response => {
                        console.log(response)
                        this.answer = response.data.answer
                        this.imageUrl = response.data.image
                    })
                } else {
                    this.answer = '?로 질문을 마무리해주세요!!'
                    return
                }
            }
        },
        // 데이터가 변화하는 것을 지켜보는 watch!
        watch: {
            question: function(){
                this.getAnswer()
            }
        },
        filters: {
            answerCapital: function(answer) {
                // if (answer === 'yes' || answer === 'no') {
                //     return answer.toUpperCase() + '!!!!!!!'
                // } else {
                //     return answer
                // }
                // 상황연산자
                return (answer === 'yes' || answer === 'no') ? answer.toUpperCase() + '!!!!!!!' : answer
            }
        }
    })
    </script>
</body>
```



### 시험 | 삼항연산자

```javascript
answerCapital: function(answer) {
                // if (answer === 'yes' || answer === 'no') {
                //     return answer.toUpperCase() + '!!!!!!!'
                // } else {
                //     return answer
                // }
                // 삼항연산자
                return (answer === 'yes' || answer === 'no') ? answer.toUpperCase() + '!!!!!!!' : answer
            }
```

이벤트 리스너는 애로우 쓰지 말자



### 시험 | v-on / v-bind

* v-on => @  ex) v-on:click => @click

* v-bind => 없애도 됨 ex) v-bind:class => :class 



### todo_html ()

filter는 검사해서 true인 것들만 모아준다.



### 시험 | this

arrow 에서 this 를 쓰면 상위로 간다.

일반함수에서 this 를 쓰면 window

json은 오브젝트가 아닌 문자열이다 !!!!