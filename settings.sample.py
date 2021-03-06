# Webserver configuration #
###########################

# gunicorn config
bind = '127.0.0.1:5000'
errorlog = 'lintreview.error.log'
accesslog = 'lintreview.access.log'
debug = True
loglevel = 'debug'

# Basic flask config
DEBUG = True
TESTING = True
SERVER_NAME = '127.0.0.1:5000'

# Config file for logging
LOGGING_CONFIG = './logging.ini'


# Celery worker configuration #
###############################
from kombu import Exchange, Queue

# AMQP or other celery broker URL.
# amqp paths should be in the form of user:pass@host:port//virtualhost
BROKER_URL = 'amqp://'

# Use json for serializing messages.
CELERY_TASK_SERIALIZER = 'json'

# Show dates and times in UTC
CELERY_ENABLE_UTC = True

# Set the queues that celery will use.
CELERY_QUEUES = (
    Queue('lint', Exchange('lintreview'), routing_key='linty'),
)


# General project configuration #
#################################

# Path where project code should be
# checked out when reviews are done
# Repos will be checked out into $WORKSPACE/$user/$repo/$number
# directories to prevent collisions.
WORKSPACE = './workspace'

# Use GITHUB_URL when working with github:e
# When working with github:e don't forget to add the /api/v3/ path
GITHUB_URL = 'https://api.github.com/'

# Github username + password
# This is the user that lintreview will use
# to fetch repositories and leave review comments.
GITHUB_USER = 'octocat'
GITHUB_PASSWORD = ''

# Set to a path containing a custom CA bundle.
# This is useful when you have github:enterprise on an internal
# network with self-signed certificates.
SSL_CA_BUNDLE = None

# Delay publishing multiple comments by this value.
# Github:e will block lots of fast requests and return 500 errors.
PUBLISH_THROTTLE = 0
