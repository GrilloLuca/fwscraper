# Generated by Django 2.1.3 on 2018-11-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('menulink', models.CharField(max_length=255)),
                ('hilite', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]