# Generated by Django 3.2.5 on 2021-07-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturePlanning', '0017_auto_20210724_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_familys',
            name='Fam_name1',
            field=models.CharField(default='Rr', max_length=80, unique=True),
        ),
    ]
