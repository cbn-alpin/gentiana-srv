# -*- coding:utf-8 -*-
# Fichier de configuration

# Don't use this file to store secrets. Use .env instead.
# Use .env file to store SECRET_KEY with variable ATLAS_SECRET_KEY

# Nom de la structure
STRUCTURE = "Gentiana"

# Nom de l'application
NOM_APPLICATION = "Atlas"

# Enable organism module : organism sheet + organism participation on species sheet
ORGANISM_MODULE = False

# +---------------------------------------------------------------------+
# Multilingual

# Default language, also used when multilingual is disabled
DEFAULT_LANGUAGE = 'fr'

# Activate multilingual
MULTILINGUAL = False

# Available languages
# Don't delete, even if you disable MULTILINGUAL
# You need to add your own default language (DEFAULT_LANGUAGE) here if it's not present
# Check documentation to add another language
LANGUAGES = {
    'en': {
        'name' : 'English',
        'flag_icon' : 'flag-icon-gb',
        'months' : ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        },
    'fr': {
        'name' : 'Français',
        'flag_icon' : 'flag-icon-fr',
        'months' : ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
        },
    'it': {
        'name' : 'Italiano',
        'flag_icon' : 'flag-icon-it',
        'months' : ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
        }
}
# +---------------------------------------------------------------------+
# Cartographie

# Configuration des cartes (centre du territoire, couches CARTE et ORTHO, échelle par défaut...)
MAP = {
    'LAT_LONG': [44.7952, 6.2287],
    'FIRST_MAP': {
            'url' : '//{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
            'attribution' : '&copy OpenStreetMap',
            'tileName' : 'OSM'
    },
    'SECOND_MAP' : {'url' :'//a.tile.opentopomap.org/{z}/{x}/{y}.png',
            'attribution' : '&copy OpenStreetMap-contributors, SRTM | Style: &copy OpenTopoMap (CC-BY-SA)',
            'tileName' : 'OTM'
    },
    'ZOOM' : 10,
    # Pas du slider sur les annees d'observations: 1 = pas de 1 an sur le slider
    'STEP': 1,
    # Couleur et épaisseur des limites du territoire
    'BORDERS_COLOR': '#000000',
    'BORDERS_WEIGHT': 3,
    'ENABLE_SLIDER': True
}
