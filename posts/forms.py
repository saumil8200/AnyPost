from django.forms import ModelForm, Textarea, ClearableFileInput
from django import forms
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'featured_image',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['category'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
        })
        self.fields['title'].widget.attrs.update({
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter title'
        })
        # Set the Textarea widget for the description field and adjust its attributes
        self.fields['description'].widget = Textarea(attrs={
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': 'Enter description',
            'rows': 15  # Number of visible rows
        })

        self.fields['featured_image'].widget = ClearableFileInput(attrs={
                'class': 'w-full bg-[#F5F5F5] p-3',
                'placeholder': 'Upload profile image',
        })

        # Set a default placeholder or initial value for the category field
        self.fields['category'].empty_label = 'Select postgroup'

class CommentForm(forms.ModelForm):
    parent_id = forms.UUIDField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3})}

    def clean_parent_id(self):
        parent_id = self.cleaned_data.get('parent_id')
        if parent_id:
            try:
                parent_comment = Comment.objects.get(id=parent_id)
                if parent_comment:
                    return parent_comment.id
            except Comment.DoesNotExist:
                raise forms.ValidationError("Invalid parent comment ID.")
        return None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields

        self.fields['content'].widget = Textarea(attrs={
            'class': 'w-full bg-[#F5F5F5] p-3',
            'placeholder': '',
            'rows': 2  # Number of visible rows
        })