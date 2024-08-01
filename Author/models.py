from django.db import models

from utils.base_models import BaseModel

class Author(BaseModel):
    nome = models.Charfield(
        max_length=50, verbose_name="Nome do Autor"
    )