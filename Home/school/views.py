from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def dashboard(request):
    #unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    #unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html")