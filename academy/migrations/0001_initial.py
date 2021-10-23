# Generated by Django 3.2.6 on 2021-10-11 14:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=30, verbose_name='Foydalanuvchi ismi:')),
                ('lastname', models.CharField(max_length=40, verbose_name='Foydalanuvchi familiyasi:')),
                ('age', models.IntegerField(verbose_name='Yoshi:')),
                ('phone', models.IntegerField(verbose_name='Telefon raqam:')),
                ('image', models.ImageField(upload_to='users/')),
                ('email', models.EmailField(max_length=40, null=True, verbose_name='email.com')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
            },
        ),
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category/')),
                ('description', models.TextField(default='Description')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': "Kategoriyalar ro'yxati",
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 10, 11, 19, 8, 35, 610802), verbose_name='Registratsiya sanasi:')),
                ('lesson_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='static/media/lessons')),
                ('accsess', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=30, verbose_name='Viloyat nomi:')),
            ],
            options={
                'verbose_name': 'Viloyat nomi',
                'verbose_name_plural': 'Viloyatlar nomi',
            },
        ),
        migrations.CreateModel(
            name='Skill_names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_format', models.BooleanField(default=False, verbose_name='kurs holati active yoki disabled')),
                ('skill_type', models.BooleanField(default=False, verbose_name='kurs offline yoki online ligi')),
                ('skill_name', models.CharField(max_length=70, verbose_name='Kurs nomi')),
                ('description', models.TextField(default='description', verbose_name='www')),
                ('course_start_date', models.DateField(default=datetime.date.today, verbose_name='Kurs boshlanish sanasi')),
                ('course_finish_date', models.DateField(default=datetime.date.today, verbose_name='Kurs tugash sanasi')),
                ('course_duration', models.IntegerField(verbose_name='Kursni davomiyligi oyda')),
                ('skill_image', models.ImageField(upload_to='skills/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.categoriesmodel')),
            ],
            options={
                'verbose_name': 'Kurs nomi',
                'verbose_name_plural': 'Kurs nomlari',
            },
        ),
        migrations.CreateModel(
            name='TeachersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='teachers/')),
                ('description', models.TextField()),
                ('start', models.IntegerField(default=0)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.skill_names')),
            ],
            options={
                'verbose_name': "O'qituvchi",
                'verbose_name_plural': "O'qituvchilar ro'yxati",
            },
        ),
        migrations.CreateModel(
            name='LinkasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=100)),
                ('task', models.TextField()),
                ('trainData', models.TextField()),
                ('script', models.CharField(max_length=200)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.lessons')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.academyusers')),
            ],
            options={
                'verbose_name': 'Havola',
                'verbose_name_plural': "HAvolalar ro'yxati",
            },
        ),
        migrations.AddField(
            model_name='lessons',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.teachersmodel', verbose_name="O'qituvchi"),
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=30, verbose_name='Tuman nomi:')),
                ('region', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.regions')),
            ],
            options={
                'verbose_name': 'Tuman nomi',
                'verbose_name_plural': 'Tumanlar nomi',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('data', models.DateTimeField(verbose_name='Sanasi va vaqti:')),
                ('skill_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.skill_names', verbose_name='Kurslarimiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.academyusers', verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Izoh',
                'verbose_name_plural': 'Izohlar',
            },
        ),
        migrations.AddField(
            model_name='academyusers',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.regions', verbose_name='Viloyatni tanlang:'),
        ),
    ]
