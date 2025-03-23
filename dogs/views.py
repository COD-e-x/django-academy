from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from dogs.models import Breed, Dog
from dogs.forms import DogForm


def index(request):
    """Отображает главную страницу с перечнем первых 3-х пород."""
    context = {
        "objects_list": Breed.objects.all()[:3],
        "title": "Питомник - Главная",
    }
    return render(
        request,
        "dogs/index.html",
        context,
    )


def breeds_list(request):
    """Отображает список всех пород собак."""
    context = {
        "objects_list": Breed.objects.all(),
        "title": "Питомник - Все наши пароды",
    }
    return render(
        request,
        "dogs/breeds.html",
        context,
    )


def breed_dogs_list(request, pk: int):
    """Отображает список собак для конкретной породы."""
    breed_item = Breed.objects.get(pk=pk)
    context = {
        "objects_list": Dog.objects.filter(breed_id=pk),
        "title": f"Собаки пароды - {breed_item.name}",
        "breed_pk": breed_item.pk,
    }
    return render(
        request,
        "dogs/dogs.html",
        context,
    )


def dogs_list(request):
    """Отображает список всех собак в питомнике."""
    context = {
        "object": Dog.objects.all(),
        "title": "Питомник - Все наши собаки",
    }
    return render(
        request,
        "dogs/dogs.html",
        context,
    )


def dog_create(request):
    """
    Обрабатывает создание новой собаки через форму.
    Если форма валидна, сохраняет собаку и перенаправляет на список собак.
    """
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dogs:dogs_list"))
    return render(request, "dogs/create.html", {"form": DogForm()})
