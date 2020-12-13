from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from account.models import Profile


class RegisterAccountForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута логин'}), max_length=100, label='Логин пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Тута мыло'}), max_length=64, label='Почтовый ящик')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Тута пароль'}), max_length=50, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Тут тоже пароль'}), max_length=50, label='Подтверждение пароля')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class LoginAccountForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута логин'}), max_length=100, label='Логин пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Тута пароль'}), max_length=50, label='Пароль')


class DateInput(forms.DateInput):
    input_type = 'date'


class EditProfileAccountForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Тута о себе', 'row': 1}), label='О себе', required=False)
    avatar = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}), label='Аватар')
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Profile.Gender.choices, label='Пол', required=False)
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Тута дата'}), label='День рождения',
                                    required=False)
    native_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута родной город'}), label='Родной город', required=False)
    languages = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута языки'}), label='Языки', required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута страна'}), label='Страна', required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута город'}), label='Город', required=False)
    mobile_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута мобильный телефон', 'type': 'tel', 'id': 'phone'}),
                                   label='Мобильный телефон', required=False)
    add_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута доп. телефон', 'type': 'tel', 'id': 'phone'}),
                                label='Доп. телефон', required=False)
    skype = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута skype'}), label='Skype', required=False)
    personal_site = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Тута ссылка на твой сайт'}), label='Личный сайт', required=False)
    job = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тута проффесия'}), label='Проффесия', required=False)

    class Meta:
        model = Profile
        exclude = ('user',)
