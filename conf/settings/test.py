import os
from .common import *  # noqa

# Storages

MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp/media')  # noqa


# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/mailbox')  # noqa
