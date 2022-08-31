from django.contrib import admin

from .models import Place
from .models import Peoples

# Register your models here.
admin.site.register(Place)
admin.site.register(Peoples)
