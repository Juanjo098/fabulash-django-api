# Generated by Django 4.2.7 on 2023-11-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pestanas',
            name='tamano',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
