# Generated by Django 3.2.7 on 2021-09-05 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="is_superuser",
            new_name="is_superadmin",
        ),
    ]
