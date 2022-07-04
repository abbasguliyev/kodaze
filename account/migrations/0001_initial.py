# Generated by Django 4.0.5 on 2022-07-04 07:05

from django.conf import settings
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
        ('company', '__first__'),
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
                ('tel2', models.CharField(blank=True, max_length=200, null=True)),
                ('id_card_image', models.ImageField(blank=True, null=True, upload_to='media/account/%Y/%m/%d/', validators=[main.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('electronic_signature', models.ImageField(blank=True, null=True, upload_to='media/account/%Y/%m/%d/', validators=[main.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('gender', models.CharField(blank=True, choices=[('Kişi', 'Kişi'), ('Qadın', 'Qadın')], default=None, max_length=150, null=True)),
                ('salary_calculation_style', models.CharField(blank=True, choices=[('SAATLIQ', 'SAATLIQ'), ('HƏFTƏLİK', 'HƏFTƏLİK'), ('AYLIQ', 'AYLIQ')], default='AYLIQ', max_length=150, null=True)),
                ('hourly_salary', models.FloatField(default=0)),
                ('weekly_salary', models.FloatField(default=0)),
                ('monthly_salary', models.FloatField(default=0)),
                ('salary', models.FloatField(blank=True, default=0, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(max_length=250, null=True)),
                ('street', models.CharField(max_length=250, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True, null=True)),
                ('start_job_date', models.DateField(blank=True, default=None, null=True)),
                ('end_job_date', models.DateField(blank=True, default=None, null=True)),
                ('termination_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supervizor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervizor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervizor', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='supervizor_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('knowledge_level', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('knowledge_level', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('tel1', models.CharField(max_length=50)),
                ('tel2', models.CharField(blank=True, max_length=50, null=True)),
                ('tel3', models.CharField(blank=True, max_length=50, null=True)),
                ('tel4', models.CharField(blank=True, max_length=50, null=True)),
                ('id_card_image', models.ImageField(blank=True, null=True, upload_to='media/account/%Y/%m/%d/', validators=[main.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('gender', models.CharField(blank=True, choices=[('Kişi', 'Kişi'), ('Qadın', 'Qadın')], default=None, max_length=150, null=True)),
                ('customer_type', models.CharField(choices=[('ŞƏXS', 'ŞƏXS'), ('KORPORATİV', 'KORPORATİV')], default=None, max_length=150, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='account.address')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.address'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='company.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='company.department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='company.office'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='company.position'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
