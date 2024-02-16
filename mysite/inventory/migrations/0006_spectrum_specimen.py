# Generated by Django 5.0.1 on 2024-02-15 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0005_remove_spectrum_specimen"),
    ]

    operations = [
        migrations.AddField(
            model_name="spectrum",
            name="specimen",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="inventory.specimen",
            ),
        ),
    ]
