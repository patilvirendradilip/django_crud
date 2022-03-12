from django.contrib import admin
from .models import StudentModel
# Register your models here.


class AdminStudentModel(admin.ModelAdmin):
    list = ['id', 'name', 'email', 'mobile', 'dob', 'gender']


admin.site.register(StudentModel, AdminStudentModel)

