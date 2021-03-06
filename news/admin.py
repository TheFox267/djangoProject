from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from news.models import Category, News


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'author', 'title', 'created_at', 'is_published', 'category']
    list_filter = ['created_at', 'category']
    list_display_links = ['id', 'title', 'category', 'author']
    list_editable = ['is_published']
    actions = ['publish', 'hide']

    def publish(self, request, queryset):
        queryset.update(is_published=1)

    publish.short_description = 'Опубликовать выбранные новости'

    def hide(self, request, queryset):
        queryset.update(is_published=0)

    hide.short_description = 'Скрыть выбранные новости'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
