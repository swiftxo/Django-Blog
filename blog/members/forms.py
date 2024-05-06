from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from my_blog.models import Profile
from django.core.validators import MaxLengthValidator


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',   'first_name', 'last_name', 'email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio', 'profile_pic', 'instagram_link', 'twitter_link',
            'website_link', 'github_link','discord_link', 'spotify_link', 'soundcloud_link', 'youtube_link'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control full-width'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'spotify_link': forms.URLInput(attrs={'class': 'form-control'}),
            'soundcloud_link': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_link': forms.URLInput(attrs={'class': 'form-control'}),
            'discord_link': forms.URLInput(attrs={'class': 'form-control'}),
        }
        validators = {
            'bio': [MaxLengthValidator(300)]
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=150, widget= forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password',   'new_password1', 'new_password2',)
    