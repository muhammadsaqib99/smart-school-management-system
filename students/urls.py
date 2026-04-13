from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-class/', views.add_class, name='add_class'),
    path('add-section/', views.add_section, name='add_section'),
    path('class-list/', views.class_list, name='class_list'),
    path('delete-class/<int:id>/', views.delete_class, name='delete_class'),
    path('edit-class/<int:id>/', views.edit_class, name='edit_class'),
    path('section-list/', views.section_list, name='section_list'),
    path('delete-section/<int:id>/', views.delete_section, name='delete_section'),
    path('edit-section/<int:id>/', views.edit_section, name='edit_section'),
    path('add-student/', views.add_student, name='add_student'),
    path('student-list/', views.student_list, name='student_list'),
    path('ajax/load-sections/', views.load_sections, name='ajax_load_sections'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('teacher-list/', views.teacher_list, name='teacher_list'),
    path('delete-teacher/<int:id>/', views.delete_teacher, name='delete_teacher'),
    path('edit-teacher/<int:id>/', views.edit_teacher, name='edit_teacher'),   
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'), 
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('bulk-upload/', views.bulk_upload_students, name='bulk_upload_students'),
    path('profile/', views.profile_view, name='profile'),
    
]