from django.urls import path
from . import views

urlpatterns = [
    ### Операции со студентами
    path('student/add/', views.student_add, name='student-add'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student-delete'),
    path('student/<int:student_id>/edit/', views.student_edit, name='student-edit'),

    ### Операции с преподавателями
    path('teacher/add/', views.teacher_add, name='teacher-add'),
    path('teacher/edit/<int:teacher_id>', views.teacher_edit, name='teacher-edit'),
    path('teacher/<int:teacher_id>/delete/', views.teacher_delete, name='teacher-delete'),

    ### Операции с группами
    path('groups/create/', views.group_create, name='group-create'),
    path('group/<int:group_id>/edit/', views.group_edit, name='group-edit'),
    path('group/<int:group_id>/delete/', views.group_delete, name='group-delete'),

    ### Просмотр информации о научной группе и входящих в нее студентов
    path('group/<int:group_id>/', views.group_details, name='group-details'),

    ### Просмотр списка студентов/преподавателей/научных групп
    path('groups/', views.science_groups, name='groups'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),

    ### Главная страница
    path('', views.index, name='index'),
]