from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_AMORTECEDORES = "TA", "Troca de amortecedores"
    TROCA_OLEO = "TO", "Troca de óleo"
    TROCA_EMBREAGEM = "TE", "Troca de embreagem"
    TROCA_PNEU = "TP", "Troca de pneu"