# Generated by Django 5.0.6 on 2024-06-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfilili', '0002_detailregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailregistration',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
