from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_servico_identificador'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='servicos_adicionais',
            field=models.ManyToManyField(to='servicos.servicoadicional'),
        ),
    ]
