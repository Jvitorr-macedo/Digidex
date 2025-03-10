from django.db import models

class Digidex(models.Model):
    NIVEL_CHOICES = [
        ('Iniciante', 'Iniciante'),
        ('Intermediário', 'Intermediário'),
        ('Avançado', 'Avançado'),
        ('Mega', 'Mega'),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='digimon')
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nome
