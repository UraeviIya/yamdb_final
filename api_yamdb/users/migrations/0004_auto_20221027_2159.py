# Generated by Django 2.2.16 on 2022-10-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221026_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Администратор'), ('user', 'Пользователь'), ('moderator', 'Модератор')], default='user', max_length=30, null=True, verbose_name='Роль'),
        ),
    ]
