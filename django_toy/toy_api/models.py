from django.contrib.auth.hashers import is_password_usable, make_password
from django.db import models
from django.utils import timezone

# Create your models here.

# 사용자 정보 모델
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

def gender_validator(value):
    if value != '남' or value != '여':
        raise forms.ValidationError('성별 선택해주세요')

class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(null=False, blank=False, validators=[min_length_3_validator])
    password = models.CharField(max_length=127, null=False, blank=False, validators=[min_length_3_validator])
    username = models.CharField(max_length=63, null=False, blank=False, validators=[min_length_3_validator])
    gender = models.CharField(max_length=15, choices=[
        ("남", "남성"),
        ("여", "여성")
    ], null=False, blank=False, validators=[gender_validator])
    reg_date = models.DateTimeField(auto_now_add=True, null=False)
    mod_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self) -> str:
        # UserInfo.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
        return str(self.id)

    class Meta:
        ordering = ['id']


@receiver(pre_save, sender=UserInfo)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.password):
        instance.password = make_password(instance.password)
