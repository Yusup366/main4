# Generated by Django 5.1.4 on 2025-01-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
