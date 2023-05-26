import yfinance as yf
import datetime
import pandas as pd
from dash import Input, Output, State, html, dcc, no_update, Patch, ctx, clientside_callback
import dash_mantine_components as dmc
import dash
import plotly.express as px
import time
import plotly.graph_objects as go

dash.register_page(__name__, path='/patch_test')

def get_stock_data(stock, date):
    start_date = date
    end_date = datetime.date.today().strftime('%Y-%m-%d')
    data = yf.download([stock], start=start_date, end=end_date)[['Close']]
    df = pd.date_range(start_date, end_date).to_frame()
    df=df.join(data)
    # df['Close'] = df.Close.interpolate(method='time')
    df['Close'] = df.Close.fillna(method = 'ffill')
    df['Close'] = df.Close.fillna(method = 'bfill')
    df.reset_index(drop=True, inplace=True)
    df.columns = ['ds', 'y']
    return df

df = get_stock_data('RELIANCE.NS', '2000-01-01')


layout=html.Div(
    style={'max-width':"1000px", 'margin':"20px", 'padding':"5px"},
    children=[
        dmc.Text("How Patch Perform, Let's check", size=30, weight=500),
        dmc.Grid(
            align='center',
            children=[
                dmc.Col(
                    span=6,
                    children=[
                        dmc.NumberInput(id='ninterval-input', value=1000, max=8000, label='Interval Start from', description='40 means plot start after 40 data points'),
                    ]
                ),
                dmc.Col(
                    span=6,
                    children=[
                        dmc.NumberInput(id='interval-input', value=3, label='Set Interval', description='1 means incrementality after 1 second'),
                    ]
                )
            ]
        ),
        dmc.Center(children=[dmc.Button(children=['Start/Stop'], id='start-btn')], mt=20),
        dcc.Interval(id='interval1', interval=3*1000, max_intervals=0),
#         dmc.Text('dffd'),
        dmc.Text(id='interval-text', mb=20),
        dmc.Grid(
            [dmc.Col(span=6, children=[dmc.Stack(align='center',children=[dmc.Text(id='graph1-time'),dcc.Graph(id='graph1')])]),
            dmc.Col(span=6, children=[dmc.Stack(align='center',children=[dmc.Text(id='graph2-time'), dcc.Graph(id='graph2')])])]
        )
    ]
)


clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output("start-btn", "loading", allow_duplicate=True),
    Input("start-btn", "n_clicks"),
    prevent_initial_call=True,
)

@dash.callback(
    Output('interval1', 'interval'),
    Output('interval1', 'n_intervals'),
    Output('interval1', 'max_intervals'),
    Output('start-btn', 'loading'),
    Input('start-btn', 'n_clicks'),
    State('ninterval-input', 'value'),
    State('interval-input', 'value'),
    State('interval1', 'max_intervals'),
    prevent_initial_call = True
)
def showit(n, nint, int_,  max_):
    if max_ == -1:
        return int_*1000, nint, 0, False
    else:
        return int_*1000, nint, -1, False

@dash.callback(
    Output('graph1', 'figure'),
    Output('graph1-time', 'children'),
    Input('interval1', 'n_intervals'),
    prevent_initial_call=True
)
def update(n):
    start = time.time()
    if n == 0:
        return no_update, no_update
    else:
        dff = df.iloc[:n]
        fig = px.line(dff, x='ds', y='y')
        fig.add_trace(go.Scatter(
                x=[ dff.iloc[-1]['ds']],
                y=[ dff.iloc[-1]['y']],
                mode='markers',
            )
        )
        first_date = df.iloc[0]['ds']
        latest_date = df.iloc[n]['ds']
        fig.update_xaxes(range=[first_date, latest_date+datetime.timedelta(days=90)])
        fig.update_layout(showlegend=False, plot_bgcolor='whitesmoke')
        end = time.time()
        render_time = end - start
        text = f"Patch OFF and Graph rendering time: {render_time:.4f} seconds"
        return fig, text
    
@dash.callback(
    Output('interval-text', 'children'),
    Output('graph2', 'figure'),
    Output('graph2-time', 'children'),
    Input('interval1', 'n_intervals'),
    State('ninterval-input', 'value'),
    prevent_initial_call=True
)
def update(n, nint):
    start = time.time()
    if n < nint+5:
        dff = df.iloc[:n]
        x_init = df.iloc[n]['ds']
        
        fig = px.line(dff, x='ds', y='y')
        fig.add_trace(go.Scatter(
                x=[ dff.iloc[-1]['ds']],
                y=[ dff.iloc[-1]['y']],
                mode='markers',
            )
        )
        first_date = df.iloc[0]['ds']
        latest_date = df.iloc[n]['ds']
        fig.update_xaxes(range=[first_date, latest_date+datetime.timedelta(days=90)])
        fig.update_layout(showlegend=False, plot_bgcolor='whitesmoke')
        end = time.time()
        render_time = end - start
        text = f"Patch OFF and Graph rendering time: {render_time:.4f} seconds"
        return f"Data Points - {n}", fig, text
    else:
#         return n, no_update
        
        y = df.iloc[n]['y']
        x = df.iloc[n]['ds']
        first_date = df.iloc[0]['ds']
        latest_date = df.iloc[n]['ds']
        patch_figure = Patch()
        patch_figure["data"][0]["x"].append(x)
        patch_figure["data"][0]["y"].append(y)
        patch_figure["data"][1]["x"]=[x]
        patch_figure["data"][1]["y"]=[y]
        patch_figure['layout']['xaxis']['range'].clear()
        patch_figure['layout']['xaxis']['range'].extend([first_date, latest_date+datetime.timedelta(days=90)])
        end = time.time()
        render_time = end - start
        text = f"Patch ON and Graph rendering time: {render_time:.4f} seconds"
        return f"Data Points - {n}", patch_figure, text
    
