# Generated by Django 4.1.7 on 2023-04-13 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='id_generolibro',
            new_name='id_genero_libro',
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('numero_identidad', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('foto_usuario', models.ImageField(upload_to='fotos')),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.ciudad')),
            ],
        ),
    ]
