from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error_404, name='404'),
    path('contact/', views.contact, name='contact'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

