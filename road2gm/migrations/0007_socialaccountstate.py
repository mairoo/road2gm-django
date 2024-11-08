# Generated by Django 5.1.2 on 2024-11-08 02:57

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road2gm', '0006_remove_refreshtoken_username_refreshtoken_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccountState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.CharField(max_length=150, verbose_name='이메일')),
                ('state', models.CharField(max_length=128, unique=True, verbose_name='상태')),
            ],
            options={
                'verbose_name': '소셜연동 임시코드',
                'verbose_name_plural': '소셜연동 임시코드',
                'db_table': 'social_account_state',
                'indexes': [models.Index(fields=['state'], name='social_acco_state_f5e850_idx'), models.Index(fields=['created'], name='social_acco_created_c43f4b_idx')],
            },
        ),
    ]