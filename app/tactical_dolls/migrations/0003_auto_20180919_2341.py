# Generated by Django 2.1.1 on 2018-09-19 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_dolls', '0002_auto_20180917_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dollsdimage',
            name='doll',
        ),
        migrations.DeleteModel(
            name='DollSDImage',
        ),
    ]