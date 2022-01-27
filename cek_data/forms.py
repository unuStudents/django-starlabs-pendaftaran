from django import forms
from .models import User

class FormCari(forms.ModelForm):
    class Meta:
        model = User
        fields = {'email_aktif'}

        widgets = {
            'email_aktif' : forms.EmailInput({'PlaceHolder':'Ketik Emailmu disi yah !', 'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_aktif'].label = 'Email Yang Terdaftar'