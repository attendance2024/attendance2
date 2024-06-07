# Generated by Django 5.0.3 on 2024-06-07 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=120)),
                ('sem', models.IntegerField()),
                ('graduation', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='addattendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=20)),
                ('roll_no', models.CharField(max_length=20)),
                ('event', models.CharField(max_length=100)),
                ('date1', models.DateField(blank=True, null=True)),
                ('hours1', models.PositiveIntegerField(default=0)),
                ('date2', models.DateField(blank=True, null=True)),
                ('hours2', models.PositiveIntegerField(default=0)),
                ('date3', models.DateField(blank=True, null=True)),
                ('hours3', models.PositiveIntegerField(default=0)),
                ('date4', models.DateField(blank=True, null=True)),
                ('hours4', models.PositiveIntegerField(default=0)),
                ('date5', models.DateField(blank=True, null=True)),
                ('hours5', models.PositiveIntegerField(default=0)),
                ('date6', models.DateField(blank=True, null=True)),
                ('hours6', models.PositiveIntegerField(default=0)),
                ('date7', models.DateField(blank=True, null=True)),
                ('hours7', models.PositiveIntegerField(default=0)),
                ('date8', models.DateField(blank=True, null=True)),
                ('hours8', models.PositiveIntegerField(default=0)),
                ('date9', models.DateField(blank=True, null=True)),
                ('hours9', models.PositiveIntegerField(default=0)),
                ('date10', models.DateField(blank=True, null=True)),
                ('hours10', models.PositiveIntegerField(default=0)),
                ('student_signature', models.CharField(max_length=100)),
                ('teacher_signature', models.CharField(max_length=100)),
                ('tutor_recommendation', models.CharField(blank=True, max_length=100, null=True)),
                ('hod_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('principal_order', models.CharField(blank=True, max_length=100, null=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=120)),
                ('event_date', models.DateField()),
                ('hour_attended', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
            ],
        ),
        migrations.CreateModel(
            name='hod',
            fields=[
                ('hod_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_ID', models.AutoField(primary_key=True, serialize=False)),
                ('reg_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
                ('program_id', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tutor',
            fields=[
                ('tutor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=10)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
