# Generated by Django 2.1.2 on 2018-10-09 02:11

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
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='전술 인형 넘버링')),
                ('codename', models.CharField(blank=True, max_length=50, null=True, verbose_name='전술 인형 명칭')),
                ('kr_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rank', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('7', 'extra')], max_length=5, verbose_name='전술 인형 등급')),
                ('type', models.CharField(choices=[('hg', 'hg'), ('ar', 'ar'), ('smg', 'smg'), ('sg', 'sg'), ('mg', 'mg'), ('rf', 'rf')], max_length=3, verbose_name='전술 인형 타입')),
                ('build_time', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='전술 인형 제조 시간')),
                ('grow', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doll_image')),
                ('image_d', models.ImageField(blank=True, null=True, upload_to='doll_image')),
                ('is_upgrade', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DollDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop', models.TextField(blank=True, null=True)),
                ('introduce', models.TextField(blank=True, null=True)),
                ('dialogue1', models.CharField(blank=True, max_length=200, null=True)),
                ('dialogue2', models.CharField(blank=True, max_length=200, null=True)),
                ('dialogue3', models.CharField(blank=True, max_length=200, null=True)),
                ('soul_contract', models.TextField(blank=True, null=True)),
                ('gain', models.CharField(blank=True, max_length=200, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_detail', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('center', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_effect', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEffectGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pow', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dodge', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('critical_percent', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cool_down', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('armor', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_effect_grid', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEffectPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_effect_pos', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEquipSlot01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(blank=True, max_length=60, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_equip_slot01', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEquipSlot02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(blank=True, max_length=60, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_equip_slot02', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollEquipSlot03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(blank=True, max_length=60, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_equip_slot03', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollMindUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mind_piece', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_mind_update', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollSkill01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('codename', models.CharField(blank=True, max_length=50, null=True)),
                ('cool_down_type', models.CharField(blank=True, choices=[('frame', 'frame'), ('turn', 'turn')], max_length=4, null=True)),
                ('initial_cool_down', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('consumption', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_skill01', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollSkill02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('skill_image', models.ImageField(blank=True, null=True, upload_to='doll_skill_images')),
                ('codename', models.CharField(blank=True, max_length=50, null=True)),
                ('cool_down_type', models.CharField(blank=True, choices=[('frame', 'frame'), ('turn', 'turn')], max_length=4, null=True)),
                ('initial_cool_down', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('consumption', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_skill02', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollSkillData01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cool_down', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_skill01_data', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollSkillData02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cool_down', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doll_skill02_data', to='tactical_dolls.Doll')),
            ],
        ),
        migrations.CreateModel(
            name='DollStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('pow', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dodge', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('armor_piercing', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('critical_percent', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bullet', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('armor', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doll_status', to='tactical_dolls.Doll')),
            ],
        ),
    ]
