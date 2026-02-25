from django.shortcuts import render
def dashboard(request):
    # Agar already dashboard function hai, uske niche add karo
    return render(request, 'dashboard.html')  # agar tumhara main dashboard template ye hai

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')