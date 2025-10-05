from django.http import HttpResponseForbidden
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        teacher_class = request.POST.get('teacher_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        teacher_image = request.FILES.get('teacher_image')

        # Retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save parent information
        parent = Parent.objects.create(
            father_name= father_name,
            father_occupation= father_occupation,
            father_mobile= father_mobile,
            father_email= father_email,
            mother_name= mother_name,
            mother_occupation= mother_occupation,
            mother_mobile= mother_mobile,
            mother_email= mother_email,
            present_address= present_address,
            permanent_address= permanent_address
        )

        # Save student information
        teacher = Teacher.objects.create(
            first_name= first_name,
            last_name= last_name,
            teacher_id= teacher_id,
            gender= gender,
            date_of_birth= date_of_birth,
            teacher_class= teacher_class,
            religion= religion,
            joining_date= joining_date,
            mobile_number = mobile_number,
            admission_number = admission_number,
            section = section,
            teacher_image = teacher_image,
            parent = parent
        )
        messages.success(request,"teacher added successfully")
        #return render(request, "student_list")
   
    return render(request,"teachers/add-teacher.html")


def teacher_list(request):
    teacher_list = Teacher.objects.select_related('parent').all()
    context = {
        'teacher_list': teacher_list,
    }
    return render(request, "teachers/teachers.html", context)

def edit_teacher(request,slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    parent = teacher.parent if hasattr(teacher, 'parent') else None
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        teacher_class = request.POST.get('teacher_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        teacher_image = request.FILES.get('teacher_image')  if request.FILES.get('teacher_image') else teacher.teacher_image

        # Retrieve parent data from the form
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()

#  update student information

        teacher.first_name= first_name
        teacher.last_name= last_name
        teacher.teacher_id= teacher_id
        teacher.gender= gender
        teacher.date_of_birth= date_of_birth
        teacher.teacher_class= teacher_class
        teacher.religion= religion
        teacher.joining_date= joining_date
        teacher.mobile_number = mobile_number
        teacher.admission_number = admission_number
        teacher.section = section
        teacher.teacher_image = teacher_image
        teacher.save()

        return redirect("teacher_list")
    return render(request, "teachers/edit-teacher.html",{'teacher':teacher, 'parent':parent})

def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, teacher_id = slug)
    context = {
        'teacher': teacher
    }
    return render(request,"teachers/teacher-details.html", context)

def delete_teacher(request,slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.delete()

        return redirect ('teacher_list')
    return HttpResponseForbidden()
