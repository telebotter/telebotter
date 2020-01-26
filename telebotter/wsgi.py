"""
WSGI config for telebotter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telebotter.settings")
logger = logging.getLogger(__name__)  # not available yet?
logger.error('wsgi gestartet')

#try:
#    logger.error('creating application')
application = get_wsgi_application()
#    logger.error('application created')
#except Exception as e:
#    logger.exception(e)
