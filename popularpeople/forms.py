from django import forms
from .models import Category, Partner

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label="Content", required=False)
    is_published = forms.BooleanField(required=False, label="Status")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Category not chosen", initial=True,  label="Category")
    partner = forms.ModelChoiceField(queryset=Partner.objects.all(), label="Partner",empty_label="Unmarried", required=False)

