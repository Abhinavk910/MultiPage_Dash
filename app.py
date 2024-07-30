
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash


app = Dash(__name__, 
           use_pages=True,
          #  external_scripts=['https://cdn.tailwindcss.com'],
           external_stylesheets=[dbc.icons.BOOTSTRAP, dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"}
             ],
            suppress_callback_exceptions=False
           )
server = app.server

app.layout = html.Div([
	dash.page_container, 
])

if __name__ == '__main__':
	app.run_server(debug=True, port=8053)
