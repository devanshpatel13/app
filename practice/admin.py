from django.contrib import admin
from .models import home
# Register your models here.


@admin.register(home)
class homeadmin(admin.ModelAdmin):
    list_display = ['name','number','email','start_date','end_date']