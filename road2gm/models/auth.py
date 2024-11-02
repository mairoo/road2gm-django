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

    roles = models.ManyToManyField(
        'road2gm.Role',
        verbose_name='역할',
        blank=True,
    )

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
        db_table = 'user'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.username


class Role(model_utils_models.TimeStampedModel):
    name = models.CharField(
        verbose_name='아이디',
        max_length=150,
    )

    parent = models.ForeignKey(
        'road2gm.Role',
        verbose_name='부모',
        db_index=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = '역할'
        verbose_name_plural = '역할'
        db_table = 'role'

    def __str__(self):
        return self.name


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
