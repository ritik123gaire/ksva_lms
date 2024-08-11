from django import forms
from .models import Course, Instructor, Category, StudentInfo
from django.core.exceptions import ValidationError
import re

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'instructor', 'weeks']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'bio', 'profile_picture']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'email', 'phone_number', 'address', 'date_of_birth', 'gender', 'education_level', 'profile_picture', 'additional_info']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(),
            'education_level': forms.Select(),
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise ValidationError('Enter a valid phone number (up to 15 digits).')
        return phone_number
