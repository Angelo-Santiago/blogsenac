from django.db import models

from utils.base_models import BaseModel

class Authors(BaseModel):
    nome = models.CharField(
        max_length=50, verbose_name="Nome do Autor"
    )
    class Meta:
        db_table = 'Autores'

    def __str__(self):
        return self.nome

