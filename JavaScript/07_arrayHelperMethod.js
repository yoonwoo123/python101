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