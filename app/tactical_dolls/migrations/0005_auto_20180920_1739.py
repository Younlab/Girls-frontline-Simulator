# Generated by Django 2.1.1 on 2018-09-20 08:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_dolls', '0004_auto_20180920_0007'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='doll',
            managers=[
                ('doll_update', django.db.models.manager.Manager()),
            ],
        ),
    ]