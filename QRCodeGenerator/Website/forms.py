from django import forms

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
