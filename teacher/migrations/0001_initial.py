# Generated by Django 5.0.3 on 2024-06-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_attendance',
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
            ],
        ),
    ]