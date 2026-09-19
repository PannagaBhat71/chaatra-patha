"""
URL configuration for mysite project.
"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from students import views
from accounts import views as account_views


def serve_static(request, path, **kwargs):
    """
    Robust static file serving for serverless deployments (Vercel).
    Checks collected staticfiles first, falls back directly to students/static.
    """
    static_file = os.path.join(settings.STATIC_ROOT, path)
    if os.path.exists(static_file):
        return serve(request, path, document_root=settings.STATIC_ROOT)
    students_static = os.path.join(settings.BASE_DIR, 'students', 'static')
    alt_file = os.path.join(students_static, path)
    if os.path.exists(alt_file):
        return serve(request, path, document_root=students_static)
    return serve(request, path, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home_alias'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('student/', views.add_student, name='student-list'),
    path('student/add/', views.add_student, name='add-student'),
    path('roadmap/<int:student_id>/', views.student_roadmap, name='student-roadmap'),
    path('roadmap/', views.roadmap_preview, name='roadmap'),
    path('accounts/', include('accounts.urls')),
    path('login/', account_views.user_login, name='login'),
    path('signup/', account_views.signup, name='signup'),
    path('logout/', account_views.user_logout, name='logout'),
    path('api/chat/', views.chatbot_api, name='chatbot-api'),
    re_path(r'^static/(?P<path>.*)$', serve_static),
]
