# Generated by Django 4.2.4 on 2023-09-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_estudiante_direccion_estudiante_imagen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='profesion',
            new_name='materia',
        ),
        migrations.AddField(
            model_name='profesor',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='jpgprofesores/'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
