from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from news.models import News


class AddNewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category', 'audio']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class FeedbackForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута тема обращения'}), max_length=150, label='Тема')
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Тута контент обращения', 'rows': 5}), label='Контент')
