# Generated by Django 2.1.1 on 2018-09-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_dolls', '0002_auto_20180914_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollstatus',
            name='bullet',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='장탄 수'),
        ),
    ]
