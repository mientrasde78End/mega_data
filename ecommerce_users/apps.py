from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'ecommerce_users'

def ready(self):
    import ecommerce_users.signals