from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Instructor, Category, StudentInfo
from .forms import StudentInfoForm, CourseForm, InstructorForm, CategoryForm

def home(request):
    context = {
        'courses': Course.objects.all(),
        'instructors': Instructor.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def courses(request):
    context = {
        'courses': Course.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'pages/courses.html', context)

def team(request):
    return render(request, 'pages/team.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def error_404(request):
    return render(request, 'pages/404.html')

def contact(request):
    return render(request, 'pages/contact.html')

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course/course_detail.html', {'course': course})

def enroll(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enroll_success')
    else:
        form = StudentInfoForm()
    return render(request, 'pages/enroll.html', {'form': form})

def enroll_success(request):
    return render(request, 'pages/enroll_success.html')