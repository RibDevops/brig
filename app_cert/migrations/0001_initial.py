# Generated by Django 4.2.10 on 2024-02-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField(verbose_name='Ano')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Ano',
                'verbose_name_plural': 'Anos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('curso_sigla', models.CharField(max_length=20, verbose_name='Curso sigla')),
                ('curso_descricao', models.CharField(max_length=100, null=True, verbose_name='Curso descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'cursos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Forca_Orgao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('forca_orgao', models.CharField(max_length=30, verbose_name='Força/Orgão Externo')),
                ('forca_orgao_descricao', models.CharField(max_length=50, null=True, verbose_name='Força/Orgão Externo Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Força/Orgão',
                'verbose_name_plural': 'Forças/Orgãos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagem', models.CharField(max_length=50, null=True, verbose_name='Imagem')),
                ('imagem_desc', models.CharField(max_length=50, null=True, verbose_name='Imagem descrição')),
                ('imagem_img', models.ImageField(blank=True, null=True, upload_to='%Y/%m/')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='ImagemTipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagemTipo', models.CharField(max_length=20, verbose_name='Tipo da imagem')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='In_Ex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('in_ex', models.CharField(max_length=20, verbose_name='Tipo Interno/Externo')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Interno/Externo',
                'verbose_name_plural': 'Internos/Externos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Instrucao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('instrucao_sigla', models.CharField(max_length=255, verbose_name='Sigla da instrução')),
                ('instrucao_descricao', models.CharField(max_length=255, verbose_name='Descrição da instrução')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status_descricao', models.CharField(max_length=20, verbose_name='Status Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Textos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=50, null=True, verbose_name='Texto')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Texto',
                'verbose_name_plural': 'Textos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo do curso - EAD/PRE/SEMI')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Tratamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tratamento', models.CharField(max_length=20, null=True, verbose_name='Tratamento')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Tratamento',
                'verbose_name_plural': 'Tratamentos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('turma_sgc', models.CharField(max_length=50, verbose_name='Nome conforme arquivo da SGC Intraer:')),
                ('turma', models.CharField(max_length=50, verbose_name='Descrição que irá aparecer no certificado:')),
                ('data_turma_interno', models.CharField(blank=True, max_length=200, null=True, verbose_name='Texto data alunos Internos')),
                ('data_turma_externo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Texto data alunos Externos')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fk_ano_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.ano', verbose_name='FK Ano do Curso')),
                ('fk_assinaturas_ch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_imagem_ch', to='app_cert.imagem', verbose_name='FK Assinaturas CH')),
                ('fk_assinaturas_dpl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_imagem_dpl', to='app_cert.imagem', verbose_name='FK Chefe de divisão')),
                ('fk_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.curso', verbose_name='FK Curso')),
                ('fk_img_frente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_img_frente', to='app_cert.imagem', verbose_name='FK Frente')),
                ('fk_img_fundo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_img_fundo', to='app_cert.imagem', verbose_name='FK Fundo')),
                ('fk_modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.modelo', verbose_name='FK Modelo: Certificado/Honra/Participação')),
                ('fk_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.tipo', verbose_name='FK Tipo: EAD - Presencial')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Quadro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quadro', models.CharField(max_length=10, verbose_name='Quadro')),
                ('quadro_descricao', models.CharField(max_length=20, verbose_name='Quadro Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fk_forca_orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.forca_orgao', verbose_name='FK Força/Orgão Externo')),
            ],
            options={
                'verbose_name': 'Quadro',
                'verbose_name_plural': 'Quadros',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hierarquia', models.IntegerField(verbose_name='Hierarquia')),
                ('posto', models.CharField(max_length=10, verbose_name='Posto')),
                ('posto_descricao', models.CharField(max_length=20, verbose_name='Posto Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fk_forca_orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.forca_orgao', verbose_name='FK Força/Orgão Externo')),
            ],
            options={
                'verbose_name': 'Posto',
                'verbose_name_plural': 'Postos',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Om',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('om', models.CharField(blank=True, max_length=30, null=True, verbose_name='OM')),
                ('om_descricao', models.CharField(blank=True, max_length=100, null=True, verbose_name='OM Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fk_forca_orgao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_cert.forca_orgao', verbose_name='FK Força/Orgão Externo')),
            ],
            options={
                'verbose_name': 'Força/Orgão',
                'verbose_name_plural': 'Forças/Orgãos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='modelo',
            name='fk_texto_modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_texto_modelo', to='app_cert.textos', verbose_name='FK Texto Tipo'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='fk_texto_modelo_desc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_texto_modelo_desc', to='app_cert.textos', verbose_name='FK Texto primeira parte'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='fk_texto_motivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_texto_motivo', to='app_cert.textos', verbose_name='FK Texto Motivo'),
        ),
        migrations.AddField(
            model_name='imagem',
            name='imagem_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.imagemtipo', verbose_name='Imagem Tipo'),
        ),
        migrations.CreateModel(
            name='GradeTurma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('interno', models.IntegerField(blank=True, default=0, null=True, verbose_name='Interno')),
                ('externo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Externo')),
                ('tempo_instrucao', models.IntegerField(blank=True, null=True, verbose_name='Tempo da Instrução')),
                ('fk_instrucao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_cert.instrucao', verbose_name='FK Instrução')),
                ('fk_turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.turma', verbose_name='FK Turma')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('especialidade', models.CharField(max_length=10, verbose_name='Especialidade')),
                ('especialidade_descricao', models.CharField(max_length=20, verbose_name='Especialidade Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fk_forca_orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cert.forca_orgao', verbose_name='FK Força/Orgão Externo')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aluno_nome', models.CharField(max_length=100, verbose_name='Nome do Aluno')),
                ('aluno_cpf', models.CharField(max_length=14, null=True, verbose_name='CPF')),
                ('aluno_email', models.CharField(max_length=50, null=True, verbose_name='Email do Aluno')),
                ('aluno_nota', models.CharField(blank=True, max_length=5, null=True, verbose_name='Nota do Aluno')),
                ('codigo_hash', models.CharField(blank=True, max_length=20, null=True, verbose_name='Código de Verificação')),
                ('qrcode', models.CharField(blank=True, max_length=100, null=True, verbose_name='QrCode')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='OBS:')),
                ('fk_especialidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.especialidade', verbose_name='Especialidade')),
                ('fk_forca_orgao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.forca_orgao', verbose_name='Força/Orgão')),
                ('fk_in_ex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_cert.in_ex', verbose_name='Tipo do Aluno - Interno/Externo')),
                ('fk_om', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.om', verbose_name='OM')),
                ('fk_posto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.posto', verbose_name='Posto')),
                ('fk_quadro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.quadro', verbose_name='Quadro')),
                ('fk_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.status', verbose_name='Situação')),
                ('fk_tratamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_cert.tratamento', verbose_name='Tratamento')),
                ('fk_turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_cert.turma', verbose_name='Turma')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['id'],
            },
        ),
    ]
