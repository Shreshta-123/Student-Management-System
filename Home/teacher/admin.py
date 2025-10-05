# Register your models here.
from django.contrib import admin
from .models import Parent, Teacher

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teacher_id', 'gender', 'date_of_birth', 'joining_date', 'mobile_number', 'admission_number', 'section')
    search_fields = ('first_name', 'last_name', 'teacher_id', 'admission_number')
    list_filter = ('gender','teacher_class', 'section')
    readonly_fields = ('teacher_image',)  # Optional: makes the image field read-only
