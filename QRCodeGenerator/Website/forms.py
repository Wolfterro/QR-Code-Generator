from django import forms
from django.contrib.auth.models import User

class CreateQRCodeForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                            max_length=50)

    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                                  max_length=100,
                                  required=False)

    message_to_qr = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-mod', 'rows': 10}),
                                    max_length=1500)

    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                           max_length=100,
                           required=False)


class MyAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
        exclude = ['username', ]

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                               max_length=50, disabled=True, required=False)

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                                 max_length=50)

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-mod'}),
                                max_length=50)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-mod'}),
                             max_length=50)
