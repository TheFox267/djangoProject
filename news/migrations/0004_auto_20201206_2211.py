# Generated by Django 3.1.4 on 2020-12-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='audio',
            field=models.FileField(default=0, upload_to='audio/%Y/%m/%d/', verbose_name='аудио'),
        ),
    ]
