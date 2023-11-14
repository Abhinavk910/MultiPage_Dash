from ..common import *
from .layout import *
from pages.BSE.callback import *

register_page(__name__, path='/BSE', layout=create_layout())

register_callbacks()