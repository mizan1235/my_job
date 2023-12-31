# Generated by Django 4.2.3 on 2023-10-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_remove_employee_cred_id_remove_user_cred_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(default=None, max_length=250, null=True, upload_to='Images/')),
                ('company_name', models.CharField(max_length=100)),
                ('company_title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=40)),
                ('job_id', models.CharField(max_length=70)),
            ],
        ),
    ]
