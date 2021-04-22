from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=25)
    to = forms.EmailField(label="Email to which link will be send")
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField(label="Search for")
