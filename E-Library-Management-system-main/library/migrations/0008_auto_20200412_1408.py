# Generated by Django 3.0.5 on 2020-04-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200412_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='Mail_ID',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
