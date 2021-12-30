from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Merchandise, MerchandiseImg
from .serializers import CategorySerializer, MerchandiseSerializer, MerchandiseIMGSerializer


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


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class MerchandiseListCreateAPIView(ListCreateAPIView):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()


class MerchandiseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()


class MerchandiseIMGListCreateAPIView(ListCreateAPIView):
    serializer_class = MerchandiseIMGSerializer
    queryset = MerchandiseImg.objects.all()


class MerchandiseIMGRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MerchandiseIMGSerializer
    queryset = MerchandiseImg.objects.all()
