# Generated by Django 5.0.3 on 2024-03-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNumber', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
            ],
        ),
    ]
