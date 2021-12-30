from django.contrib import admin
from .models import Category, Merchandise, MerchandiseImg

admin.site.register(Category)
admin.site.register(Merchandise)
admin.site.register(MerchandiseImg)
