# Generated by Django 4.2.3 on 2025-02-19 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='curso',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='calificación',
            new_name='grade',
        ),
    ]
