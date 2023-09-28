# Generated by Django 3.2.21 on 2023-09-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servidor', models.CharField(max_length=128)),
                ('id_servidor', models.CharField(max_length=128)),
                ('situacao_vinculo', models.CharField(max_length=128)),
                ('uorg', models.CharField(max_length=128)),
                ('nivel_funcao', models.CharField(max_length=128)),
                ('cargo', models.CharField(max_length=128)),
                ('nome_uorg', models.CharField(max_length=128)),
                ('escolaridade', models.CharField(max_length=128)),
                ('aposentadoria', models.CharField(max_length=128)),
                ('unidade', models.CharField(max_length=128)),
                ('caminho', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=128)),
                ('setor', models.CharField(max_length=128)),
                ('categoria', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'vw_servidores',
                'managed': False,
            },
        ),
    ]
