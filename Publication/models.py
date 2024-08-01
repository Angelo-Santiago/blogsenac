from django.db import models
from utils.base_models import BaseModel
from Author.models

class Publication(BaseModel):
    author = models.Charfield(
        max_length=50, verbose_name="Nome da Publicação"
    )