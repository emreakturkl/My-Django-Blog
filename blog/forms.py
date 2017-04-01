from django import forms
from .models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'id'   : 'inputdefault',
            })
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'comment','captcha')    


