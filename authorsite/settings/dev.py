from .base import *



# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
