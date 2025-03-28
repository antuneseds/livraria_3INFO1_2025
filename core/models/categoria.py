from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return f"(0{self.id}) {self.descricao}"