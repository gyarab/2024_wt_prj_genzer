from django.db import models

class Film(models.Model):
    nazev = models.CharField(max_length=300)
    rokPremiery = models.IntegerField(null=True, blank=True)
    obrazekUrl = models.CharField(max_length=300)
    zanr = models.CharField(max_length=300)
    reziseri = models.ForeignKey('Osoba', null=True, on_delete=models.SET_NULL)
    herci = models.ForeignKey('Osoba', null=True, on_delete=models.SET_NULL)
    recenze = models.ForeignKey('Recenze', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} ({self.RokPremiery})"

class Osoba(models.Model):
    jmeno = models.CharField(max_length=300)
    povolani = models.CharField(max_length=300)
    filmy = models.ForeignKey('Film', null=True, on_delete=models.SET_NULL)
    obrazekUrl = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.jmeno}"
    
class Recenze(models.Model):
    username = models.CharField(max_length=300)
    obsah = models.TextField(blank=True, default="")
    pocetHvezd = models.IntegerField(max_length=5)
    datumPridani = models.DateField.auto_now_add()

    def __str__(self):
        return f"{self.username} ({self.RokPremiery})"
