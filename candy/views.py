from django.shortcuts import render

from webproject.models import voto

# Create your views here.
def voto_off(request):

    return render(request,'candy/novovoto.html',{})


def voto_on(request,date):
    #Se necessaio salvamos o novo dado!
    if(date == "DC"):
        print("DOCE")
        voto.objects.create(voto="DC")
    elif(date == "SL"):
        print("SALGADO")
        voto.objects.create(voto="SL")
    else:
        print("LIMPO")


    # Primeiro, buscamos os votos
    votos = voto.objects.all()

    # Incluímos no contexto
    contexto = {
        'salgados':voto.objects.filter(voto="SL").count(),
        'doces':voto.objects.filter(voto="DC").count(),
        'total':voto.objects.count()
    }

    return render(request,'candy/velhovoto.html',contexto)