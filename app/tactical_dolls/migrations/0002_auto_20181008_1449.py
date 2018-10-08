# Generated by Django 2.1.2 on 2018-10-08 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_dolls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DollDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop', models.TextField(blank=True, max_length=255, null=True)),
                ('context', models.TextField(blank=True, max_length=255, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_detail', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.RemoveField(
            model_name='dollskill01',
            name='skill_image',
        ),
    ]
