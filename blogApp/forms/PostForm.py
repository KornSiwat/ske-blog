import sys

from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_tagify.fields import TagsField

from blogApp.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        min_length=1,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'id': 'title-field',
                'placeholder': 'Title'
            }
        ),
        label=''
    )

    slug = forms.CharField(
        min_length=1,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'input-field',
                'id': 'slug-field',
                'placeholder': 'Slug',
            }
        ),
        label=''
    )

    tags = TagsField(max_length=1000)

    public = forms.BooleanField(label='Publish Now', required=False)

    content = forms.CharField(
        required=False, widget=CKEditorUploadingWidget(), label='')

    class Meta:
        model = Post
        fields = ['public', 'thumbnail', 'title', 'slug', 'tags', 'content']


sys.modules[__name__] = PostForm
