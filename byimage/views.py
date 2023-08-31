from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import random


def game(request):
    # Lista todos los objetos
    players = Player.objects.all()
    # Obtiene un numero random y luego busca el jugador en ese indice
    random_number = random.randint(0, len(players) - 1)
    random_player = players[random_number]
    # Suma la cantidad de palabras
    words = len(random_player.name.split(" "))
    # Quita los espacios en blanco, para evitar problemas
    random_player.name = random_player.name.replace(" ", " ")

    return render(request, 'game.html', {
        'player': random_player,
        'words': words
    })


def find_out(request):
    # Obtiene los datos que vienen desde el formulario
    guess_name = request.POST['input_name'].replace(" ", "").lower()
    correct_name = request.POST['input_correct'].replace(" ", "").lower()

    if guess_name == correct_name:
        messages.success(request, 'Correct!!')
    else:
        messages.success(request, f'Wrong!!, it was {request.POST["input_correct"]}')

    # Redirige a la página para seguir jugando
    return redirect('/')