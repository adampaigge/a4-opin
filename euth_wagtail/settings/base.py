"""
Django settings for euth_wagtail project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.wagtailstyleguide',

    'modelcluster',
    'taggit',
    'widget_tweaks',
    'webpack_loader',
    'easy_thumbnails',
    'parler',
    'ckeditor',
    'ckeditor_uploader',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'rest_framework',
    'autofixture',
    'rules.apps.AutodiscoverRulesConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'adhocracy4.images.apps.ImagesConfig',
    'adhocracy4.phases.apps.PhasesConfig',
    'adhocracy4.projects.apps.ProjectsConfig',
    'adhocracy4.ratings.apps.RatingsConfig',
    'adhocracy4.reports.apps.ReportConfig',
    'adhocracy4.modules.apps.ModulesConfig',

    'euth.users.apps.UsersConfig',
    'euth.actions.apps.ActionsConfig',
    'euth.organisations.apps.OrganisationsConfig',
    'euth.projects.apps.ProjectsConfig',
    'euth.comments.apps.CommentConfig',
    'euth.ideas.apps.IdeaConfig',
    'euth.dashboard.apps.DashboardConfig',
    'euth.memberships.apps.MembershipsConfig',
    'euth.documents.apps.DocumentConfig',
    'euth.flashpoll.apps.FlashpollConfig',
    'euth.maps.apps.MapConfig',
    'euth.follows.apps.FollowsConfig',
    'euth.offlinephases.apps.OfflinephaseConfig',
    'euth.contrib',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'euth_wagtail.urls'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'euth_wagtail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
}


# Auth
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/

AUTH_USER_MODEL = 'euth_users.User'

AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'image-editor': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    }
}

BLEACH_LIST = {
    'default' : {
        'tags': ['p','strong','em','u','ol','li','ul','a'],
        'attributes': {
            'a': ['href', 'rel'],
        },
    },
    'image-editor': {
        'tags': ['p','strong','em','u','ol','li','ul','a','img'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    ('it', _('Italien')),
    ('fr', _('French')),
    ('sv', _('Swedish')),
    ('sl', _('Slovene')),
    ('da', _('Danish')),
]

PARLER_LANGUAGES = {
    1:[{'code': language_code } for language_code, language in LANGUAGES]
}

# fixtures

FIXTURE_DIRS = [ os.path.join(PROJECT_DIR, 'fixtures') ]

IMAGE_ALIASES = {
    '*': {
        'max_size': 5*10**6,
        'fileformats': ('image/png', 'image/jpeg', 'image/gif')
    },
    'heroimage': {'min_resolution': (1300, 600)},
    'logo': {'min_resolution': (200, 200), 'aspect_ratio': (1, 1)},
    'avatar': {'min_resolution': (200, 200)},
    'idea_image': {'min_resolution': (800, 200)},
}

THUMBNAIL_ALIASES = {
    '': {
        'heroimage': {'size': (1500, 500), 'crop': 'smart'},
        'heroimage_preview': {'size': (880, 220), 'crop': 'smart'},
        'project_thumbnail': {'size': (520, 330), 'crop': 'smart'},
        'idea_image': {'size': (800, 0), 'crop': 'scale'},
        'idea_thumbnail': {'size': (240, 240), 'crop': 'smart'},
        'map_thumbnail': {'size': (400, 200), 'crop': 'smart'},
        'organisation_thumbnail': {'size': (740, 540), 'crop': 'smart'},
        'avatar_small': {'size': (60, 60), 'crop': 'smart'},
        'org_avatar_small': {'size': (60, 60), 'crop': 'scale'},
        'org_avatar_medium': {'size': (200, 200), 'crop': 'scale'},
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': '/static/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'node_modules/salvattore/dist'),
    os.path.join(BASE_DIR, 'node_modules/flatpickr/dist'),
    os.path.join(BASE_DIR, 'node_modules/leaflet/dist'),
    os.path.join(BASE_DIR, 'node_modules/leaflet-draw/dist'),
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_SUBJECT_PREFIX = '[OPIN] '

# Wagtail settings

WAGTAIL_SITE_NAME = "euth_wagtail"

# Authentification

LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_ADAPTER = 'euth.users.adapters.EuthAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = EMAIL_SUBJECT_PREFIX
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FORM_CLASS = 'euth.users.forms.SignUpForm'
ACCOUNT_USER_DISPLAY = 'euth.users.services.account_user_display'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # seconds
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_EMAIL_VERIFICATION = False

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# Euth settings

COMMENTABLES = (
    ('euth_ideas', 'idea'),
    ('euth_documents', 'paragraph'),
    ('euth_documents', 'document'),
    ('euth_comments', 'comment'),
)

A4_RATEABLES = (
    ('euth_ideas', 'idea'),
    ('euth_comments', 'comment'),
)

A4_REPORTABLES = (
    ('euth_ideas', 'ideas'),
    ('euth_comments', 'comment'),
)

ACTIONABLE = [
    ('euth_ideas', 'Idea'),
    ('euth_comments', 'Comment')
]

FLASHPOLL_URL = "https://opin.flashpoll.eu/"

BASE_MAP = 'https://{s}.tile.openstreetmap.org/'

MAP_BOUNDING_BOX = ('[[[34.95799531086792,-28.388671875],'
            '[71.35706654962706,-28.388671875],'
            '[71.35706654962706,50.88867187499999],'
            '[34.95799531086792,50.88867187499999],'
            '[34.95799531086792,-28.388671875]]]')

# Adhocracy4

A4_ORGANISATIONS_MODEL = 'euth_organisations.Organisation'
