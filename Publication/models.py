from django.db import models
from Author.models import Authors
from datetime import date
from utils.base_models import BaseModel

class Publications(BaseModel):
    date_pub = models.DateField(default=date.today)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    pub_text = models.CharField(
        max_length=50, verbose_name="Texto da Publicação"
    )
    pub_title = models.CharField(
        max_length=30, verbose_name="Título da Publicação"
    )

    class Meta:
        db_table = 'publicações'

    def __str__(self):
        return self.pub_title