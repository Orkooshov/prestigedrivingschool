from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms


user_model = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user_model
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user_model
        fields = ('email',)


class EditPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = user_model
        fields = ('username', 'email', 'phone_number', 'photo')


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)


class AuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
