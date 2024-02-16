# Generated by Django 5.0.1 on 2024-02-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0008_spectrum_specimen"),
    ]

    operations = [
        migrations.AddField(
            model_name="spectrum",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/images/spectra/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="spectrum",
            name="file",
            field=models.FileField(upload_to="uploads/spectra/%Y/%m/%d/"),
        ),
    ]
