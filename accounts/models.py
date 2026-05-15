# models.py — Définit la table User de MonBut dans la base de données

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,   # Base minimale pour créer un User custom
    BaseUserManager,    # Gestionnaire pour créer des users
    PermissionsMixin    # Ajoute le système de permissions Django
)

# ── Le gestionnaire d'utilisateurs ──────────────────────────
# UserManager définit comment créer un utilisateur normal
# et un superutilisateur (administrateur).
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Vérifie que l'email est fourni
        if not email:
            raise ValueError('L\'email est obligatoire')
        # Normalise l'email (met le domaine en minuscules)
        # ex: Pascal@Gmail.COM → Pascal@gmail.com
        email = self.normalize_email(email)
        # Crée l'objet User sans le sauvegarder en base
        user = self.model(email=email, **extra_fields)
        # Hash le mot de passe avant de le sauvegarder
        # Ne jamais stocker un mot de passe en clair !
        user.set_password(password)
        # Sauvegarde l'utilisateur dans la base de données
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Un superuser a toutes les permissions par défaut
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# ── Le modèle User personnalisé ──────────────────────────────
class User(AbstractBaseUser, PermissionsMixin):

    # Choix possibles pour le rôle de l'utilisateur
    # Format : (valeur_stockée_en_base, label_affiché)
    ROLE_CHOICES = [
        ('student', 'Student'),      # Étudiant cherchant des missions
        ('employer', 'Employer'),    # Employeur publiant des offres
    ]

    # Champ email — identifiant principal de MonBut
    # unique=True : deux users ne peuvent pas avoir le même email
    email = models.EmailField(unique=True)

    # Rôle de l'utilisateur : étudiant ou employeur
    # max_length=20 : longueur max de la valeur stockée
    # choices : liste des valeurs autorisées
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    # Indique si le compte est vérifié (email confirmé)
    # default=False : non vérifié à la création
    is_verified = models.BooleanField(default=False)

    # Champs requis par Django pour le panneau d'administration
    is_active = models.BooleanField(default=True)   # Compte actif ?
    is_staff = models.BooleanField(default=False)    # Accès admin ?

    # Date de création du compte — auto_now_add=True :
    # Django remplit ce champ automatiquement à la création
    date_joined = models.DateTimeField(auto_now_add=True)

    # Associe le UserManager qu'on a créé ci-dessus à ce modèle
    objects = UserManager()

    # Définit quel champ est utilisé comme identifiant de connexion
    # Ici l'email remplace le username par défaut de Django
    USERNAME_FIELD = 'email'

    # Champs demandés en plus lors de la création d'un superuser
    # via la commande : python manage.py createsuperuser
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        # Représentation lisible de l'objet User
        # Affiché dans l'admin Django et le shell Python
        return self.email

    class Meta:
        # Nom de la table dans la base de données
        db_table = 'users'
        # Noms affichés dans le panneau d'administration Django
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
