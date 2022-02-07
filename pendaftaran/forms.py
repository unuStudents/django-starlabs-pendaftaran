from django.forms import ModelForm
from django import forms
from .models import User

class FormPendaftaran(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        PRODI       = (
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Matematika', 'Matematika'),
        ('Manaajemen', 'Manajemen'),
        ('Ekonomi Pembangunan', 'Ekonomi Pembangunan'),
        ('Pendidikan Guru Sekolah Dasar', 'Pendidikan Guru Sekolah Dasar'),
    )

        widgets = {
            'nama'          : forms.TextInput({'PlaceHolder':'Masukan Nama Lengkap', 'autocomplete': 'off'}),
            'prodi'         : forms.Select(choices=PRODI,  attrs={'class':'selek', 'autocomplete': 'off'}),
            'nim'           : forms.TextInput({'PlaceHolder':'Masukan NIM mu', 'autocomplete': 'off'}),
            'email_aktif'   : forms.EmailInput({'PlaceHolder':'Email Aktif', 'autocomplete': 'off'}),
            'tgl_lahir'     : forms.DateInput({'type':'date', 'required':'true', 'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama'].label   = 'Nama Lengkap'
        self.fields['prodi'].label = 'Program Studi'
        self.fields['nim'].label = 'NIM'
        self.fields['email_aktif'].label = 'Email Aktif'
        self.fields['tgl_lahir'].label = 'Tanggal Lahir'
