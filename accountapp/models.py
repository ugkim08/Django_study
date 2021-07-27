from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # null = false는 text변수가 없어도 되는지 설정하는 파라미터 필수값으로 설정하려면 false로. 선택값으로 설정하려면 ture로
