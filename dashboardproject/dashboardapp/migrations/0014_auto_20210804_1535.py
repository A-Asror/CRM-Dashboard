# Generated by Django 3.2.5 on 2021-08-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0013_alter_student_checkout_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mentors/'),
        ),
        migrations.DeleteModel(
            name='Student_checkout',
        ),
    ]
