# Generated by Django 3.2.7 on 2021-10-03 10:05

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magazin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descriere', models.TextField(blank=True)),
                ('add_at', models.DateTimeField(auto_now_add=True)),
                ('photo1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo3', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('SKU', models.CharField(default=django.utils.crypto.get_random_string, max_length=8, unique=True)),
            ],
        ),
    ]
