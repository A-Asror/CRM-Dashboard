# Generated by Django 3.2.5 on 2021-08-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0014_auto_20210804_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='photo',
            new_name='image',
        ),
    ]
