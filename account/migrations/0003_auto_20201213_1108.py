# Generated by Django 3.1.4 on 2020-12-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0002_auto_20201213_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar/default_avatar.png', upload_to='avatar/%Y/%m/%d/', verbose_name='аватар'),
        ),
    ]
