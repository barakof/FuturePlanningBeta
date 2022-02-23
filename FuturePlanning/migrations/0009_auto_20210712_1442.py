# Generated by Django 3.2.5 on 2021-07-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturePlanning', '0008_records_test1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='test',
        ),
        migrations.RemoveField(
            model_name='records',
            name='test1',
        ),
        migrations.AddField(
            model_name='records',
            name='Rec_Name',
            field=models.CharField(default='In', max_length=50),
        ),
        migrations.AddField(
            model_name='records',
            name='Start_Date',
            field=models.CharField(default='mm_yyyy', max_length=20),
        ),
    ]