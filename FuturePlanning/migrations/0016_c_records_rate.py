# Generated by Django 3.2.5 on 2021-07-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturePlanning', '0015_c_events_rec_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_records',
            name='Rate',
            field=models.FloatField(default=1.0),
        ),
    ]
