from django import forms




class ContactForm(forms.Form):
    name = forms.CharField(label='name',max_length=100)
    email= forms.EmailField(label='email')
    website = forms.URLField(label='website')
    message = forms.CharField(label='message',widget=forms.Textarea)
