# Generated by Django 2.2.8 on 2020-03-11 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Planet", new_name="Planets",),
        migrations.AlterModelOptions(
            name="planets",
            options={"verbose_name": "Planeta", "verbose_name_plural": "Planetas"},
        ),
    ]