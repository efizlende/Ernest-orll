# Generated by Django 4.2.11 on 2024-03-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crudapp', '0003_rename_estudante_employee_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='Estudante',
        ),
    ]
