# Generated by Django 5.1.3 on 2024-11-27 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0002_address_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookmodule.address'),
        ),
    ]
