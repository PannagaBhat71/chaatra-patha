from django import forms
from .models import student


class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['roll_number', 'student_name', 'skills', 'age']
        labels = {
            'roll_number': 'Roll Number',
            'student_name': 'Full Name',
            'skills': 'Skills / Areas of Interest',
            'age': 'Age',
        }
        widgets = {
            'roll_number': forms.NumberInput(attrs={
                'class': 'neu-input',
                'placeholder': 'e.g. 101',
                'min': '1',
            }),
            'student_name': forms.TextInput(attrs={
                'class': 'neu-input',
                'placeholder': 'Enter student name',
            }),
            'skills': forms.TextInput(attrs={
                'class': 'neu-input',
                'placeholder': 'e.g. Python, Django, Machine Learning',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'neu-input',
                'placeholder': 'e.g. 21',
                'min': '1',
                'max': '120',
            }),
        }

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')
        if not skills or not skills.strip():
            raise forms.ValidationError("Skills must be mentioned.")
        return skills.strip()
