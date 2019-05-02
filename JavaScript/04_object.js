// 자바스크립트 데이터타입 - 원시타입(primitive type)
    // Boolean(True, False), Null, undefined, number, string

    // 자바스크립트 object 표기법
    let youngwoo = {
        name: 'youngwoo',
        age: 26,
        phonenumber: '010-8947-2935'
    }
    console.log(youngwoo.name) // 'youngwoo'
    console.log(youngwoo.age) // 26
    console.log(typeof youngwoo) // object
    console.log(typeof [1, 2, 3]) // object

    // ES6+ 주가 오브젝트 표현법
    // 변수를 그대로 넣으면, 변수명: 값
    let name = 'injeong'
    let stuffs = ['텀블러', '안경']
    let injeong = {
        name: name,
        stuffs: stuffs
    }
    // json <-> object ( json이랑 object 바꾸는 법 )
    let jsonData = JSON.stringify(injeong) // 오브젝트를 json 문자열로 바꿔주고
    let jsonParse = JSON.parse(jsonData) // json 문자열을 json 오브젝트로 바꿔주는 구조