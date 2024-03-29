from django.forms import ModelForm, Textarea, ClearableFileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
             'first_name': 'Name',
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['first_name'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter email'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Confirm password'
        })

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['name'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter email'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter username'
        })

        self.fields['location'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter location'
        })

        # Set the Textarea widget for the description field and adjust its attributes
        self.fields['bio'].widget = Textarea(attrs={
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter description',
            'rows': 3  # Number of visible rows
        })

        self.fields['profile_image'].widget = ClearableFileInput(attrs={
                'class': 'w-full bg-[#F5F5F5] p-3',
                'placeholder': 'Upload profile image',
        })