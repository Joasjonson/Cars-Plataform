# Generated by Django 5.1.6 on 2025-03-11 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='cars/no-image.jpeg', null=True, upload_to='cars/'),
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='cars.car')),
            ],
        ),
    ]
