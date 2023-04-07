from django.shortcuts import render
from .models import Raffle

def raffle_list(request):
    raffles = Raffle.objects.all()
    return render(request, 'raffle_list.html', {'raffles': raffles})

def raffle_detail(request, raffle_id):
    raffle = Raffle.objects.get(pk=raffle_id)
    return render(request, 'raffle_detail.html', {'raffle': raffle})
