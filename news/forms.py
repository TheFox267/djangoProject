from django import forms

from news.models import News


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class FeedbackForm(forms.Form):
    header = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута тема обращения'}), max_length=150, label='Тема обращения')
    content_mail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Тута контент обращения','rows':5}), label='Контент обращения')

