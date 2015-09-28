
###
#
# Static File Settings
#
###

import os
from mainsite import TOP_DIR


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(TOP_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'static'),
]
