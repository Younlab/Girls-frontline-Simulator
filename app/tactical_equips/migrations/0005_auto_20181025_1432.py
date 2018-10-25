# Generated by Django 2.1.2 on 2018-10-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_equips', '0004_auto_20181025_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollequip',
            name='company',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dollequip',
            name='exclusiveRate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dollequip',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dollequip',
            name='maxLevel',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dollequip',
            name='type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]