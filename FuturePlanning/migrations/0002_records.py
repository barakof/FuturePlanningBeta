# Generated by Django 3.2.5 on 2021-07-12 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FuturePlanning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rec_Type', models.CharField(max_length=3)),
                ('Start_Date', models.DateField(auto_now=True)),
                ('Family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuturePlanning.familys')),
            ],
        ),
    ]
