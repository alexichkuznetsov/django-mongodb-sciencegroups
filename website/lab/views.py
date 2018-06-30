from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Student, Teacher, Science_Group
from .forms import StudentForm, TeacherForm, ScienceGroupForm

# Главная страница
def index(request):
    template = loader.get_template('lab/index.html')
    return HttpResponse(template.render())

### Операции со студентами
def students(request):
    students = Student.objects.order_by('student_id')
    template = loader.get_template('lab/students.html')

    return HttpResponse(template.render({'students': students}, request))


def student_add(request):
    template = 'lab/student_form.html'

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentForm()

    return render(request, template, {
        'form': form
    })


def student_edit(request, student_id):
    template = 'lab/student_form.html'

    try:
        student = get_object_or_404(Student, student_id=student_id)

        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                student_id = form.cleaned_data['student_id']
                form.save()
                return HttpResponseRedirect(reverse('students'))
        else:
            form = StudentForm(instance=student)
    except Student.DoesNotExist:
        raise Http404('Такого студента нет в базе данных')

    return render(request, template, {
        'form': form,
        'student': student
    })


def student_delete(request, student_id):
    template = 'lab/student_delete_form.html'

    try:
        student = get_object_or_404(Student, student_id=student_id)

        if request.method == 'POST':
            form = StudentForm(request.POST)
            student.delete()
            return HttpResponseRedirect(reverse('students'))
        else:
            form = StudentForm(instance=student)
    except Student.DoesNotExist:
        raise Http404('Такого студента нет в базе данных')

    return render(request, template, {
        'form': form,
        'student': student
    })


### Операции с преподавателями
def teachers(request):
    teachers = Teacher.objects.order_by('teacher_id')
    template = loader.get_template('lab/teachers.html')

    return HttpResponse(template.render({
        'teachers': teachers
    }, request))

def teacher_add(request):
    template = 'lab/teacher_form.html'

    if request.method == 'POST':
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherForm()

    return render(request, template, {
        'form': form
    })


def teacher_edit(request, teacher_id):
    template = 'lab/teacher_form.html'

    try:
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

        if request.method == 'POST':
            form = TeacherForm(request.POST, instance=teacher)
            if form.is_valid():
                teacher_id = form.cleaned_data['teacher_id']
                form.save()
                return HttpResponseRedirect(reverse('teachers'))
        else:
            form = TeacherForm(instance=teacher)
    except Teacher.DoesNotExist:
        raise Http404('Такого преподавателя нет в базе данных')

    return render(request, template, {
        'form': form,
        'teacher': teacher
    })


def teacher_delete(request, teacher_id):
    template = 'lab/teacher_delete_form.html'

    try:
        teacher = get_object_or_404(Teacher, teacher_id=teacher_id)

        if request.method == 'POST':
            form = TeacherForm(request.POST)
            teacher.delete()
            return HttpResponseRedirect(reverse('teachers'))
        else:
            form = TeacherForm(instance=teacher)
    except Student.DoesNotExist:
        raise Http404('Такого преподавателя нет в базе данных')

    return render(request, template, {
        'form': form,
        'teacher': teacher
    })

### Операции с научными группами
def science_groups(request):
    groups = Science_Group.objects.all()
    template = loader.get_template('lab/groups.html')

    return HttpResponse(template.render({'groups': groups}, request))


def group_details(request, group_id):
    group = Science_Group.objects.get(group_id=group_id)
    students = group.student.all()
    template = loader.get_template('lab/group_details.html')

    return HttpResponse(template.render({
        'group': group,
        'students': students
    }, request))


def group_create(request):
    template = 'lab/group_form.html'

    if request.method == 'POST':
        form = ScienceGroupForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            form.save()
            return HttpResponseRedirect(reverse('group-details', kwargs={
                'group_id': group_id
            }))
    else:
        form = ScienceGroupForm()

    return render(request, template, {
        'form': form
    })


def group_edit(request, group_id):
    template = 'lab/group_form.html'
    group = Science_Group.objects.get(group_id=group_id)

    if request.method == 'POST':
        form = ScienceGroupForm(request.POST, instance=group)

        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            form.save()
            return HttpResponseRedirect(reverse('group-details', kwargs={'group_id': group_id}))
    else:
        form = ScienceGroupForm(instance=group)

    context = {
        'form': form,
        'group': group
    }

    return render(request, template, context)


def group_delete(request, group_id):
    template = 'lab/group_delete_form.html'

    try:
        group = get_object_or_404(Science_Group, group_id=group_id)
        if request.method == 'POST':
            group.delete()
            return HttpResponseRedirect(reverse('groups'))
        else:
            form = ScienceGroupForm(instance=group)
    except Science_Group.DoesNotExist:
        raise Http404('Такой группы не существует')

    context = {
        'form': form,
        'group': group
    }

    return render(request, template, context)