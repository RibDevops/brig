# Generated by Django 5.0.2 on 2024-04-30 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='fk_especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.especialidade', verbose_name='Especialidade'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='fk_om',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.om', verbose_name='OM'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='fk_posto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.posto', verbose_name='Posto'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='fk_quadro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.quadro', verbose_name='Quadro'),
        ),
    ]
