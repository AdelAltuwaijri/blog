# Generated by Django 3.0.6 on 2020-05-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200525_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='التعليق'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='البريد الالكتروني'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
    ]
