from datetime import date, timedelta, datetime
import plotly.express as px
import pandas as pd
import numpy as np
import math
import yfinance as yf
import base64
import io
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import dash
from dash import Dash, Input, Output, State, register_page, callback, html, dcc, ALL, \
    clientside_callback, no_update, ctx
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate

import feffery_antd_components as fac
import feffery_utils_components as fuc

import pandas as pd
from datetime import datetime, date
import time

import os
from datetime import datetime
from icecream import ic
def time_format():
    return f'{datetime.now()}|> '
ic.configureOutput(includeContext=True, prefix=time_format())


from icecream import ic
def time_format():
    return f'{datetime.now()}|> '
ic.configureOutput(includeContext=True)


