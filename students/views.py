from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from students.models import student
from .forms import studentform
from .skills_data import SKILLS_DICTIONARY, ALL_SKILLS_LIST
from .course_roadmap import get_roadmap_for_skill, parse_student_skills


def add_student(request):
    """
    Renders the student registration form and processes submission.
    Upon successful submission, redirects directly to the personalized course roadmap.
    Does not display other users' records.
    """
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            new_student = form.save()
            return redirect("student-roadmap", student_id=new_student.id)
    else:
        form = studentform()

    return render(request, "students/student.html", {
        "form": form,
        "skills_dictionary": SKILLS_DICTIONARY,
        "all_skills": ALL_SKILLS_LIST,
    })


def student_roadmap(request, student_id):
    """
    Displays the interactive course roadmap for the student's selected skills,
    complete with milestone checkboxes, animated green progress connectors,
    and multi-language YouTube tutorial resources.
    """
    student_obj = get_object_or_404(student, id=student_id)
    skills_list = parse_student_skills(student_obj.skills)

    if not skills_list:
        skills_list = ["Machine Learning Algorithms"]

    roadmaps = [get_roadmap_for_skill(s) for s in skills_list]

    # Handle skill selection tab if multiple skills are present
    selected_slug = request.GET.get('skill')
    active_roadmap = roadmaps[0]
    if selected_slug:
        for rm in roadmaps:
            if rm['slug'] == selected_slug:
                active_roadmap = rm
                break

    return render(request, "students/roadmap.html", {
        "student": student_obj,
        "roadmaps": roadmaps,
        "active_roadmap": active_roadmap,
        "skills_count": len(roadmaps),
    })


def roadmap_preview(request):
    """
    Fallback view for /roadmap/ direct visits.
    Shows the roadmap for the most recent student, or a demo student.
    """
    latest_student = student.objects.order_by('-date_created').first()
    if latest_student:
        return redirect("student-roadmap", student_id=latest_student.id)

    # Demo fallback
    demo_student = {
        "id": 0,
        "student_name": "Preview Scholar",
        "roll_number": 101,
        "skills": "Machine Learning Algorithms",
        "age": 21,
    }
    roadmaps = [get_roadmap_for_skill("Machine Learning Algorithms")]
    return render(request, "students/roadmap.html", {
        "student": demo_student,
        "roadmaps": roadmaps,
        "active_roadmap": roadmaps[0],
        "skills_count": 1,
    })


class HomeView(TemplateView):
    template_name = "students/home.html"


class AboutView(TemplateView):
    template_name = "students/about.html"


class ContactView(TemplateView):
    template_name = "students/contact.html"


class studentView(TemplateView):
    template_name = "students/student.html"