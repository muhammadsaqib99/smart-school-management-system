from django import forms
from .models import Class, Section, Student, Teacher



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

        widgets = {
    'name': forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
    }),
}

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'class_obj']

        widgets = {
        'name': forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
        }),

            'class_obj': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-4 py-2  focus:ring-2 focus:ring-blue-500'
            }),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'class_obj': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg'
            }),
            'section': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg'
            }),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'class_obj', 'section']

        widgets = {
          'name': forms.TextInput(attrs={
          'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
        }),

       
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'class_obj': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'section': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
        }

