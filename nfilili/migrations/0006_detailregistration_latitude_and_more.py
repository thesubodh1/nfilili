# Generated by Django 5.0.6 on 2024-06-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfilili', '0005_detailregistration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailregistration',
            name='latitude',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='detailregistration',
            name='longitude',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
