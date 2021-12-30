from rest_framework import serializers
from .models import Category, Merchandise, MerchandiseImg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = ["name", "manufacturer", "price", "category"]


class MerchandiseIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchandiseImg
        fields = ["image", "product"]
