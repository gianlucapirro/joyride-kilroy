from django.contrib import admin
from .models import Registrant

@admin.register(Registrant)
class RegistrantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'roadtrip', 'email_friend1', 'email_friend2')