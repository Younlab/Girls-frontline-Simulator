# Generated by Django 2.1.2 on 2018-10-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_equips', '0002_auto_20181008_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='dollequip',
            name='kr_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
