# Generated by Django 4.0.5 on 2022-06-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
