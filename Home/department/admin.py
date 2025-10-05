# Register your models here.
from django.contrib import admin
from .models import  Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_id', 'mobile_number')
    search_fields = ('department_name', 'department_id')
    list_filter = ('department_hod',)