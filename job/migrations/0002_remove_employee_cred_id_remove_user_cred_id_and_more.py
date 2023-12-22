# Generated by Django 4.2.3 on 2023-10-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_cred',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user_cred',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee_cred',
            name='username',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_cred',
            name='username',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
