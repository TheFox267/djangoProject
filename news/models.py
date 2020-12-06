from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Count
from django.urls import reverse


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='автор', default=None)
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='постер', default='photos/default.svg')
    is_published = models.BooleanField(default=True, verbose_name='статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория', db_index=True, default=None)
    audio = models.FileField(upload_to='audio/%Y/%m/%d/', verbose_name='аудио', default=0)

    def __str__(self):
        return f"Заголовок новости: {self.title}"

    def get_absolute_url(self):
        return reverse('news:detail_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок', unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('news:detail_category', kwargs={'category_id': self.pk})
