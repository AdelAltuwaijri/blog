# Generated by Django 3.0.6 on 2020-05-25 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200524_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enail', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-post_date',)},
        ),
    ]
