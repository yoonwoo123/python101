# 0503 JavaScript Vue

---

* 명령형 , MVVM (Model View View Model)



### 01_Vue.html

```html
<body>
    <div id="app">
        <button v-on:click='plus'>Count증가하쟈</button>
        {{ message }} - {{ count }}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script>
        const app = new Vue ({
            // element: 실제 Vue와 연결 할 element
            el: "#app",
            // app (vue 인스턴스)의 속성을 가지게 된다.
            data: {
                message: 'Hello, Vue!',
                count: 0
            },
            methods: {
                plus: function() {
                    this.count ++
                }
            }
        })

    </script>
</body>
```

---

### 활용

```
app.message
"Hello, Vue!"
app.message = 'Hello, 영우'
"Hello, 영우"
app.message = 'bye'
"bye"
app.plus() ==> count가 1씩 증가한다.
undefined
app.plus()
undefined
```

arrow function => lexical this 와 같다



### 02_todo.html

```html
<body>
    <div id="app">
        <!-- v-model : data의 newTodo 값이 사용자가 입력하는 값으로 변경됨.-->
        <input type="text" v-model="newTodo" v-on:keyup.enter="addNewTodo"><br>
        {{ newTodo }}
        <button v-on:click="allComplete">[전부 완료]</button>
        <ul>
            <!-- v-for가 우선, v-if가 나중 | 그래야 for에서 하나씩 나오며 if를 해주기 때문이다. -->
            <li v-for="todo in todoList" v-if="!todo.completed">
                {{ todo.content }} <button v-on:click='complete(todo)'>[완료]</button>
            </li>
            <li v-else>
                <span style="color: red">
                    <del>{{ todo.content }}</del>
                </span>
                <button v-on:click='complete(todo)'>[취소]</button>
            </li>
        </ul>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                newTodo: '',
                todoList: [
                    { 
                        content: '쉬는 시간 놀기',
                        completed: true
                    },
                    {
                        content: '전골 먹기',
                        completed: false
                    },
                    {
                        content: '취업 특강 들으면서 자기',
                        completed: false
                    },
                    {
                        content: '어벤저스보기',
                        completed: false
                    }
                ]
            },
            methods: {
                complete: function(todo) {
                    todo.completed = !todo.completed // true -> false , false -> true 로
                },
                addNewTodo: function() {
                    // this : Vue 오브젝트(app)
                    // this.todoList : data의 todoList
                    if (this.newTodo) {
                        this.todoList.push({
                            // this.newTodo : data의 newTodo (사용자가 입력을 한 값)
                            content: this.newTodo,
                            completed: false
                        })
                        this.newTodo = ""
                    }
                },
                allComplete: function(){
                    // this.todoList.forEach(todo => {  // 이렇게 arrow로 해서 check함수로
                    //    if (!todo.completed) {        // 확인할 수 있으나 아직은 이해만하는걸로
                    //        this.check(todo)
                    //    }
                    //})
                    this.todoList.forEach(function(todo){
                        todo.completed = true
                })
                }
            } 
        })
    </script>
</body>
```

### 03_dogvue.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        img {
            width: 300px;
            height: 300px;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        <button v-on:click="getDogImage">댕댕이 {{ dogCount }} 마리~ </button><br>
        <img 
            v-for="image in images"
            v-bind:src="image"
        >   
    </div>

    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        const getDogImage = function() {
            axios.get('https://dog.ceo/api/breeds/image/random')
                .then( response => {
                    this.images.push(response.data.message)
                    this.dogCount += 1 // 강아지 이미지가 추가될때마다 카운트 += 1
                })
        }
        const app = new Vue({
            el: '#app',
            data: {
                images: [],
                dogCount: 0 // 1. data에 추가하고 싶은 값을 담고
            },
            methods: {
                getDogImage
            }
        })    
    </script>
</body>
</html>
```

### this 쓸 때 숙지해야할 점!

> 1. 모든 함수는 function 키워드로 
> 2.  메서드에서 쓰이는 함수 중에 콜백 함수는 arrow function
> 3. 메서드 정의 시에는 function 키워드

