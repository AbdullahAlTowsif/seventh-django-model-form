from django.shortcuts import render
from first_app.forms import StudentForm
from . models import Teacher, Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})

def showData(request):
    # students list for one teacher
    teacher = Teacher.objects.get(name = 'Towsif')
    students = teacher.student.all() # here student is the Student
    for stud in students:
        print(stud.name)
    # teachers list for one studnet
    student = Student.objects.get(name = 'rahim')
    # without using realated_name
    # teachers = student.teacher_set.all() # here teacher_set is the Teacher
    # using realated_name
    teachers = student.teacherss.all() # here teacherss is the related name
    for teacher  in teachers:
        print(teacher.name)
    return render(request, 'show_data.html')