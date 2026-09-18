from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from students.models import student
from .forms import studentform


# Create your views here.

def add_student(request):
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-list")
    else:
        form = studentform()

    students_list = student.objects.all().order_by('-date_created')
    return render(request, "students/student.html", {
        "form": form,
        "students": students_list
    })


class HomeView(TemplateView):
    template_name = "students/home.html"


class AboutView(TemplateView):
    template_name = "students/about.html"


class ContactView(TemplateView):
    template_name = "students/contact.html"


class studentView(TemplateView):
    template_name = "students/student.html"