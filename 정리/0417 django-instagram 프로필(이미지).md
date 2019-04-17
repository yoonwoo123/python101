# 0417 django-instagram 프로필(이미지)

* accounts의 models.py 에 class Profile을 만든다.
* imagekit 은 pip install pillow pilkit django-imagekit 로 설치

```python
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Profile(models.Model):                                                        # CASCADE 는
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # user가 삭제가 될때
    nickname = models.CharField(max_length=30)                                      # Profile도 같이 삭제
    introduction = models.TextField()
    image = ProcessedImageField(
                    processors=[ResizeToFill(300, 300)],
                    format="JPEG",
                    options = {'quality': 80},
        )
```

