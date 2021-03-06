# Generated by Django 4.0.4 on 2022-06-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('ram', models.CharField(blank=True, max_length=20, null=True)),
                ('gpu', models.CharField(blank=True, max_length=20, null=True)),
                ('cpu', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
            ],
        ),
    ]
