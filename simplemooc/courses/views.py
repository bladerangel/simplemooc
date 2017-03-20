from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse


# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/index.html', context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()

    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    return render(request, 'courses/details.html', context)
