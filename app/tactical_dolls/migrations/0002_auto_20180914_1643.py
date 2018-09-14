# Generated by Django 2.1.1 on 2018-09-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tactical_dolls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollstatus',
            name='armor',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='장갑'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='armor_piercing',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='장갑 관통'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='crit',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='크리티컬 확률(%)'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='critdmg',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='크리티컬 데미지 추가 증가량(%)'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='dodge',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='회피'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='hit',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='명중'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='hp',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='체력'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='pow',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='화력'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='range',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='사거리(철혈)'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='사속'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='shield',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='보호막(철혈)'),
        ),
        migrations.AlterField(
            model_name='dollstatus',
            name='speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='이동속도'),
        ),
    ]
