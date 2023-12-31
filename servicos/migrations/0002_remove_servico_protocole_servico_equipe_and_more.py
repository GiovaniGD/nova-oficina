# Generated by Django 4.2.6 on 2023-12-03 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipes', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='protocole',
        ),
        migrations.AddField(
            model_name='servico',
            name='equipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipes.equipe'),
        ),
        migrations.AddField(
            model_name='servico',
            name='identificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TA', 'Troca de amortecedores'), ('TO', 'Troca de óleo'), ('TE', 'Troca de embreagem'), ('TP', 'Troca de pneu')], max_length=3),
        ),
    ]
