# Generated by Django 2.0.6 on 2019-06-23 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("db_data", "0016_auto_20190623_0107")]

    operations = [migrations.RemoveField(model_name="officer", name="enabled")]
