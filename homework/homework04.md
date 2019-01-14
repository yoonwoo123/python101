# 구글 드라이브:zzu.li/day1

# homework04

1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

   ```python
   False, None, True, and 등이 있다.
   ```






2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.
   (floating point rounding error)
   따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

   ​			a = 0.1 * 3
   ​			  b = 0.3

   ```python
   import math
   math.isclose(a, b) 
   # 혹은
   a = 0.1 * 3
   b = 0.3
   abs(a-b) < 1e-5
   ```
     python 3.5 부터 

3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \ 을 작성하세요.
\n , \t, \\




4. “안녕, 철수야”를 String Interpolation을 사용하여 출력하세요.

```python
name = "철수"
print(f'안녕, {name}야')
```



5. 다음 중 형변환시 오류가 발생하는 것은?
    1) str(1) 2) int(‘30’)
    3) int(5) 4) bool(‘50’)
    5) int(‘3.5’)

    int('3.5') 입니다. int 안의 수는 정수여야 하기 때문입니다.

6. 변경할 수 있는 (mutable) 것과 변경 불가능한 것 (immutable)을 분류하시오.

String, Tuple, Range = immutable


list, set, dic = mutable