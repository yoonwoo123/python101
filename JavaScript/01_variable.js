// alert('자바 스크립트, 안녕!')    # 한 줄 주석 처리는 //
/*  여러줄 주석처리 시 
console.log('안녕?')
console.log('bye !')
*/
document.write('<h1>SSAFY 최고</h1>')
// 변수 hoisting
// 자바스크립트에서 모든 선언과 관련된 (변수, 함수 등) 문장은 호이스팅 된다.\
// 변수는 1) 선언단계 2) 초기화 단계 3) 할당 단계를 거치게 된다.
console.log(name) // undefiend
var name = "영우"
console.log(phonenumber) // phonenumber is not defined error(Reference Error)

// let, const 키워드 (ES6+)
console.log(a)
var a = 5
console.log(a) // 에러가 발생하지 않음.

// let b = 5
// let b = 3 // 에러 발생

for (var i = 0; i < 3; i++) {
    console.log(i)
}
console.log('===============')
console.log(i) // i 값이 3임.


for (let j = 0; j < 3; j++) {
    console.log(j)
}
console.log('===============')
console.log(j)  // j 값이 없음, 오류 발생.