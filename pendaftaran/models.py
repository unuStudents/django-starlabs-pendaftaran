import email
from django.db import models

# Create your models here.
class User(models.Model):
    PRODI       = (
        ('SI', 'Sistem Informasi'),
        ('TI', 'Teknik Informatika'),
        ('MTK', 'Matematika'),
        ('MNJ', 'Manajemen'),
        ('EP', 'Ekonomi Pembangunan'),
        ('PGSD', 'Pendidikan Guru Sekolah Dasar'),
    )
    nama        = models.CharField(max_length=100,)
    prodi       = models.CharField(max_length=5, choices=PRODI, default='Sistem Informasi')
    nim         = models.BigIntegerField(unique=True)
    # nim         = models.CharField(unique=True, max_length=15)
    email_aktif = models.EmailField(max_length=40, unique=True, null=False)
    tgl_lahir   = models.DateField(null=False)

    def __str__(self):
        # return self.nama
        return '{}.{}'.format(self.nama, self.nim)

    # def isEksis(self):
    #     if User.objects.filter(email_aktif = self.context['request'].email_aktif).exists():
    #         return True
    #     return False