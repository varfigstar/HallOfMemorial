from django.contrib import admin

from .models import Person, ImageURL


admin.site.register(ImageURL)
admin.site.register(Person)

