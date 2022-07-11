# Generated by Django 4.0.5 on 2022-06-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
