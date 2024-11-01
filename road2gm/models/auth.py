from django.db import models
from model_utils import models as model_utils_models


class User(model_utils_models.TimeStampedModel):
    username = models.CharField(
        verbose_name='아이디',
        max_length=150,
    )

    password = models.CharField(
        verbose_name='비밀번호',
        max_length=128,
    )

    email = models.CharField(
        verbose_name='이메일',
        max_length=254,
    )

    remember_me = models.BooleanField(
        verbose_name='로그인 유지',
        default=False,
    )

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
        db_table = 'user'

    def __str__(self):
        return self.username


class RefreshToken(model_utils_models.TimeStampedModel):
    username = models.CharField(
        verbose_name='아이디',
        max_length=150,
    )

    token = models.CharField(
        verbose_name='토큰',
        max_length=128,
    )

    ip_address = models.GenericIPAddressField(
        verbose_name='IP 주소',
    )

    class Meta:
        verbose_name = '리프레시 토큰'
        verbose_name_plural = '리프레시 토큰'
        db_table = 'refresh_token'
        indexes = [
            models.Index(fields=['token', 'ip_address']),
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return self.token
