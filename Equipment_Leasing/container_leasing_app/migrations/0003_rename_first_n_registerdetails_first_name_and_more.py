# Generated by Django 4.0.7 on 2022-12-24 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('container_leasing_app', '0002_rename_first_name_registerdetails_first_n_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdetails',
            old_name='First_N',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='registerdetails',
            old_name='Last_N',
            new_name='Last_Name',
        ),
        migrations.RenameField(
            model_name='registerdetails',
            old_name='Phone_Num',
            new_name='Phone_Number',
        ),
    ]
