# Generated by Django 2.0.6 on 2019-06-23 23:36

import apps.db_data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("db_data", "0018_auto_20190623_0120")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="video2",
            field=models.FileField(
                blank=True,
                max_length=255,
                upload_to=apps.db_data.models.person_photo_path_alt,
            ),
        )
    ]
