# Generated by Django 2.2.3 on 2019-07-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='photo',
            field=models.ImageField(upload_to='Photos/'),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='resume',
            field=models.FileField(upload_to='Resume/'),
        ),
    ]