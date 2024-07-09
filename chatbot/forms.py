from django import forms

class ChatForm(forms.Form):
    message=forms.CharField(label='Ask anything', max_length=100)