# Generated by Django 4.0.5 on 2022-07-03 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_company_alter_user_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sv_image',
            new_name='id_card_image',
        ),
    ]
