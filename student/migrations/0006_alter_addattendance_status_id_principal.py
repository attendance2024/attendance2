# Generated by Django 5.0.3 on 2024-06-13 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_addattendance_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addattendance',
            name='status_id',
            field=models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('ap_by_teacher', 'ap_by_teacher'), ('ap_by_tutor', 'ap_by_tutor'), ('ap_by_hod', 'ap_by_hod'), ('ap_by_princi', 'ap_by_princi'), ('ap_by_tutor_2', 'ap_by_tutor_2')], default='pending', max_length=15),
        ),
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
        ),
    ]
