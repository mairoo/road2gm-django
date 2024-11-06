# Generated by Django 5.1.2 on 2024-11-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road2gm', '0002_alter_role_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='이미지 경로'),
        ),
        migrations.AddField(
            model_name='user',
            name='provider',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='소셜로그인'),
        ),
        migrations.AddField(
            model_name='user',
            name='provider_id',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='소셜로그인 식별자'),
        ),
    ]
