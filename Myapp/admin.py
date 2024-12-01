from django.contrib import admin
from .models import Client, Case, Sitting

# Register your models here.
admin.site.register(Client)
admin.site.register(Case)
admin.site.register(Sitting)
