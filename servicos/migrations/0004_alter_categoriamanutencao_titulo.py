# Generated by Django 4.2.6 on 2023-12-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_remove_servico_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('Troca de amortecedores', 'Troca de amortecedores'), ('Troca de óleo', 'Troca de óleo'), ('Troca de embreagem', 'Troca de embreagem'), ('Troca de pneu', 'Troca de pneu')], max_length=100),
        ),
    ]
