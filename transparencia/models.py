from django.db import models

class Servidor(models.Model):
	nome_servidor = models.CharField(max_length=128)
	id_servidor = models.CharField(max_length=128)
	situacao_vinculo = models.CharField(max_length=128)
	uorg = models.CharField(max_length=128)
	nivel_funcao  = models.CharField(max_length=128)
	cargo = models.CharField(max_length=128)
	nome_uorg = models.CharField(max_length=128)
	escolaridade = models.CharField(max_length=128)
	aposentadoria = models.CharField(max_length=128)
	unidade = models.CharField(max_length=128)
	caminho = models.CharField(max_length=128)
	nome = models.CharField(max_length=128)
	setor = models.CharField(max_length=128)
	categoria = models.CharField(max_length=128)
	sexo = models.CharField(max_length=128)
	jornada_trabalho = models.CharField(max_length=128)
	idade = models.CharField(max_length=128)
	categoria = models.CharField(max_length=128)
	
	class Meta:
		managed = False
		db_table = 'vw_servidores'


