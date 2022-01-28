from django.http import HttpResponseRedirect
from django.shortcuts import  render
from .forms import FormPendaftaran
from .models import User

# Create your views here.
def index(request):
    if request.POST:
        form    = FormPendaftaran(request.POST or None)
        if form.is_valid():
            form.save()
            form = FormPendaftaran()
            konteks = {
                'form'  :form,
            }
            return HttpResponseRedirect('konfirmasi-sukses')
        # else:
        #     form = FormPendaftaran()

    else:
        form = FormPendaftaran()
        konteks = {
            'judul' :'Pendaftaran',
            'form':form,
        }
        return render(request, 'pendaftaran/index.html', konteks)

    return render(request, 'pendaftaran/index.html', {'form':form} )

def konfirmasi(request):
    return render(request, 'pendaftaran/konfirmasi.html', {'judul' :'Thanks say...'})
