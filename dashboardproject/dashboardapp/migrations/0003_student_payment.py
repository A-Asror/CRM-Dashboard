# Generated by Django 3.2.1 on 2021-06-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0002_auto_20210614_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='payment',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='NO', max_length=4),
        ),
    ]