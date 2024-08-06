from django.db import models
from accounts.models import User
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #user = models.ForeignKey()

    #User 모델을 참조하는 방법 
    # 1 직접 참조(권장하지 않음)
    #user = model.ForeignKey(user, on_delete=models.CASCADE)
    # 2 settings의 변수 활용 ->이걸 이번 수업시간에 사용하기로
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 3. get_user_model 함수를 활용
   # user = model.ForeignKey(get_user_model(), on_delete=models.CASCADE)