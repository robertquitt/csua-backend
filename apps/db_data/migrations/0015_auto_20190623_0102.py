# Generated by Django 2.0.6 on 2019-06-23 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("db_data", "0014_auto_20190623_0050")]

    operations = [
        migrations.AlterField(
            model_name="officership",
            name="tutor_subjects",
            field=models.ManyToManyField(blank=True, to="db_data.UcbClass"),
        ),
        migrations.AlterField(
            model_name="person",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
                to_field="username",
            ),
        ),
        migrations.AlterField(
            model_name="semester",
            name="events",
            field=models.ManyToManyField(blank=True, to="db_data.Event"),
        ),
    ]
