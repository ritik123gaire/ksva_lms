from django.db import models
from django.db.models import JSONField
from django.forms import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructor_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, related_name='courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    weeks = JSONField(default=list)

    def __str__(self):
        return self.title


class StudentInfo(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensuring the email is unique
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    education_level = models.CharField(max_length=2, choices=EDUCATION_LEVEL_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'  # Singular name
        verbose_name_plural = 'Students'

    def clean(self):
        super().clean()
        if not self.phone_number.isdigit() or not (10 <= len(self.phone_number) <= 15):
            raise ValidationError('Phone number must be between 10 to 15 digits.')

        # Example: Validate profile picture size and type if needed
        if self.profile_picture:
            if self.profile_picture.size > 5 * 1024 * 1024:  # 5 MB limit
                raise ValidationError('Profile picture size should not exceed 5 MB.')
            if not self.profile_picture.content_type.startswith('image/'):
                raise ValidationError('Only image files are allowed for profile picture.')
