from django import forms
from .models import student
from .skills_data import SKILLS_LOOKUP, ALL_SKILLS_LIST


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
                'placeholder': 'Enter student full name',
            }),
            'skills': forms.TextInput(attrs={
                'class': 'neu-input',
                'placeholder': 'Type to search approved skills (e.g. Web Development...)',
                'list': 'skills-datalist',
                'autocomplete': 'off',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'neu-input',
                'placeholder': 'e.g. 21',
                'min': '1',
                'max': '120',
            }),
        }

    def clean_skills(self):
        import re
        raw_skills = self.cleaned_data.get('skills')
        if not raw_skills or not raw_skills.strip():
            raise forms.ValidationError("Skills must be mentioned.")

        trimmed = raw_skills.strip()

        # If exact match for single skill
        if trimmed.lower() in SKILLS_LOOKUP:
            return SKILLS_LOOKUP[trimmed.lower()]

        # Split by comma that is NOT inside parentheses
        entered_items = [item.strip() for item in re.split(r',\s*(?![^()]*\))', trimmed) if item.strip()]
        if not entered_items:
            raise forms.ValidationError("Please provide at least one valid skill.")

        validated_skills = []
        invalid_skills = []

        for item in entered_items:
            canonical = SKILLS_LOOKUP.get(item.lower())
            if canonical:
                if canonical not in validated_skills:
                    validated_skills.append(canonical)
            else:
                invalid_skills.append(item)

        if invalid_skills:
            formatted_invalid = ", ".join(f"'{s}'" for s in invalid_skills)
            raise forms.ValidationError(
                f"Unrecognized skill(s): {formatted_invalid}. Please choose only from the approved skills list."
            )

        return ", ".join(validated_skills)

        return ", ".join(validated_skills)
