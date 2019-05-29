from django.forms import ModelForm, Textarea, TextInput, EmailInput, IntegerField
from .models import Comment, URL, Reply
from django.utils.translation import ugettext_lazy


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'highlighted', 'page_url']

        widgets = {
            'author': TextInput(
                attrs={'id': 'input_username', 'placeholder': 'username'}),
            'text': Textarea(attrs={'id': 'message', 'placeholder': 'Add your comments here..'}),
            'highlighted': Textarea(attrs={'id': 'part', 'placeholder': 'Paste here text you want to highlight..'}),
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


class ReplyModelForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'text']

        widgets = {
            'author': TextInput(
                attrs={'id': 'input_username', 'placeholder': 'nickname'}),
            'text': Textarea(attrs={'id': 'message', 'placeholder': 'Leave your reply here..'}),
        }
