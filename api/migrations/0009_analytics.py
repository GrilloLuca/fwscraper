# Generated by Django 2.1.3 on 2018-12-01 16:22

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181128_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=20)),
                ('data', jsonfield.fields.JSONField()),
            ],
        ),
    ]
