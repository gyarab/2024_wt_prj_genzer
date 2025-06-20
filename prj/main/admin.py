from django.contrib import admin
from .models import Film, Osoba, Recenze

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'rokPremiery', 'zanr')

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'povolani', 'obrazekUrl')  # Use valid fields from the Osoba model

@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
    list_display = ('username', 'obsah', 'pocetHvezd')  # Use valid fields from the Recenze model