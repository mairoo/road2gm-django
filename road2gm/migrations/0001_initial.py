# Generated by Django 5.1.2 on 2024-10-31 19:01

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(max_length=150, verbose_name='아이디')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('email', models.CharField(max_length=254, verbose_name='이메일')),
                ('remember_me', models.BooleanField(default=False, verbose_name='로그인 유지')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('thumbnail', models.CharField(max_length=128, verbose_name='썸네일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='road2gm.user', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '책',
                'verbose_name_plural': '책',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('token', models.CharField(max_length=128, verbose_name='토큰')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP 주소')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='road2gm.user', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '리프레시 토큰',
                'verbose_name_plural': '리프레시 토큰',
                'db_table': 'refresh_token',
                'unique_together': {('token', 'ip_address')},
            },
        ),
    ]
