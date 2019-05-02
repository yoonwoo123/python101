const firstName = 'happy'
const lastName = 'hacking'
const name = firstName + lastName
// document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)
document.write(`<h1>${name}</h1>`) // '' 가 아닌 `` 1 옆의 ` 두개

let userName = prompt('너 NUGU니?')
let message = `<h1>${userName}</h1>`
// document.write(message)

// 자바스크립트에서는 ===이 파이썬의 ==과 같은 비교 연산자이다.
// === : 일치함을 비교(값, 타입)
// == : 동등함을 비교(값) : 타입의 암묵적 변환 ( 타입이 달라도 True 반환 )
// 123 == '123' : True
// !== : ! = = 
// != : ! = 

if (userName === '영우') { // JS 조건문에서 파이썬의 == 과 같은걸 쓰려면 === 을 써야한다. 
    message = '<h1>영우는 들어와있어</h1>'
} else if (userName === '성민') {
    message = `<h1>${userName}은(는) 일하자!</h1>`
} else {
    message = `<h1>${userName}은(는) 수업듣자</h1>`
}
document.write(message)