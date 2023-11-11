from ..common import *
from .layout import *
from .callback import *

register_page(__name__, path='/BSE', layout=create_layout())

# register_callback()