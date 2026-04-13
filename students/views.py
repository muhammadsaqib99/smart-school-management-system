from django.shortcuts import render, redirect
from .forms import ClassForm, SectionForm, StudentForm,TeacherForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Class, Section, Student, Teacher, Profile
from django.shortcuts import get_object_or_404
from django.http import JsonResponse   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
import csv
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

#Add Class
@login_required
@admin_only
def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class added successfully!")
            return redirect('students:add_class')
    else:
        form = ClassForm()

    return render(request, 'students/add_class.html', {'form': form})

#Add Section
@login_required
@admin_only
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Section added successfully!")
            return redirect('students:add_section')
    else:
        form = SectionForm()

    return render(request, 'students/add_section.html', {'form': form})


# Classes List
@login_required

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'students/class_list.html', {'classes': classes})

#Delete Class
@login_required
@admin_only
def delete_class(request, id):
    cls = get_object_or_404(Class, id=id)
    cls.delete()
    return redirect('students:class_list')

#Edit Class
@login_required
@admin_only
def edit_class(request, id):
    cls = get_object_or_404(Class, id=id)

    if request.method == 'POST':
        form = ClassForm(request.POST, instance=cls)
        if form.is_valid():
            form.save()
            return redirect('students:class_list')
    else:
        form = ClassForm(instance=cls)

    return render(request, 'students/edit_class.html', {'form': form})

#section list
@login_required
def section_list(request):
    sections = Section.objects.select_related('class_obj')
    return render(request, 'students/section_list.html', {'sections': sections})

#Delete Section
@login_required
@admin_only
def delete_section(request, id):
    section = get_object_or_404(Section, id=id)
    section.delete()
    return redirect('students:section_list')

#Edit Section
@login_required
@admin_only
def edit_section(request, id):
    section = get_object_or_404(Section, id=id)

    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('students:section_list')
    else:
        form = SectionForm(instance=section)

    return render(request, 'students/edit_section.html', {'form': form})

#Add Student
@login_required
@admin_only
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})

#Student List
@login_required
def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/student_list.html', {
        'page_obj': page_obj
    })

def load_sections(request):
    class_id = request.GET.get('class_id')
    sections = Section.objects.filter(class_obj_id=class_id)

    data = list(sections.values('id', 'name'))

    return JsonResponse(data, safe=False)

#Delete Student
@login_required
@admin_only
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students:student_list')

#Edit Student
@login_required
@admin_only
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form})

# Add Teacher
@login_required
@admin_only
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:teacher_list')
    else:
        form = TeacherForm()

    return render(request, 'teachers/add_teacher.html', {'form': form})

@login_required
def teacher_list(request):
    teachers = Teacher.objects.select_related('class_obj', 'section')
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

@login_required
@admin_only
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('students:teacher_list')

@login_required
def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('students:teacher_list')
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'teachers/edit_teacher.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_classes = Class.objects.count()

    class_data = Class.objects.annotate(num_students=Count('student'))

    labels = [c.name for c in class_data]
    data = [c.num_students for c in class_data]

    return render(request, 'dashboard.html', {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_classes': total_classes,
        'labels': labels,
        'data': data
    })

# Login 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            
            role = getattr(getattr(user, 'profile', None), 'role', 'student')

            if role == 'admin':
                return redirect('students:dashboard')

            elif role == 'teacher':
                return redirect('students:teacher_dashboard')

            elif role == 'student':
                return redirect('students:student_dashboard')

            else:
                return redirect('students:dashboard')

        else:
            return render(request, 'auth/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'auth/login.html')

# Logout
def user_logout(request):
    logout(request)
    return redirect('students:login')

@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# Teacher Dashboard
def teacher_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return redirect('students:dashboard')

    students = Student.objects.filter(
        class_obj=teacher.class_obj,
        section=teacher.section
    )

    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher,
        'students': students
    })

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return redirect('students:dashboard')

    return render(request, 'student_dashboard.html', {
        'student': student
    })

def bulk_upload_students(request):
    if request.method == "POST":
        file = request.FILES.get('file')

        if not file:
            messages.error(request, "No file selected")
            return redirect('students:bulk_upload_students')

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        created = 0
        skipped = 0

        for row in reader:
            try:
                name = row['name'].strip()
                username = row['username'].strip()
                password = row['password'].strip()
                class_name = row['class'].strip()
                section_name = row['section'].strip()

                # Skip duplicates
                if User.objects.filter(username=username).exists():
                    skipped += 1
                    continue

                
                class_obj = Class.objects.filter(
                    name__icontains=class_name
                ).first()

                if not class_obj:
                    print("CLASS NOT FOUND:", class_name)
                    skipped += 1
                    continue

               
                section = Section.objects.filter(
                    name__iexact=section_name,
                    class_obj=class_obj
                ).first()

                if not section:
                    print("SECTION NOT FOUND:", section_name, class_name)
                    skipped += 1
                    continue

                # Create user
                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                # Create student
                Student.objects.create(
                    user=user,
                    name=name,
                    class_obj=class_obj,
                    section=section
                )

                created += 1

            except Exception as e:
                print("ERROR ROW:", row, e)
                skipped += 1

        messages.success(
            request,
            f"Upload completed → Created: {created}, Skipped: {skipped}"
        )

        return redirect('students:student_list')

    return render(request, 'students/bulk_upload.html')
 
@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student'}
    )

    student = None
    teacher = None

    if profile.role == 'student':
        student = Student.objects.filter(user=request.user).first()

    elif profile.role == 'teacher':
        teacher = Teacher.objects.filter(user=request.user).first()

    context = {
        'profile': profile,
        'student': student,
        'teacher': teacher
    }

    return render(request, 'students/profile.html', context)
