from django.contrib import admin
from .models import Class, Section, Student, Teacher,Profile

admin.site.site_title = "Smart School Admin Panels"
admin.site.site_header = "Smart School Login Page"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']

admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Teacher)

