# Generated by Django 3.1.4 on 2020-12-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201205_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/%Y/%m/%d/', verbose_name='аудио'),
        ),
    ]
