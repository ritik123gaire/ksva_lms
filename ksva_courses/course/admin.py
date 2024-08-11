from django.contrib import admin
from .models import Category, Instructor, Course, StudentInfo

# Register Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
admin.site.register(Category, CategoryAdmin)

# Register Instructor model
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)
    
admin.site.register(Instructor, InstructorAdmin)

# Register Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'instructor')
    search_fields = ('title', 'category__name', 'instructor__name')
    list_filter = ('category', 'instructor')
    
admin.site.register(Course, CourseAdmin)

# Register StudentInfo model
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course')
    search_fields = ('name', 'email', 'course__title')
    list_filter = ('course', 'gender', 'education_level')
    
admin.site.register(StudentInfo, StudentInfoAdmin)
