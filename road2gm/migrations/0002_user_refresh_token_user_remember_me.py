# Generated by Django 5.1.2 on 2024-10-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road2gm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='리프레시 토큰'),
        ),
        migrations.AddField(
            model_name='user',
            name='remember_me',
            field=models.BooleanField(default=False, verbose_name='로그인 유지'),
        ),
    ]
