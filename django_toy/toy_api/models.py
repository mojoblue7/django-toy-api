from django.contrib.auth.hashers import is_password_usable, make_password
from django.db import models
from django.utils import timezone

# Create your models here.

# 사용자 정보 모델
from django.db.models.signals import pre_save
from django.dispatch import receiver


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

    def __str__(self):
        UserInfo.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
        return self.id


@receiver(pre_save, sender=UserInfo)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.password):
        instance.password = make_password(instance.password)
