from django.db import models

# Create your models here.

# 사용자 정보 모델
class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=127)
    username = models.CharField(max_length=63)
    gender = models.CharField(max_length=15, choices=[
        ("남", "남성"),
        ("여", "여성")
    ])
    reg_date = models.DateTimeField(auto_now_add=True, null=False)
    mod_date = models.DateTimeField(auto_now=True, null=False)
