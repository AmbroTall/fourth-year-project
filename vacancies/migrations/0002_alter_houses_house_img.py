# Generated by Django 3.2.3 on 2021-06-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='house_img',
            field=models.ImageField(default='house3.jpg', upload_to='images'),
        ),
    ]
