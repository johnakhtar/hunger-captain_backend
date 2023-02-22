import os
import pytz

#config

STATUS=(
    ('active','Active'),
    ('inactive','Inactive'),
    ('disabled','Disabled')
)
STATUS_DICT =dict(STATUS)

CATEGORIES =(
    ('hot','Hot'),
    ('cold','Cold'),
    ('bagel','Bagel')
)
CATEGORIES_DICT=dict(CATEGORIES)