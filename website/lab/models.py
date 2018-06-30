from djongo import models


class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {} {} {}'.format(str(self.student_id), self.last_name, self.first_name, self.middle_name)


class Teacher(models.Model):
    teacher_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)


class Science_Group(models.Model):
    group_id = models.IntegerField(unique=True)
    group_purpose = models.CharField(max_length=300)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return 'Науч. группа №{}, руководитель - {}, назначение - {}'.format(str(self.group_id), self.teacher, self.group_purpose)