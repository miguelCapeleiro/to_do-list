from django.db import models
from django.conf import settings
# Create your models here.

class Task (models.Model):
    class Prioriry(models.TextChoices):
        BAIXA = 'B', 'Baixa'
        MEDIA = 'M', 'Média'
        Alta = 'A', 'Alta'
        
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        null= True,
        blank = True
    )
    titulo = models.CharField('Titulo', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    concluida = models.BooleanField('Concluida',default=False)
    prioridade = models.CharField(
        'Prioridade',
        max_length=1,
        choices=Prioriry.choices,
        default=Prioriry.MEDIA,
    )
    data_limite = models.DateField("Data limite", null = True, blank = True)
    criado_em = models.DateTimeField("Criado Em", auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    
    class meta:
        ordering = ['concluida', 'data_limite','-prioridade', '-criado_em']
        
    def __str__(self) -> str:
        return self.titulo
    