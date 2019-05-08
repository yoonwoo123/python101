# 0508 JS Vue - 파이어베이스

firebase- DB(NoSQL)

1. push

   ```html
   <!-- html의 head 태그 부분에 4줄 복사 -->
   <!-- Firebase -->
   <script src="https://gstatic.com/firebasejs/5.8.0/firebase.js"></script>
   <!-- VueFire -->
   <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
   <script>
       // Initialize Firebase
       // TODO: Replace with your project's customized code snippet
       const config = {
           apiKey: "AIzaSyD3g5YCuZMYQymVqyDcmrNYvnBnqm9tX68", // 나의 apiKey
           databaseURL: "https://vue-project-yoon.firebaseio.com/", // 내 URL
           projectId: "vue-project-yoon", // 내 프로젝트Id
       };
       firebase.initializeApp(config);
       const db = firebase.database()
   </script>
   ```

   

* 자바스크립트 + node.js => 서버 구축 가능
* npm install -g firebase-tools

* node.js

firebase 설치

firebase init 후 1번과 4번 스페이스 누르고 엔터 2번에 y

<https://github.com/firebase/firebaseui-web>