from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# USERS DATABSE MODELS STARTS HERE

class students(models.Model):
    student_Key = models.CharField(max_length=10,default='STUD')
    student_username = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    student_gender = models.CharField(max_length=30)
    student_dob = models.CharField(max_length=30)
    student_address = models.CharField(max_length=200)
    student_phone =models.CharField(max_length=30)
    student_admissionyear = models.CharField(max_length=30)
    student_admissionnumber = models.CharField(max_length=30)
    student_course = models.CharField(max_length=30)
    student_department = models.CharField(max_length=30)
    def __str__(self):
        return self.student_admissionnumber

class staffs(models.Model):
    staff_Key = models.CharField(max_length=30,default='FAC')
    staff_username = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=30)
    staff_gender = models.CharField(max_length=30)
    staff_dob = models.CharField(max_length=30)
    staff_address = models.CharField(max_length=200)
    staff_phone =models.CharField(max_length=30)
    staff_yearofjoin = models.CharField(max_length=30)
    staff_department = models.CharField(max_length=30)
    staff_post = models.CharField(max_length=30)
    def __str__(self):
        return self.staff_name

class quesadmin(models.Model):
    quesadmin_Key = models.CharField(max_length=30,default='QAD')
    quesadmin_username = models.ForeignKey(User, on_delete=models.CASCADE)
    quesadmin_department = models.CharField(max_length=30)
    def __str__(self):
        return self.quesadmin_department


# USERS DATABSE MODELS ENDS HERE

# USERS DETAILS MODELS STARTS HERE

class posts(models.Model):
    post = models.CharField(max_length=100)
    def __str__(self):
        return self.post

# class courses(models.Model):
#     course = models.CharField(max_length=100)
#     def __str__(self):
#         return self.course

class department(models.Model):
    department = models.CharField(max_length=30)
    def __str__(self):
        return self.department


class subject(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.subject

# class department(models.Model):
#     department_name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.department_name

# USERS DETAILS MODELS ENDS HERE