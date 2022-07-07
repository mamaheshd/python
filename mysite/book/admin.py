from django.contrib import admin
from .models import Laptops, book

# Register your models here.
admin.site.register(book)
admin.site.register(Laptops)