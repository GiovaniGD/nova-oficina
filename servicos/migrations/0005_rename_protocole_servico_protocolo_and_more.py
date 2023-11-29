from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_servicoadicional_servico_servicos_adicionais'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='protocole',
            new_name='protocolo',
        ),
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TA', 'Troca de amortecedores'), ('TO', 'Troca de óleo'), ('TE', 'Troca de embreagem'), ('TP', 'Troca de pneu')], max_length=3),
        ),
    ]
