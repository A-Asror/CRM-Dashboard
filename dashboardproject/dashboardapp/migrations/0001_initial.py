# Generated by Django 3.1.7 on 2021-06-14 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spes', models.CharField(choices=[('HTML', 'HTML'), ('JS', 'JS'), ('PYTHON', 'PYTHON'), ('REACT', 'REACT'), ('DJANGO', 'DJANGO')], default='HTML', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=90)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('spes', models.CharField(choices=[('FRONTEND', 'FRONTEND'), ('BACKEND', 'BACKEND')], default='SPES_CHOICE', max_length=9)),
                ('photo', models.ImageField(upload_to='mentors/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=90)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboardapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('time', models.CharField(choices=[('11:00-12:30', '11:00-12:30'), ('14:00-15:30', '14:00-15:30'), ('16:00-17:30', '16:00-17:30'), ('18:30-20:00', '18:30-20:00')], default='11:00-12:30', max_length=13)),
                ('room', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('COWORKING', 'COWORKING')], default='FIRST', max_length=12)),
                ('student_qty', models.PositiveIntegerField()),
                ('theme', models.CharField(max_length=90)),
                ('status', models.CharField(choices=[('PLANNED', 'PLANNED'), ('DONE', 'DONE'), ('CANCEL', 'CANCEL')], default='PLANNED', max_length=8)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboardapp.course')),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboardapp.mentor')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboardapp.mentor'),
        ),
    ]