"""
settings.py — Fichier de configuration centrale du projet Django MonBut.

Généré automatiquement par 'django-admin startproject core .'
puis personnalisé par nous pour les besoins de MonBut.

Documentation officielle :
https://docs.djangoproject.com/en/6.0/topics/settings/
"""

# On importe la classe Path du module pathlib de Python.
# Path permet de construire des chemins vers des fichiers et dossiers
# de manière compatible avec tous les systèmes d'exploitation
# (Windows utilise \, Linux/Mac utilisent /)
# Avec Path, on écrit toujours BASE_DIR / 'dossier' / 'fichier'
# et Python s'occupe du bon séparateur selon le système.
from pathlib import Path


# ─────────────────────────────────────────────────────────
# CHEMINS DU PROJET
# ─────────────────────────────────────────────────────────

# BASE_DIR = chemin absolu vers le dossier racine du projet (monbut-api/)
# On le construit étape par étape :
# - Path(__file__)  → chemin vers ce fichier settings.py
#                     ex: C:/Users/.../monbut-api/core/settings.py
# - .resolve()      → transforme en chemin absolu complet
# - .parent         → remonte d'un niveau : core/settings.py → core/
# - .parent         → remonte encore d'un niveau : core/ → monbut-api/
#
# BASE_DIR est utilisé partout pour construire des chemins
# relatifs à la racine du projet sans jamais écrire de
# chemin absolu en dur (ce qui casserait sur un autre PC).
BASE_DIR = Path(__file__).resolve().parent.parent


# ─────────────────────────────────────────────────────────
# SÉCURITÉ
# ─────────────────────────────────────────────────────────

# Clé secrète utilisée par Django pour signer et chiffrer
# de nombreux mécanismes de sécurité :
# - les cookies de session
# - les tokens CSRF (protection contre les attaques de formulaires)
# - les signatures de données sensibles
#
# ⚠️ RÈGLES ABSOLUES À RETENIR :
# 1. Ne JAMAIS partager cette clé publiquement (GitHub, forum, etc.)
# 2. En production : la stocker dans une variable d'environnement
#    et non directement dans ce fichier
# 3. En production : utiliser une clé différente et plus complexe
SECRET_KEY = 'django-insecure-w&yyxr+pr3l-z0ld(3xz+-jwby!5ng+0j8n*g2xmf33uyv310l'

# Mode débogage — contrôle l'affichage des erreurs
#
# ✅ DEBUG = True (développement) :
#    → Affiche les erreurs détaillées dans le navigateur
#    → Montre le code source en cas d'erreur
#    → Active des outils de développement supplémentaires
#
# ❌ DEBUG = False (production) :
#    → Cache les détails des erreurs aux utilisateurs
#    → Affiche une page d'erreur générique et sécurisée
#    → OBLIGATOIRE en production pour la sécurité
DEBUG = True

# Liste des domaines autorisés à accéder à ce serveur Django.
# [] = vide en développement car on travaille uniquement en local.
# En production, on met le vrai domaine de l'API :
# ALLOWED_HOSTS = ['api.monbut.com', 'monbut.com']
ALLOWED_HOSTS = []

# Liste des origines (adresses) autorisées à envoyer des requêtes
# à notre API depuis un navigateur web.
#
# PROBLÈME QUE ÇA RÉSOUT :
# Le frontend React tourne sur → http://localhost:3000
# Le backend Django tourne sur → http://localhost:8000
# Les ports sont différents = origines différentes.
# Par défaut, le navigateur bloque ces requêtes "cross-origin"
# pour des raisons de sécurité.
#
# SOLUTION :
# On autorise explicitement localhost:3000 à appeler notre API.
# En production, on remplacera par : 'https://monbut.com'
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Adresse du frontend React en développement
]


# ─────────────────────────────────────────────────────────
# APPLICATIONS INSTALLÉES
# ─────────────────────────────────────────────────────────

# Liste de TOUTES les applications actives dans le projet Django.
#
# ⚠️ RÈGLE FONDAMENTALE :
# Django ne connaît une application que si elle est listée ici.
# Une app absente de INSTALLED_APPS = une app inexistante pour Django.
# Ses modèles ne seront pas migrés, ses URLs ignorées, etc.
INSTALLED_APPS = [

    # ── Applications Django intégrées (présentes par défaut) ──

    # Fournit le panneau d'administration automatique de Django.
    # Accessible sur : http://127.0.0.1:8000/admin/
    # Permet de gérer visuellement les utilisateurs, offres,
    # candidatures sans écrire une seule ligne de code d'interface.
    'django.contrib.admin',

    # Fournit le système d'authentification intégré de Django :
    # - Gestion des utilisateurs (création, modification, suppression)
    # - Hashage sécurisé des mots de passe
    # - Système de permissions et de groupes
    # - Sessions de connexion/déconnexion
    'django.contrib.auth',

    # Permet à Django de travailler avec différents types de modèles
    # de manière générique. Utilisé en interne par Django et l'admin.
    # On ne l'utilise pas directement mais il est indispensable.
    'django.contrib.contenttypes',

    # Gestion des sessions utilisateurs.
    # Une session permet de "mémoriser" un utilisateur
    # entre plusieurs requêtes HTTP successives.
    'django.contrib.sessions',

    # Système de messages flash — notifications temporaires
    # affichées une seule fois après une action.
    # Exemple : "Votre profil a été mis à jour avec succès."
    'django.contrib.messages',

    # Gestion des fichiers statiques : CSS, JavaScript, images.
    # En développement, Django les sert directement.
    # En production, c'est Nginx ou un CDN qui s'en charge.
    # Dans notre API REST, c'est surtout utile pour l'interface admin.
    'django.contrib.staticfiles',

    # ── Packages tiers installés par nous ──

    # Active Django REST Framework (DRF) dans le projet.
    # Sans cette ligne, DRF est installé mais complètement ignoré.
    # C'est lui qui nous permet de créer des endpoints API REST
    # et de renvoyer du JSON au lieu de pages HTML.
    'rest_framework',

    # Active l'authentification par JWT (JSON Web Tokens).
    # Fournit les mécanismes de génération et validation
    # des tokens d'accès et de rafraîchissement pour MonBut.
    'rest_framework_simplejwt',

    # Active la gestion des requêtes cross-origin (CORS).
    # Permet au frontend React (port 3000) de communiquer
    # avec notre backend Django (port 8000) sans être bloqué
    # par la politique de sécurité du navigateur.
    'corsheaders',

    'accounts',     # Notre app de gestion des utilisateurs
]


# ─────────────────────────────────────────────────────────
# MIDDLEWARES
# ─────────────────────────────────────────────────────────

# Les middlewares sont des couches de traitement intermédiaires.
# Chaque requête HTTP reçue traverse TOUS les middlewares
# de haut en bas AVANT d'arriver à l'endpoint (vue).
# Chaque réponse retraverse tous les middlewares
# de bas en haut AVANT d'être envoyée au client.
#
# SCHÉMA DU FLUX D'UNE REQUÊTE :
#
# Postman/React envoie une requête
#        ↓
# CorsMiddleware        → vérifie si l'origine est autorisée
#        ↓
# SecurityMiddleware    → vérifie la sécurité HTTPS
#        ↓
# SessionMiddleware     → lit le cookie de session
#        ↓
# CommonMiddleware      → normalise l'URL
#        ↓
# CsrfViewMiddleware    → vérifie le token CSRF
#        ↓
# AuthenticationMiddleware → identifie l'utilisateur
#        ↓
# MessageMiddleware     → gère les messages flash
#        ↓
# XFrameOptionsMiddleware → protection clickjacking
#        ↓
# Vue (endpoint) → traite la requête et renvoie une réponse
MIDDLEWARE = [

    # ⚠️ DOIT ÊTRE EN PREMIER dans la liste.
    # Ajoute les headers CORS à chaque réponse HTTP pour autoriser
    # les requêtes venant du frontend React.
    # S'il n'est pas en premier, il ne peut pas intercepter
    # les réponses avant les autres middlewares.
    'corsheaders.middleware.CorsMiddleware',

    # Gère la sécurité HTTPS :
    # - Redirige HTTP vers HTTPS en production
    # - Ajoute des headers de sécurité (HSTS, etc.)
    'django.middleware.security.SecurityMiddleware',

    # Gère les sessions utilisateurs :
    # - Lit le cookie de session dans la requête entrante
    # - Écrit le cookie de session dans la réponse sortante
    'django.contrib.sessions.middleware.SessionMiddleware',

    # Normalise les URLs :
    # - Ajoute un slash final si nécessaire (/api/jobs → /api/jobs/)
    # - Gère les redirections communes
    'django.middleware.common.CommonMiddleware',

    # Protection CSRF (Cross-Site Request Forgery) :
    # Vérifie un token secret dans les requêtes POST, PUT, DELETE
    # pour empêcher les attaques où un site malveillant enverrait
    # des requêtes à notre API en se faisant passer pour l'utilisateur.
    # Note : avec JWT, cette protection est moins critique car
    # le token JWT joue déjà ce rôle de vérification.
    'django.middleware.csrf.CsrfViewMiddleware',

    # Identifie l'utilisateur connecté à partir de la session
    # et l'attache à l'objet request sous request.user.
    # Dans nos vues, on pourra faire : request.user.email
    # pour connaître l'utilisateur qui fait la requête.
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Gère les messages flash entre les requêtes.
    # Stocke temporairement les notifications (succès, erreur)
    # pour les afficher à l'utilisateur à la prochaine requête.
    'django.contrib.messages.middleware.MessageMiddleware',

    # Protection contre le clickjacking :
    # Empêche l'affichage de notre site dans un iframe
    # sur un autre site malveillant.
    # Ajoute le header X-Frame-Options: DENY à chaque réponse.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ─────────────────────────────────────────────────────────
# URLS
# ─────────────────────────────────────────────────────────

# Indique à Django quel fichier contient les URLs principales du projet.
# 'core.urls' = le fichier urls.py dans le dossier core/
# C'est le point d'entrée de tout le système de routage de MonBut.
# Django commencera toujours par chercher les URLs dans ce fichier.
ROOT_URLCONF = 'core.urls'


# ─────────────────────────────────────────────────────────
# TEMPLATES (GABARITS HTML)
# ─────────────────────────────────────────────────────────

# Configuration du moteur de templates HTML de Django.
# Dans MonBut (API REST pure), on n'utilise pas les templates
# car on renvoie du JSON et non du HTML.
# Django en a quand même besoin pour son interface d'administration.
TEMPLATES = [
    {
        # Le moteur de templates utilisé.
        # 'DjangoTemplates' = le moteur intégré de Django.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Dossiers supplémentaires où chercher les templates HTML.
        # [] = vide car on n'a pas de templates personnalisés.
        'DIRS': [],

        # True = Django cherche automatiquement les templates
        # dans un sous-dossier 'templates/' de chaque application.
        'APP_DIRS': True,

        'OPTIONS': {
            # Processeurs de contexte :
            # fonctions appelées automatiquement sur chaque requête
            # qui ajoutent des variables utiles à tous les templates.
            'context_processors': [

                # Ajoute l'objet 'request' (la requête HTTP en cours)
                # à tous les templates. Utile pour accéder aux données
                # de la requête directement dans les templates.
                'django.template.context_processors.request',

                # Ajoute les informations d'authentification à tous
                # les templates : l'utilisateur connecté (user)
                # et ses permissions (perms).
                'django.contrib.auth.context_processors.auth',

                # Ajoute les messages flash à tous les templates
                # pour qu'ils puissent être affichés à l'utilisateur.
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Point d'entrée WSGI pour déployer Django sur un serveur en production.
# WSGI = Web Server Gateway Interface — interface standard entre
# Python et les serveurs web (Nginx, Apache, Gunicorn).
# 'core.wsgi.application' pointe vers le fichier core/wsgi.py
# qui est généré automatiquement par Django.
WSGI_APPLICATION = 'core.wsgi.application'


# ─────────────────────────────────────────────────────────
# BASE DE DONNÉES
# ─────────────────────────────────────────────────────────

DATABASES = {
    # 'default' = nom de la connexion à la base de données principale.
    # Django supporte plusieurs bases de données simultanément,
    # mais on en utilise une seule pour MonBut.
    'default': {

        # Le moteur (système de gestion) de base de données utilisé.
        # 'sqlite3' = base de données stockée dans un simple fichier.
        # ✅ Avantages en développement :
        #    - Aucune installation requise
        #    - Fichier unique facile à supprimer/recréer
        #    - Parfait pour tester
        # ❌ Inconvénients en production :
        #    - Pas adapté à plusieurs utilisateurs simultanés
        #    - Pas de performances pour une vraie application
        #
        # En production (Railway), on utilisera PostgreSQL :
        # 'ENGINE': 'django.db.backends.postgresql'
        'ENGINE': 'django.db.backends.sqlite3',

        # Chemin complet vers le fichier de base de données SQLite.
        # BASE_DIR / 'db.sqlite3' = monbut-api/db.sqlite3
        # Ce fichier est créé automatiquement par Django
        # lors de la première commande 'python manage.py migrate'.
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ─────────────────────────────────────────────────────────
# VALIDATION DES MOTS DE PASSE
# ─────────────────────────────────────────────────────────

# Liste des règles de validation appliquées aux mots de passe.
# Django vérifie automatiquement toutes ces règles lors de
# la création ou du changement d'un mot de passe utilisateur.
# Si une règle n'est pas respectée, Django renvoie une erreur claire.
AUTH_PASSWORD_VALIDATORS = [

    # Règle 1 : le mot de passe ne doit pas être trop similaire
    # aux informations personnelles de l'utilisateur
    # (prénom, nom, email, nom d'utilisateur).
    # Exemple refusé : email = "ousmane@gmail.com", mdp = "ousmane123"
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    # Règle 2 : le mot de passe doit avoir une longueur minimale.
    # Par défaut : 8 caractères minimum.
    # Exemple refusé : "abc123" (6 caractères seulement)
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    # Règle 3 : le mot de passe ne doit pas être un mot de passe
    # trop commun. Django possède une liste de 20 000 mots de passe
    # courants à éviter.
    # Exemples refusés : "password", "123456789", "qwerty"
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    # Règle 4 : le mot de passe ne doit pas être entièrement numérique.
    # Un mot de passe 100% composé de chiffres est trop facile à deviner.
    # Exemple refusé : "12345678" (que des chiffres)
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ─────────────────────────────────────────────────────────
# INTERNATIONALISATION
# ─────────────────────────────────────────────────────────

# Langue par défaut de l'interface d'administration Django.
# 'en-us' = anglais américain.
# On pourrait mettre 'fr-fr' pour avoir l'admin en français.
LANGUAGE_CODE = 'en-us'

# Fuseau horaire utilisé par Django pour afficher les dates et heures.
# 'UTC' = temps universel coordonné (référence mondiale).
# La Guinée est en UTC+0, donc 'UTC' ou 'Africa/Conakry' donnent
# le même résultat pour MonBut.
TIME_ZONE = 'UTC'

# Active le système de traduction internationale (i18n = internationalization).
# True = Django peut afficher l'interface dans différentes langues
# selon la préférence de l'utilisateur.
USE_I18N = True

# Active la gestion des fuseaux horaires.
# True = Django stocke TOUTES les dates en UTC dans la base de données
# et les convertit dans le bon fuseau horaire au moment de l'affichage.
# C'est la bonne pratique pour une application utilisée
# dans plusieurs pays (perspective d'évolution de MonBut).
USE_TZ = True


# ─────────────────────────────────────────────────────────
# FICHIERS STATIQUES
# ─────────────────────────────────────────────────────────

# URL de base pour accéder aux fichiers statiques (CSS, JS, images).
# 'static/' signifie que les fichiers statiques seront accessibles
# sur : http://127.0.0.1:8000/static/nom-du-fichier.css
# Dans une API REST pure comme MonBut, cette configuration
# est surtout utile pour l'interface d'administration Django.
STATIC_URL = 'static/'


# ─────────────────────────────────────────────────────────
# CONFIGURATION DJANGO REST FRAMEWORK
# (ajoutée manuellement par nous — absente par défaut)
# ─────────────────────────────────────────────────────────

REST_FRAMEWORK = {

    # DEFAULT_AUTHENTICATION_CLASSES :
    # Définit COMMENT DRF vérifie l'identité de l'utilisateur
    # qui envoie une requête à l'API.
    #
    # JWTAuthentication = DRF cherche un token JWT dans le header
    # Authorization de chaque requête entrante :
    # Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    #
    # ✅ Token valide   → utilisateur identifié, requête autorisée
    # ❌ Token absent   → requête refusée (erreur 401 Unauthorized)
    # ❌ Token invalide → requête refusée (erreur 401 Unauthorized)
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # DEFAULT_PERMISSION_CLASSES :
    # Définit QUI a le droit d'accéder aux endpoints de l'API.
    #
    # IsAuthenticated = par défaut, seuls les utilisateurs possédant
    # un token JWT valide peuvent accéder aux endpoints.
    # C'est la règle de sécurité de base de MonBut :
    # un anonyme ne peut rien faire sur la plateforme.
    #
    # Les endpoints publics seront ouverts explicitement
    # avec 'AllowAny' directement dans leurs vues :
    # - POST /api/auth/register/ (inscription)
    # - POST /api/auth/login/    (connexion)
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


AUTH_USER_MODEL = 'accounts.User'