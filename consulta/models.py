from django.db import models


class Consultas(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=250)
    sono_alterado = models.BooleanField(default=False)
    peso_alterado = models.BooleanField(default=False)
    apetite_alterado = models.BooleanField(default=False)

    def __str__(self):
        return self.pk

