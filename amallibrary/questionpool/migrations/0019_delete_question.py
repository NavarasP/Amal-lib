# Generated by Django 4.0.3 on 2022-04-16 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionpool', '0018_alter_question_question_answer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='question',
        ),
    ]