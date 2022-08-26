from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="THISNTAGOOSSECRETKEY",
)

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "contato@bemlidos.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Bem Lidos"
