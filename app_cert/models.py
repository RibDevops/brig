from django.db import models

class Forca_Orgao(models.Model):
    id = models.AutoField(primary_key=True)
    forca_orgao = models.CharField(max_length=30, verbose_name="Força/Orgão Externo")
    forca_orgao_descricao = models.CharField(max_length=50, verbose_name="Força/Orgão Externo Descrição", null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.forca_orgao)
    
    class Meta:
        verbose_name = 'Força/Orgão'
        verbose_name_plural = 'Forças/Orgãos'
        ordering = ['id']

class Om(models.Model):
    id = models.AutoField(primary_key=True)
    fk_forca_orgao = models.ForeignKey(Forca_Orgao, on_delete=models.CASCADE, verbose_name="Força/Orgão Externo", null=True, blank=True)
    om = models.CharField(max_length=30, verbose_name="OM", null=True, blank=True)
    om_descricao = models.CharField(max_length=100, verbose_name="OM Descrição", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.om)
    
    class Meta:
        verbose_name = 'Força/Orgão'
        verbose_name_plural = 'Forças/Orgãos'
        ordering = ['id']

class Posto(models.Model):
    id = models.AutoField(primary_key=True)
    fk_forca_orgao = models.ForeignKey(Forca_Orgao, on_delete=models.CASCADE, verbose_name="Força/Orgão Externo")
    hierarquia = models.IntegerField(verbose_name="Hierarquia")
    posto = models.CharField(max_length=10, verbose_name="Posto")
    posto_descricao = models.CharField(max_length=20, verbose_name="Posto Descrição")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.posto
    
    class Meta:
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'
        ordering = ['create_at']

class Quadro(models.Model):
    id = models.AutoField(primary_key=True)
    fk_forca_orgao = models.ForeignKey(Forca_Orgao, on_delete=models.CASCADE, verbose_name="Força/Orgão Externo")
    quadro = models.CharField(max_length=10, verbose_name="Quadro")
    quadro_descricao = models.CharField(max_length=20, verbose_name="Quadro Descrição")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.quadro
    
    class Meta:
        verbose_name = 'Quadro'
        verbose_name_plural = 'Quadros'
        ordering = ['create_at']

class Especialidade(models.Model):
    id = models.AutoField(primary_key=True)
    fk_forca_orgao = models.ForeignKey(Forca_Orgao, on_delete=models.CASCADE, verbose_name="Força/Orgão Externo")
    especialidade = models.CharField(max_length=10, verbose_name="Especialidade")
    especialidade_descricao = models.CharField(max_length=20, verbose_name="Especialidade Descrição")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.especialidade
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
        ordering = ['create_at']

class Ano(models.Model):
    id = models.AutoField(primary_key=True)
    ano = models.IntegerField(verbose_name="Ano")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.ano)
    
    class Meta:
        verbose_name = 'Ano'
        verbose_name_plural = 'Anos'
        ordering = ['create_at']

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status_descricao = models.CharField(max_length=20, verbose_name="Status Descrição")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.status_descricao)
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['create_at']

class ImagemTipo(models.Model):
    id = models.AutoField(primary_key=True)
    imagemTipo = models.CharField(max_length=20, verbose_name="Tipo da imagem")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.imagemTipo)
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['create_at']

class Imagem(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.CharField(max_length=50, verbose_name="Imagem", null=True)
    imagem_desc = models.CharField(max_length=50, verbose_name="Imagem descrição", null=True)
    imagem_tipo = models.ForeignKey(ImagemTipo, on_delete=models.CASCADE, verbose_name="Imagem Tipo")

    # assinatura_dpl_img = models.FileField(upload_to="assinaturas/%Y/%m/")
    imagem_img = models.ImageField(null=True, blank=True, upload_to ="%Y/%m/")
    
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        # return f"{self.imagem} ({self.imagem_desc}) ({self.imagem_img})"
        return f"{self.imagem} - {self.imagem_desc}"
    
    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['create_at']

class Textos(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=50, verbose_name="Texto", null=True)
    # texto_desc = models.CharField(max_length=50, verbose_name="Texto descrição", null=True)   
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.texto}"
        # return self.id
    
    class Meta:
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
        ordering = ['create_at']

class Tipo(models.Model):  # EAD Presencial
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, verbose_name="Tipo do curso - EAD/PRE/SEMI")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.tipo)
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['create_at']

class Tratamento(models.Model):
    id = models.AutoField(primary_key=True)
    tratamento = models.CharField(max_length=20, verbose_name="Tratamento", null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.tratamento
    
    class Meta:
        verbose_name = 'Tratamento'
        verbose_name_plural = 'Tratamentos'
        ordering = ['create_at']

class In_Ex(models.Model):
    id = models.AutoField(primary_key=True)
    in_ex = models.CharField(max_length=20, verbose_name="Tipo Interno/Externo")
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.in_ex)
    
    class Meta:
        verbose_name = 'Interno/Externo'
        verbose_name_plural = 'Internos/Externos'
        ordering = ['create_at']

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso_sigla = models.CharField(max_length=20, verbose_name="Curso sigla")
    curso_descricao = models.CharField(max_length=100, verbose_name="Curso descrição", null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.curso_sigla
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'cursos'
        ordering = ['id']

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    fk_texto_modelo = models.ForeignKey(Textos, on_delete=models.CASCADE, verbose_name="Texto Tipo", related_name='fk_texto_modelo',null=True)
    fk_texto_modelo_desc = models.ForeignKey(Textos, on_delete=models.CASCADE, verbose_name="Texto primeira parte", related_name='fk_texto_modelo_desc',null=True)
    fk_texto_motivo = models.ForeignKey(Textos, on_delete=models.CASCADE, verbose_name="Texto Motivo", related_name='fk_texto_motivo',null=True)
    # fk_id_aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, verbose_name="ID Aluno", null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        # return self.fk_texto_modelo
        return str(self.fk_texto_modelo)
    
    
    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['create_at']

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    fk_ano_curso = models.ForeignKey(Ano, on_delete=models.CASCADE, verbose_name="Ano do Curso")
    fk_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    fk_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Tipo: EAD - Presencial")
    fk_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, verbose_name="Modelo: Certificado/Honra/Participação")
    
    fk_assinaturas_ch = models.ForeignKey(Imagem, on_delete=models.CASCADE, verbose_name="Assinaturas CH", related_name='fk_imagem_ch', null=True)
    fk_assinaturas_dpl = models.ForeignKey(Imagem, on_delete=models.CASCADE, verbose_name="Chefe de divisão", related_name='fk_imagem_dpl',null=True)
    fk_img_frente = models.ForeignKey(Imagem, on_delete=models.CASCADE, verbose_name="Frente", related_name='fk_img_frente',null=True)
    fk_img_fundo = models.ForeignKey(Imagem, on_delete=models.CASCADE, verbose_name="Fundo", related_name='fk_img_fundo',null=True)

    turma_sgc = models.CharField(max_length=50, verbose_name="Nome conforme arquivo da SGC Intraer:")
    turma = models.CharField(max_length=50, verbose_name="Descrição que irá aparecer no certificado:")
    # turma_numerao = models.IntegerField(verbose_name="Ano")

    # turma_desc = models.CharField(max_length=50, verbose_name="Ex: 1/2023")
    data_turma_interno = models.CharField(max_length=200, verbose_name="Texto data alunos Internos", null=True, blank=True)
    data_turma_externo = models.CharField(max_length=200, verbose_name="Texto data alunos Externos", null=True, blank=True)    
    
    # data_turma_interno = models.DateField(verbose_name="Texto data alunos Internos", null=True, blank=True)
    # data_turma_externo = models.DateField(verbose_name="Texto data alunos Externos", null=True, blank=True)

    # data_inicio_turma_interno = models.DateField(verbose_name="Data de Início Alunos Internos", null=True, blank=True)

    # data_fim_turma_interno = models.DateField(verbose_name="Data de Término Alunos Internos", null=True, blank=True)

    
    # data_inicio_turma_externo = models.DateField(verbose_name="Data de Início Alunos Externos", null=True, blank=True)
    # data_fim_turma_externo = models.DateField(verbose_name="Data de Término Alunos Externos", null=True, blank=True)
  

    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        # return f"Curso {self.id}"
        return str(self.turma_sgc)
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['create_at']

class Instrucao(models.Model):
    id = models.AutoField(primary_key=True)
    # fk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name="Turma")
    instrucao_sigla = models.CharField(max_length=255, verbose_name="Sigla da instrução")
    instrucao_descricao = models.CharField(max_length=255, verbose_name="Descrição da instrução")

    def __str__(self):
        # return f"{self.instrucao_sigla} - {self.instrucao_descricao}"
        return str(self.instrucao_descricao)

class GradeTurma(models.Model):
    id = models.AutoField(primary_key=True)
    fk_turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma", null=True)
    # fk_in_ex = models.ForeignKey(In_Ex, on_delete=models.CASCADE, verbose_name="Tipo Interno Externo", null=True, blank=True)
    interno = models.IntegerField(verbose_name="Interno", null=True, blank=True, default=0)
    externo = models.IntegerField(verbose_name="Externo", null=True, blank=True, default=0)

    # fk_instrucao = models.ForeignKey(Instrucao, on_delete=models.CASCADE, verbose_name="Instrução", null=True, blank=True, default=0)
    fk_instrucao = models.ForeignKey(Instrucao, on_delete=models.CASCADE, verbose_name="Instrução", null=True, blank=True)
    tempo_instrucao = models.IntegerField(verbose_name="Tempo da Instrução", null=True, blank=True)

    def __str__(self):
        # return f"{self.fk_turma} - {self.fk_in_ex} - {self.fk_instrucao} - {self.tempo_instrucao}"
        return str(self.fk_turma)
    
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    
    # fk_curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso", null=True)
    fk_turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma", null=True)
    fk_forca_orgao = models.ForeignKey(Forca_Orgao, on_delete=models.PROTECT, verbose_name="Força/Orgão", null=True)
    fk_om = models.ForeignKey(Om, on_delete=models.PROTECT, verbose_name="OM", null=True)
    
    
    fk_posto = models.ForeignKey(Posto, on_delete=models.PROTECT, verbose_name="Posto", null=True)
    fk_quadro = models.ForeignKey(Quadro, on_delete=models.PROTECT, verbose_name="Quadro", null=True)
    fk_especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, verbose_name="Especialidade", null=True)
    fk_in_ex = models.ForeignKey(In_Ex, on_delete=models.CASCADE, verbose_name="Tipo do Aluno - Interno/Externo", null=True)
    fk_tratamento = models.ForeignKey(Tratamento, on_delete=models.CASCADE, verbose_name="Tratamento", null=True)
    aluno_nome = models.CharField(max_length=100, verbose_name="Nome do Aluno")
    aluno_cpf = models.CharField(max_length=14, verbose_name="CPF", null=True)
    aluno_email = models.CharField(max_length=50, verbose_name="Email do Aluno", null=True, blank=True)
    aluno_nota = models.CharField(max_length=5, verbose_name="Nota do Aluno", null=True, blank=True)
    # codigo_hash = models.TextField(verbose_name="Código de Verificação", null=True,)
    codigo_hash = models.CharField(max_length=20,verbose_name="Código de Verificação", null=True, blank=True)
    qrcode = models.CharField(max_length=100,verbose_name="QrCode", null=True, blank=True)
    fk_status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Situação", null=True, blank=True)
    obs = models.TextField(verbose_name="OBS:", null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
        # return f"{self.aluno_nome} - {self.id}"
        # return f"{self.id} - {self.aluno_nome}"
    
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']