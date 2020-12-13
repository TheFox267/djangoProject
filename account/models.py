from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    class Gender(models.TextChoices):
        MAN = ('M', 'Мужской')
        WOMAN = ('W', 'Женский')
        OTHER = ('O', 'Другой')
        NS = ('NS', 'Не выбран')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', verbose_name='аватар', default='avatar/default_avatar.png')
    bio = models.TextField(verbose_name='о себе', blank=True)
    gender = models.CharField(choices=Gender.choices, default=Gender.NS, verbose_name='пол', max_length=2)
    date_of_birth = models.DateField(verbose_name='дата рождения', blank=True)
    native_city = models.CharField(max_length=100, verbose_name='родной город', blank=True)
    languages = models.CharField(max_length=100, verbose_name='языки', blank=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True)
    city = models.CharField(max_length=100, verbose_name='город', blank=True)
    mobile_phone = models.CharField(max_length=50, verbose_name='мобильный телефон', blank=True)
    add_phone = models.CharField(max_length=50, verbose_name='доп. телефон', blank=True)
    skype = models.CharField(max_length=100, verbose_name='skype', blank=True)
    personal_site = models.URLField(verbose_name='личный сайт', blank=True)
    job = models.CharField(max_length=100, verbose_name='профессия', blank=True)

    def __str__(self):
        return f'Профиль: {self.user.username}'

    def get_absolute_url(self):
        return reverse('account:profile_user', kwargs={'pk': self.pk})
