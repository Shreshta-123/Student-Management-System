from django.http import HttpResponseForbidden
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def add_department(request):
    if request.method == "POST":
        department_name = request.POST.get('department_name')
        department_id = request.POST.get('department_id')
        department_hod = request.POST.get('department_hod')
        mobile_number = request.POST.get('mobile_number')
        department_email = request.POST.get('department_email')


        # Save student information
        department = Department.objects.create(
            department_name= department_name,
            department_id= department_id,
            department_hod= department_hod,
            mobile_number = mobile_number,
            department_email = department_email
        )
        messages.success(request,"department added successfully")
        #return render(request, "student_list")
   
    return render(request,"departments/add-department.html")


def department_list(request):
    department_list = Department.objects.all()
    context = {
        'department_list': department_list,
    }
    return render(request, "departments/departments.html", context)

def edit_department(request,slug):
    department = get_object_or_404(Department, slug=slug)
    if request.method == "POST":
        department_name = request.POST.get('department_name')     
        department_id = request.POST.get('department_id')
        department_hod = request.POST.get('department_hod')
        mobile_number = request.POST.get('mobile_number')
        department_email = request.POST.get('department_email')  


#  update student information

        department.department_name= department_name
        department.teacher_id= department_id
        department.teacher_hod= department_hod
        department.mobile_number = mobile_number
        department.department_email = department_email
        department.save()

        return redirect("department_list")
    return render(request, "departments/edit-department.html",{'department':department})





