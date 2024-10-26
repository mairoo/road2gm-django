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

    refresh_token = models.CharField(
        verbose_name='리프레시 토큰',
        max_length=256,
        null=True,
        blank=True,
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
