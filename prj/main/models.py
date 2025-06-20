from django.db import models

class Film(models.Model):
    nazev = models.CharField(max_length=300)
    rokPremiery = models.IntegerField(null=True, blank=True)
    obrazekUrl = models.CharField(max_length=300)
    zanr = models.CharField(max_length=300)
    reziseri = models.ManyToManyField('Osoba', related_name="directed_films", blank=True)
    herci = models.ManyToManyField('Osoba', related_name="acted_films", blank=True)
    recenze = models.ManyToManyField('Recenze', related_name="film_reviews", blank=True)

    def __str__(self):
        return f"{self.nazev} ({self.rokPremiery})"

class Osoba(models.Model):
    jmeno = models.CharField(max_length=300)
    povolani = models.CharField(max_length=300)
    obrazekUrl = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.jmeno}"

class Recenze(models.Model):
    username = models.CharField(max_length=300)
    obsah = models.TextField(blank=True, default="")
    pocetHvezd = models.IntegerField()
    datumPridani = models.DateField()

    def __str__(self):
        return f"{self.username} ({self.datumPridani})"