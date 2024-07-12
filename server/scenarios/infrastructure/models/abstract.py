from django.db import models

from config.base_model import BaseModel


class LocatedUnitModel(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
