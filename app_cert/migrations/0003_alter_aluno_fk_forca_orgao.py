# Generated by Django 5.0.2 on 2024-04-30 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cert', '0002_alter_aluno_fk_especialidade_alter_aluno_fk_om_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='fk_forca_orgao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.forca_orgao', verbose_name='Força/Orgão'),
        ),
    ]
