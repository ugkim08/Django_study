from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# created_at = models.DataField(auto_now_add=True, null=True)

# 36강_ 10번 라인은 게시글을 작성한 유저가 탈퇴하더라도 해당 게시물이 삭제되지 않도록 세팅하는 코드
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='artice', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='artice', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)