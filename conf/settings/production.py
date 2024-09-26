from .common import *  # noqa


# Email settings

EMAIL_BACKEND = 'anymail.backends.amazon_ses.EmailBackend'
ANYMAIL = {
    'AMAZON_SES_CLIENT_PARAMS': {
        'aws_access_key_id': env.str('AWS_ACCESS_KEY_SES', ''),  # noqa
        'aws_secret_access_key': env.str('AWS_SECRET_KEY_SES', ''),  # noqa
        'region_name': env.str('AWS_REGION_NAME_SES', ''),  # noqa
    }
}
