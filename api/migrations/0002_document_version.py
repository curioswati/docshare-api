# Generated by Django 3.1.7 on 2021-03-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='version',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
