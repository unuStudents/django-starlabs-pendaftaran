import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    PRODI       = (
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Matematika', 'Matematika'),
        ('Manaajemen', 'Manajemen'),
        ('Ekonomi Pembangunan', 'Ekonomi Pembangunan'),
        ('Pendidikan Guru Sekolah Dasar', 'Pendidikan Guru Sekolah Dasar'),
    )
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama        = models.CharField(max_length=100,)
    prodi       = models.CharField(max_length=35, choices=PRODI, default='Sistem Informasi')
    nim         = models.BigIntegerField(unique=True)
    email_aktif = models.EmailField(max_length=40, unique=True, null=False)
    tgl_lahir   = models.DateField(null=False)

    def __str__(self):
        # return self.nama
        return '{}.{}'.format(self.nama, self.nim)

    # def isEksis(self):
    #     if User.objects.filter(email_aktif = self.context['request'].email_aktif).exists():
    #         return True
    #     return False