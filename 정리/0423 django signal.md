# 0423 django signal

signals.py , apps.py , settings.py 3개에 만들어줘야 signal을 사용할 수 있다.



## 2. 테스트 코드(TDD)

### 오류를 방지하기 위하여 그 상황이 나타나면 Failed가 뜨게 하는 것



pip install django_test_plus 를 깔아준다.

타키쌤이 올려준 형식을 git clone을 하여서 했지만 보통 tests.py라고 만들어서 작성

(git clone 후 makemigrations, migrate 해주기)

```python
from test_plus.test import TestCase
from django.conf import settings

class SettingsTest(TestCase):
    # 1. settings 값 확인
    def test_01_settings_locale(self):
        self.assertEqual(settings.USE_I18N, True)
        self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
        
from .models import Board

class BoardModelTest(TestCase):
    def test_01_model(self):
        board = Board.objects.create(title="테스트", content="내용", user_id=1)
        self.assertEqual(str(board), f'Board{board.pk}')
```

