from django.db import models
from model_utils import models as model_utils_models


class Book(model_utils_models.TimeStampedModel):
    title = models.CharField(
        verbose_name='제목',
        max_length=64,
    )

    author = models.ForeignKey(
        'road2gm.User',
        verbose_name='사용자',
        db_index=True,
        on_delete=models.CASCADE,
    )

    thumbnail = models.CharField(
        verbose_name='썸네일',
        max_length=128,
    )

    class Meta:
        verbose_name = '책'
        verbose_name_plural = '책'
        db_table = 'book'

    def __str__(self):
        return self.title
