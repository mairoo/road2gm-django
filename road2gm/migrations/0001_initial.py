# Generated by Django 5.1.2 on 2024-11-13 12:29

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
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='아이디')),
            ],
            options={
                'verbose_name': '역할',
                'verbose_name_plural': '역할',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='OAuth2Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.CharField(max_length=150, verbose_name='이메일')),
                ('token', models.CharField(max_length=128, unique=True, verbose_name='상태')),
            ],
            options={
                'verbose_name': '소셜연동 임시코드',
                'verbose_name_plural': '소셜연동 임시코드',
                'db_table': 'oauth2_token',
                'indexes': [models.Index(fields=['token'], name='oauth2_toke_token_4bdcbd_idx'), models.Index(fields=['created'], name='oauth2_toke_created_ccbb8d_idx')],
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.CharField(max_length=150, verbose_name='이메일')),
                ('token', models.CharField(max_length=128, verbose_name='토큰')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP 주소')),
            ],
            options={
                'verbose_name': '리프레시 토큰',
                'verbose_name_plural': '리프레시 토큰',
                'db_table': 'refresh_token',
                'indexes': [models.Index(fields=['token', 'ip_address'], name='refresh_tok_token_7a9ce0_idx'), models.Index(fields=['created'], name='refresh_tok_created_32b2d8_idx')],
            },
        ),
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
                ('roles', models.ManyToManyField(blank=True, to='road2gm.role', verbose_name='역할')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('provider', models.CharField(max_length=32, verbose_name='소셜로그인')),
                ('uid', models.CharField(max_length=254, verbose_name='소셜로그인 식별자')),
                ('extra_data', models.TextField(verbose_name='추가 정보')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='road2gm.user')),
            ],
            options={
                'verbose_name': '소셜연동계정',
                'verbose_name_plural': '소셜연동계정',
                'db_table': 'social_account',
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
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='user_usernam_b79065_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='user_email_7bbb4c_idx'),
        ),
    ]
