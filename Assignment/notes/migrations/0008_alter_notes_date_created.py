# Generated by Django 4.1 on 2022-09-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0007_alter_notes_sharedwith"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="date_created",
            field=models.DateField(default="2022-09-01"),
        ),
    ]
