from django.contrib import admin
from .models import Human

class HumanAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'dob', 'address']

admin.site.register(Human, HumanAdmin)