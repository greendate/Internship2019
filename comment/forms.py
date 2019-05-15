from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import Comment, URL
from django.utils.translation import ugettext_lazy


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'page_url']

        widgets = {
            'author': TextInput(
                attrs={'id': 'input_username', 'placeholder': 'username'}),
            'text': Textarea(attrs={'id': 'message', 'placeholder': 'Add your comments here..'}),
            'page_url': TextInput(
                attrs={'id': 'input_url', 'placeholder': 'New URL goes here..'}),
        }


class URLModelForm(ModelForm):
    class Meta:
        model = URL
        fields = ['site_url']

        widgets = {
            'site_url': TextInput(
                attrs={'id': 'requested_url', 'placeholder': 'Enter the URL of site..'}),
        }
