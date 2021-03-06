# Generated by Django 4.0.3 on 2022-04-18 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_Key', models.CharField(default='STUD', max_length=10)),
                ('student_name', models.CharField(max_length=30)),
                ('student_gender', models.CharField(max_length=30)),
                ('student_dob', models.CharField(max_length=30)),
                ('student_address', models.CharField(max_length=200)),
                ('student_phone', models.CharField(max_length=30)),
                ('student_admissionyear', models.CharField(max_length=30)),
                ('student_admissionnumber', models.CharField(max_length=30)),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.courses')),
                ('student_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('student_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_Key', models.CharField(default='FAC', max_length=30)),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_gender', models.CharField(max_length=30)),
                ('staff_dob', models.CharField(max_length=30)),
                ('staff_address', models.CharField(max_length=200)),
                ('staff_phone', models.CharField(max_length=30)),
                ('staff_yearofjoin', models.CharField(max_length=30)),
                ('staff_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('staff_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.posts')),
                ('staff_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='quesadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesadmin_Key', models.CharField(default='QAD', max_length=30)),
                ('quesadmin_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('quesadmin_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
    ]
