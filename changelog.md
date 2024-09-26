
- [26/09/2024](#26092024)
  - [Django 5.0](#django-50)
    - [Storages](#storages)
  - [Django REST Framework 3.15.2](#django-rest-framework-3152)
  - [Updated dependencies](#updated-dependencies)

# 26/09/2024

Major Update.

## Django 5.0
We updated Django to version 5.0. This update brings new features and improvements to the project.

### Storages
Some settings were updated to use the new storages configuration.
Now we have:
```python	
# Default STORAGES from Django documentation
# See:
# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}
```

## Django REST Framework 3.15.2
We updated Django REST Framework to version 3.15.2. 
It solves some issues with the collect static command.

## Updated dependencies
Django==5.0
boto3==1.35.28
django-simple-history==3.7.0
djangorestframework==3.15.2
model-bakery==1.19.5

