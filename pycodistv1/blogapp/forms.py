from django import forms
from django.contrib.auth.models import User

class NewArticle(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.IntegerField()

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     print(f"ID : {self.request.user.id}")

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     if self.request and self.request.user.is_authenticated:
    #         user_id = self.request.user.id
    #     self.author = user_id

    #     print(f"AUTHOR : {self.author}")

    #     super(NewArticle, self).__init__(*args, **kwargs)

    
    # def clean(self):
    #     cleaned_data = super(NewArticle, self).clean()
    #     if self.request and self.request.user.is_authenticated:
    #         user_id = self.request.user.id