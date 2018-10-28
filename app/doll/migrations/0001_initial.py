# Generated by Django 2.1.2 on 2018-10-27 18:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('code_name', models.CharField(max_length=50)),
                ('rank', models.PositiveSmallIntegerField()),
                ('type', models.CharField(max_length=10)),
                ('build_time', models.PositiveIntegerField()),
                ('grow', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='doll_image')),
                ('image_d', models.ImageField(upload_to='doll_image_d')),
                ('obtain', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None), size=None)),
                ('slot_01', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None), size=None)),
                ('slot_02', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None), size=None)),
                ('slot_03', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('center', models.PositiveSmallIntegerField()),
                ('pos', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None), size=None)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='EffectGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pow', models.PositiveIntegerField()),
                ('hit', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('dodge', models.PositiveIntegerField()),
                ('critical_percent', models.PositiveIntegerField()),
                ('cool_down', models.PositiveIntegerField()),
                ('armor', models.PositiveIntegerField()),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Effect')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('code_name', models.CharField(max_length=50)),
                ('skill_image', models.ImageField(blank=True, null=True, upload_to='skill_image')),
                ('cool_down_type', models.CharField(max_length=30)),
                ('initial_cool_down', models.PositiveIntegerField()),
                ('consumption', models.PositiveIntegerField()),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='SkillData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cool_down', models.PositiveIntegerField(blank=True, null=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.PositiveIntegerField()),
                ('pow', models.PositiveIntegerField()),
                ('hit', models.PositiveIntegerField()),
                ('dodge', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('armor_piercing', models.PositiveIntegerField()),
                ('critical_harm_rate', models.PositiveIntegerField()),
                ('critical_percent', models.PositiveIntegerField()),
                ('bullet', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
                ('night_view', models.PositiveIntegerField()),
                ('armor', models.PositiveIntegerField()),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialogue01', models.TextField(blank=True, null=True)),
                ('dialogue02', models.TextField(blank=True, null=True)),
                ('dialogue03', models.TextField(blank=True, null=True)),
                ('introduce', models.TextField(blank=True, null=True)),
                ('allhallows', models.TextField(blank=True, null=True)),
                ('dialogue_wedding', models.TextField(blank=True, null=True)),
                ('soul_contract', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=None), size=None)),
                ('gain', models.TextField(blank=True, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doll.Doll')),
            ],
        ),
    ]
