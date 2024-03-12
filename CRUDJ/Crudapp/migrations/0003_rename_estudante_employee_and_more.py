# Generated by Django 4.2.11 on 2024-03-09 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crudapp', '0002_rename_employee_estudante_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudante',
            new_name='Employee',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='contacto',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='nome',
            new_name='name',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='tblemployee',
        ),
    ]
