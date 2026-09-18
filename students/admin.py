from django.contrib import admin
from .models import student  # Import your model from models.py

# Register the model
admin.site.register(student)
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'student_name', 'age', 'date_created')
    search_fields = ('roll_number', 'student_name')
    ordering = ('-date_created',)