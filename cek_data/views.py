from django.shortcuts import render
from pendaftaran.models import User
from .forms import FormCari

# Create your views here.
def read(request):
    hasil = User.objects.all()
    context = {
        'data':hasil,
    }
    return render(request, 'cek_data/cek_all_data.html', context)

def cek_data(request):
    form = FormCari(request.POST or None)
    if request.POST:
        cari = request.POST['email_aktif']
        hasil = FormCari()
        hasil = User.objects.filter(email_aktif=cari)
        form = FormCari()
        context = {
            'judul' :'Cek Data Diri',
            'data'  :hasil,
            'form'  :form,
        }
        return render(request, 'cek_data/index.html', context)

    return render(request, 'cek_data/index.html', {'form':form, 'judul' :'Cek Data Diri'})
