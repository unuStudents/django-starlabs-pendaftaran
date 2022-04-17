import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    PRODI = (
        ("FMIKOM|SI", "Sistem Informasi"),
        ("FMIKOM|TI", "Teknik Informatika"),
        ("FMIKOM|MAT", "Matematika"),
        ("FE|MAN", "Manajemen"),
        ("FE|EP", "Ekonomi Pembangunan"),
        ("FKIP|PGSD", "Pendidikan Guru Sekolah Dasar"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=100, blank=False)
    prodi = models.CharField(max_length=35, choices=PRODI, default="FMIKOM|SI")
    nim = models.CharField(unique=True, max_length=12, blank=False)
    email_aktif = models.EmailField(max_length=40, unique=True, null=False, blank=False)
    no_wa = models.CharField(max_length=15, blank=False, null=False)
    tgl_lahir = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.nama
        return "{}.{}".format(self.nama, self.nim)

    # def isEksis(self):
    #     if User.objects.filter(email_aktif = self.context['request'].email_aktif).exists():
    #         return True
    #     return False
