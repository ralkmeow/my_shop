from django.shortcuts import render
from .models import Category, Merchandise, MerchandiseImg


def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})


def merchandises(request, category_id):
    category = Category.objects.get(id=category_id)
    merchandises = Merchandise.objects.filter(category=category)
    return render(request, "merchandises.html", {"category": category, "merchandises": merchandises})


def merchandise(request, category_id, merchandise_id):
    merchandise = Merchandise.objects.get(id=merchandise_id)
    pictures = MerchandiseImg.objects.filter(product=merchandise_id)
    return render(request, "merchandise.html", {"merchandise": merchandise, "pictures": pictures})
