# template_example

## 1. 반복문

```html
{% for menu in my_list %}
    {{ forloop.counter }} <!-- forloop.counter는 %가 아닌 {} 를 쓴다 -->
    {% if forloop.first %}
        <p>짜장면+고추가루</p>
    {% else %}
        <p>{{ menu }}</p>
    {% endif %}
{% endfor %}
{% for user in empty_list %}
    <p>{{ user }}</p>
    {% empty %}
        <p>지금 가입된 유저가 없습니다.</p>
{% endfor}
```

## 2. 조건문

```html
{% if '짜장면' in my_list %}
    <p>짜장면은 고추가루 없이 못 먹지!</p>
{% endif %}
```

## 3. length 필터 활용

```html
{% for message in messages %}
    {% if message|length > 5 %}
        <p>글씨가 너무 길어요</p>
    {% else %}
        <p>{{ message }}, {{message|length }}</p>
    {% endif %}
{% endfor %}
```

## 4. lorem ipsum

```html
{% lorem %}
<hr>
{% lorem 3 w %}
<hr>
{% lorem 4 w random %}
<hr>
{% lorem 4 p %}
```

## 5. 글자 수 제한하기(truncate)

```html
<p>{{ my_sentence|truncatewords:3 }}</p>
<p>{{ my_sentence|truncatechars:10 }}</p>
```

## 6. 글자 관련 필터

```html
<p>{{ 'abc'|length }}</p>
<p>{{ 'ABC'|lower }}</p>
<h3>{{ my_sentence|title }}</h3>
<p>{{ 'abc def'|capfirst }}</p>
<p>{{ my_list|random }}</p>
```

## 7. 연산-django-mathfilters 쓰면 추가적 기능 사용가능

```html
<p>{{ 4|add:6 }}</p>0
```

## 8. 날짜표현

```html
{{ now }}<br>
{% now "SHORT_DATETIME_FORMAT" %}<br>
{% now "DATETIME_FORMAT" %}<br>
{% now "SHORT_DATE_FORMAT" %}<br>
{% now "DATE_FORMAT" %}<br>
{% now "Y년 m월 d일 (l) h:i" %}<br>
```

