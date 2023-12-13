# Generated by Django 4.2.5 on 2023-12-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cert', '0002_alter_gradeturma_fk_in_ex_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeturma',
            name='fk_in_ex',
        ),
        migrations.AddField(
            model_name='gradeturma',
            name='externo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Externo'),
        ),
        migrations.AddField(
            model_name='gradeturma',
            name='interno',
            field=models.IntegerField(blank=True, null=True, verbose_name='Interno'),
        ),
    ]
