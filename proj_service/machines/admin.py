from django.contrib import admin
from .models import Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('m_name', 'machine_type', 'status')
    search_fields = ('m_name',)  # обязательно для autocomplete_fields