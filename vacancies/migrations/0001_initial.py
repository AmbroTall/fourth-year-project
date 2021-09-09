# Generated by Django 3.2.3 on 2021-06-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('house_img', models.ImageField(blank=True, default='house3.jpg', null=True, upload_to='images')),
                ('slug', models.SlugField(blank=True, max_length=20, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, null=True, to='vacancies.Tags')),
            ],
        ),
    ]
