# Generated by Django 4.0.5 on 2022-07-02 13:44

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.image_validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('job_start_date', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('tel1', models.CharField(max_length=200)),
                ('tel2', models.CharField(max_length=200, null=True)),
                ('sv_image', models.ImageField(null=True, upload_to='media/account/%Y/%m/%d/', validators=[main.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('electronic_signature', models.ImageField(null=True, upload_to='media/account/%Y/%m/%d/', validators=[main.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('gender', models.CharField(blank=True, choices=[('Kişi', 'Kişi'), ('Qadın', 'Qadın')], default=None, max_length=150, null=True)),
                ('salary_calculation_style', models.CharField(blank=True, choices=[('SAATLIQ', 'SAATLIQ'), ('HƏFTƏLİK', 'HƏFTƏLİK'), ('AYLIQ', 'AYLIQ')], default='AYLIQ', max_length=150, null=True)),
                ('hourly_salary', models.FloatField(default=0)),
                ('weekly_salary', models.FloatField(default=0)),
                ('monthly_salary', models.FloatField(default=0)),
                ('salary', models.FloatField(blank=True, default=0, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.company')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ishci', to='company.office')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_vezife', to='company.position')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
