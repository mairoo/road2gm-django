# Generated by Django 5.1.2 on 2024-11-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road2gm', '0004_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='road2gm.role', verbose_name='역할'),
        ),
    ]
