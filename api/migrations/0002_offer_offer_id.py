# Generated by Django 2.1.3 on 2018-11-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
