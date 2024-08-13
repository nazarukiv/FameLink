from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

from .models import Category, Partner, People


class AddPostForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'partner', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'title': "Title",
            'slug': "URL",
            'content': "Content",
            'is_published': "Status",
            'cat': "Category",
            'partner': "Partner",
            'photo': "Photo",
        }
        error_messages = {
            'title': {
                'min_length': "At least 5 symbols",
                'required': "Required**",
            },
        }
    slug = forms.SlugField(
        max_length=255,
        validators=[MinLengthValidator(5), MaxLengthValidator(100)],
        label="URL"
    )
    photo = forms.ImageField(
        required=False,
        label="Photo"
    )



class UploadFileForm(forms.Form):
    file = forms.FileField(label="File")