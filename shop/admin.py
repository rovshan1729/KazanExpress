from django.contrib import admin
from django.apps import apps


app_models = apps.get_models()
for model in app_models:
    if not admin.site.is_registered(model):
        admin.site.register(model)
