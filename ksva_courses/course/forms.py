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
        fields = ['name', 'email', 'phone_number', 'address', 'date_of_birth', 'gender', 'education_level','course','additional_info']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'education_level': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise ValidationError('Enter a valid phone number (up to 15 digits).')
        return phone_number