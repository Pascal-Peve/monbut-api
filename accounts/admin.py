# admin.py — Configure l'affichage du modèle User dans l'admin Django

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User  # Importe notre User depuis models.py

# @admin.register(User) est un décorateur qui enregistre
# le modèle User dans le panneau d'administration Django.
# Sans cette ligne, User n'apparaît pas dans l'admin.
@admin.register(User)
class UserAdmin(BaseUserAdmin):

    # Colonnes affichées dans la liste des utilisateurs
    list_display = ('email', 'role', 'is_verified', 'date_joined')

    # Champs sur lesquels on peut filtrer dans l'admin
    list_filter = ('role', 'is_verified', 'is_active')

    # Champs dans lesquels on peut faire une recherche
    search_fields = ('email',)

    # Tri par défaut : les plus récents en premier
    ordering = ('-date_joined',)

    # On retire username des champs requis car on utilise email
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations', {'fields': ('role', 'is_verified')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'role', 'password1', 'password2'),
        }),
    )

