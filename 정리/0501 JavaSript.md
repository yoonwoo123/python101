# 0501 JS

---

### Review

```html
    <script>
        // 1. 배열 반복하면서 출력
        // 1-1. for of
        const avengers = ['캡틴아메리카', '닥터스트레인지', '토르', '헐크', '블랙위도우', '캡틴마블', '스파이더맨', '아이언맨']
        for (const avenger of avengers) {
            console.log(avenger)
        }
        // 1-2. forEach
        avengers.forEach( function (heroName) {
            console.log(heroName)})
        // 1-3. forEach + arrow
        avengers.forEach(avenger => console.log(avenger))

        // 2. map
        const numbers = [1, 2, 3]
        const strNumbers = numbers.map(number => String(number))
        console.log(strNumbers)

        const squareNumbers = numbers.map(number => number * number)
        console.log(squareNumbers)

        const squareNumbers2 = numbers.map(function(number){ // 위랑 같은 코드인데 arrow를 뺀 기본형태
            return number*number
        })
        console.log(squareNumbers2)
        
        const youngwoo = [
            {'velocity': 40, 'time': 50},
            {'velocity': 100, 'time': 50},
            {'velocity': 20, 'time': 100},
        ]
        const distances = youngwoo.map(obj => obj.velocity * obj.time)
        console.log(distances)

        // 3. filter 여러개를 걸러줄 수 있다.
        const nums = [1, 5, 6, 8]
        const evenNums = nums.filter(num => num%2 === 0)
        console.log(evenNums)
        const drinks = [
            {type: 'caffeine', name: 'cold brew'},
            {type: 'caffeine', name: 'green tea'},
            {type: 'juice', name: 'orange'},
            {type: 'juice', name: 'mango'}
        ]
        const noCaffeine = drinks.filter(drink => drink.type !== 'caffeine')
            //.map(obj => obj.name) name으로 출력하게 하고 싶을 때
        console.log(noCaffeine)

        // 4. reduce
        const reduceNum = [1, 5, 6]
        const reduceResult = reduceNum.reduce((result, num) => result += num*10, 0)
        console.log(reduceResult)

        // 5. find 배열에서 특정값 하나를 찾아준다.
        const dc = ['슈퍼맨', '배트맨', '아쿠아맨', '조커']        
        const badguy = dc.find(name => name === '조커')
        console.log(badguy)
    </script>
```

### event

```html
# event.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .bg {
            background-color: #F7F7F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
    </style>
</head>
<body>
    <div class="bg">
        <img id="dino" width="100px" heigth="100px" src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg" alt="dino">
    </div>

    <script>
        let y = 0
        // 무엇을
        const dinoImage = document.querySelector('#dino')
        // 언제
        dinoImage.addEventListener('click', function(e) {
            // 무엇을
            console.log(e)
            const bgDiv = document.querySelector('.bg')
            bgDiv.append('크앙')
        })
        document.addEventListener('keydown', function(e) {
            console.log(e)
            if (e.keyCode === 38) {
                console.log('위로가')
                y -= 30
                dinoImage.style.marginTop = `${y}px`
            }
            if (e.keyCode === 40) {
                console.log('아래로가')
                y += 30
                dinoImage.style.marginTop = `${y}px`
            }
            if (e.keyCode === 37) {
                console.log('좌로가')
                y -= 30
                dinoImage.style.marginLeft = `${y}px`
            }
            if (e.keyCode === 39) {
                console.log('우로가')
                y += 30
                dinoImage.style.marginLeft = `${y}px`
            }


        })
    </script>
</body>
</html>
```

### 03 멍멍이

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
</head>
<body>
    <h1>댕댕이 vs 키티</h1>
    <button id="dog">멍멍이 내놔</button>
    <button id="cat">떼껄룩 내놔</button>
    <div id="animals"></div>

    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        const getDogImage = function() {
            axios.get('https://dog.ceo/api/breeds/image/random')
            .then(response => response.data.message)
            .then(url => {
                const imageTag = document.createElement('img') // 태그 만들어주기
                imageTag.src = url
                const animal = document.querySelector('#animals')
                animal.append(imageTag)
            })
        }

        // 버튼을 누르면 이미지가 나오도록
        const dogbt = document.querySelector('#dog')
        dogbt.addEventListener('click', getDogImage)
    </script>

    <script>
        const getCatImage = function() {
            axios.get('https://api.thecatapi.com/v1/images/search')
            .then(response => response.data[0].url)
            .then(url => {
                const imageTag = document.createElement('img')
                imageTag.src = url
                const animal = document.querySelector('#animals')
                animal.append(imageTag)
            })
        }
        const catbt = document.querySelector('#cat')
        catbt.addEventListener('click', getCatImage)
    </script>



    
</body>
</html>
```



