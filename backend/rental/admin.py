from django.contrib import admin

from .models import Belonging, Borrowed


admin.site.register(Belonging)
admin.site.register(Borrowed)
