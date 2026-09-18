from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, request



# Create your views here.
class HomeView(TemplateView):
    template_name = "students/home.html"


class AboutView(TemplateView):
    template_name = "students/about.html"


class ContactView(TemplateView):
    template_name = "students/contact.html"
