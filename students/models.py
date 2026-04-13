from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Class Model for classes
class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Section Model for sections
class Section(models.Model):
    name = models.CharField(max_length=10)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_obj} - {self.name}"
    
 # Student Model for students
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def clean(self):
        if self.section.class_obj != self.class_obj:
            raise ValidationError("Section does not belong to selected class")
    def __str__(self):
        return self.name

    # Teacher Model for teachers


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def clean(self):
        if self.section.class_obj != self.class_obj:
            raise ValidationError("Section does not belong to selected class")

    def __str__(self):
        return self.name
    


class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    student = models.OneToOneField('Student', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE, null=True, blank=True)

