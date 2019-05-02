// 1. 함수 선언식
let result = add(1, 3)
function add(num1, num2) {
    return num1+num2
}
console.log(result)
// 2. 함수 표현식
let add2 = function (num1, num2) {
    return num1+num2
}
console.log(add2(1, 3))
// console.log(add3(1, 3))

// workshop
let concat = function (str1, str2) {
    return `${str1}-${str2}`
}

let checkLongStr = function (string) {
    if (string.length > 10) {
        return true
    } else {
        return false
    }
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}
//


// ES6+ Arrow Function
let sub = (num1, num2) => { // arrow function = >
    return num1-num2
}

// 인자가 하나인 경우, () 생략가능
// 단순 리턴인 경우, {} 및 리턴 키워드 생략 가능
let greeting = name => `${name}, 안녕!`
console.log(greeting('인정'))
let mul = (num1, num2) => num1 * num2
console.log(mul(5, 4))

// 인자가 없는 경우에는 () 작성
let hellow = () => 'hello, world!'
console.log(hellow())
// object 리턴 시 반드시 ()묶어서 작성
// let me
let me = (name, age) => ({name, age}) // return을 못해준다. undefined
console.log(me('hi', 3))

// 만약, default args (기본인자)
let bonjour = (name='동명') => `${name}, bonjour`

// 4. 익명 함수
(function (num) {return num*num})

// 5. 즉시 실행 함수 (익명함수 + 호출) - IIFE (Immediately Invoked Function Expression)
( num => num*num )(5)

let myNum = (function(num) {return num})

// 배열을 받아서 다 더해주는 함수를 작성 해주세요.
    // numberAddEach(numbers)

    const numberAddEach = numbers => {
        let sum = 0
        for (let number of numbers) {
            sum += number
        }
        return sum
    }
    console.log(numberAddEach([1, 2, 3]))

    const numberSubEach = numbers => {
        let sum = 0
        for (let number of numbers) {
            sum -= number
        }
        return sum
    }
    console.log(numberSubEach([1, 2, 3]))

    const numberMulEach = numbers => {
        let sum = 1
        for (let number of numbers) {
            sum *= number
        }
        return sum
    }
    console.log(numberMulEach([1, 2, 3]))

    const numberEach = (numbers, calc) => {
        let result 
        for (const number of numbers) {
            result = calc(number, result)
        }
        return result
    }

    const addEach = (number, result=0) => result + number
    const subEach = (number, result=0) => result - number
    const mulEach = (number, result=1) => result * number
    // 콜백 callback 
    console.log(numberEach([10, 20, 30], addEach))
    console.log(numberEach([10, 20, 30], subEach))
    console.log(numberEach([10, 20, 30], mulEach))
    // 익명함수 + 콜백
    console.log(numberEach([10, 20, 30], (number, result=0) => result + number))
    console.log(numberEach([10, 20, 30], function(number, result=0) {
        return result + number 
    }))