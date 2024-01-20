#imports
from .common import *
from .components import *

#page register
dash.register_page(__name__, path='/thetailend') 


#userful function
def total_life_span(upto, age):
    x = np.arange(1, 11, 1)
    y = np.arange(1, 11, 1)

    x, y = np.meshgrid(x, y)

    x, y = x.reshape(-1), y.reshape(-1)

    x, y = x[:upto], y[:upto]
    color = ['completed']*age+['remaining']*(upto-age)\
    
    fig = px.scatter(x=x, y=y, color=color, color_discrete_map={'completed':'red', 'remaining':'green'})
    fig.add_shape(type="line",
        x0=1, y0=0, x1=10, y1=0,
        line=dict(
            color="LightSeaGreen",
            width=4,
            dash="dashdot",
        )
    )
    fig.add_annotation(text="Each row is 10 years = 1 Decade",
                    xref="x", yref="y",
                    x=5, y=0.2, showarrow=False)
    fig.update_layout(showlegend=False, margin=dict(l=0, t=20, r=0, b=0, pad=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    hovermode=False)
    fig.update_traces(marker_size=15, marker_line_width=2, marker_symbol='diamond-open-dot')
    fig.update_yaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, autorange='reversed', title="")
    fig.update_xaxes(showgrid=False, fixedrange=True,showticklabels=False, zeroline=False, title="")
    return fig

def total_month_span(upto, age):
    x = np.arange(1, 37, 1)
    y = np.arange(1, math.ceil(upto/3)+1, 1)

    x, y = np.meshgrid(x, y)

    x, y = x.reshape(-1), y.reshape(-1)

    x, y = x[:upto*12], y[:upto*12]
    color = ['completed']*age*12+['remaining']*(upto-age)*12
    fig = px.scatter(x=x, y=y, color=color,
                 color_discrete_map={'completed':'red', 'remaining':'green'}
                 )
    fig.add_shape(type="line",
        x0=1, y0=-2, x1=36, y1=-2,
        line=dict(
            color="LightSeaGreen",
            width=4,
            dash="dashdot",
        )
    )
    fig.add_annotation(text="Each row is 36 months = 3 years",
                    xref="x", yref="y",
                    x=19, y=-1.5, showarrow=False)
    fig.update_layout(showlegend=False, margin=dict(l=0, t=20, r=0, b=0, pad=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    hovermode=False)
    fig.update_traces(marker_size=5, marker_symbol='circle-open', marker_line_width=2)
    fig.update_yaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, autorange='reversed', title="")
    fig.update_xaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, title="")
    return fig

def total_weeks_span(upto, age):
    x = np.arange(1, 113, 1)
    y = np.arange(1, math.ceil(upto/2)+1, 1)

    x, y = np.meshgrid(x, y)

    x, y = x.reshape(-1), y.reshape(-1)

    x, y = x[:upto*56], y[:upto*56]
    color = ['completed']*age*56+['remaining']*(upto-age)*56

    fig = px.scatter(x=x, y=y, color=color,
                 color_discrete_map={'completed':'red', 'remaining':'green'}
                 )
    fig.add_shape(type="line",
        x0=1, y0=-2, x1=112, y1=-2,
        line=dict(
            color="LightSeaGreen",
            width=4,
            dash="dashdot",
        )
    )
    fig.add_annotation(text="Each row is 112 weeks = 2 years",
                    xref="x", yref="y",
                    x=56, y=-1, showarrow=False)
    fig.update_layout(showlegend=False, margin=dict(l=0, t=20, r=0, b=0, pad=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    hovermode=False)
    fig.update_traces(marker_size=4, marker_symbol='circle-open-dot', marker_line_width=0.5)
    fig.update_yaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, autorange='reversed', title="")
    fig.update_xaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, title="")
    return fig

def total_days_span(upto, age):
    x = np.arange(1, 366, 1)
    y = np.arange(1, upto+1, 1)

    x, y = np.meshgrid(x, y)

    x, y = x.reshape(-1), y.reshape(-1)

    x, y = x[:upto*365], y[:upto*365]
    color = ['completed']*age*365+['remaining']*(upto-age)*365
    fig = px.scatter(x=x, y=y, color=color,
                 color_discrete_map={'completed':'red', 'remaining':'green'}
                 )
    fig.add_shape(type="line",
        x0=1, y0=-5, x1=365, y1=-5,
        line=dict(
            color="LightSeaGreen",
            width=4,
            dash="dashdot",
        )
    )
    fig.add_annotation(text="Each row is 365 days = 1 years",
                    xref="x", yref="y",
                    x=180, y=-3, showarrow=False)
    fig.update_layout(showlegend=False, margin=dict(l=0, t=20, r=0, b=0, pad=0),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    hovermode=False)
    fig.update_traces(marker_size=1, marker_symbol='circle-open-dot', marker_line_width=0.2)
    fig.update_yaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, autorange='reversed', title="")
    fig.update_xaxes(showgrid=False, fixedrange=True, showticklabels=False, zeroline=False, title="")
    return fig
#layout
layout = html.Div(
    style={'maxWidth':'1400px', 'margin':'auto'},
    children=[
        dmc.Container(
            fluid=True,
            children=[
                html.Div(id='check'),
                dmc.Grid(
                    m=20,
                    children=[
                        dmc.Col(
                            span=12,
                            md=6,
                            lg=3,
                            children=[
                                numberinput(id='age-no-input', label='Current Age?',value=25,min=10,
                                    max=100, step=1, licon='ant-design:number-outlined'),
                            ]
                        ),
                        dmc.Col(
                            span=12,
                            md=6,
                            lg=3,
                            children=[
                                numberinput(id='max-age-no-input',
                                    label='How Long you will Live(Years)?',
                                    value=85,min=10, max=100, step=1, licon='ant-design:number-outlined')
                            ]
                        ),
                    ]
                ),
                dmc.Grid(
                    children=[
                        dmc.Col(
                            span=12,
                            md=6,
                            m=0, p=0,
                            children=[
                                dmc.Container(
                                    fluid=True,
                                    m=0, p=0,
                                    children=[
                                        get_graph_skeleton(graph_id='total-years')
                                    ]
                                ),
                            ]
                        ),
                        dmc.Col(
                            span=12,
                            md=6,
                            m=0, p=0,
                            children=[
                                dmc.Container(
                                    fluid=True,
                                    m=0, p=0,
                                    children=[
                                        get_graph_skeleton(graph_id='total-months')
                                    ]
                                ),
                            ]
                        ),
                        dmc.Col(
                            span=12,
                            md=6,
                            m=0, p=0,
                            children=[
                                dmc.Container(
                                    fluid=True,
                                    m=0, p=0,
                                    children=[
                                        get_graph_skeleton(graph_id='total-weeks')
                                    ]
                                ),
                            ]
                        ),
                        dmc.Col(
                            span=12,
                            md=6,
                            m=0, p=0,
                            children=[
                                dmc.Container(
                                    fluid=True,
                                    m=1, p=1,
                                    children=[
                                        get_graph_skeleton(graph_id='total-days')
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

#total years
@dash.callback(
    Output('total-years-skeleton', 'visible'),
    Output('total-years', 'figure'),
    Input('age-no-input', 'value'),
    Input('max-age-no-input', 'value')
)
def update_total_years(age, upto):
    fig = total_life_span(upto, age)
    return False, fig

#total months
@dash.callback(
    Output('total-months-skeleton', 'visible'),
    Output('total-months', 'figure'),
    Input('age-no-input', 'value'),
    Input('max-age-no-input', 'value')
)
def update_total_months(age, upto):
    fig = total_month_span(upto, age)
    return False, fig

#total weeks
@dash.callback(
    Output('total-weeks-skeleton', 'visible'),
    Output('total-weeks', 'figure'),
    Input('age-no-input', 'value'),
    Input('max-age-no-input', 'value')
)
def update_total_weeks(age, upto):
    fig = total_weeks_span(upto, age)
    return False, fig

#total weeks
@dash.callback(
    Output('total-days-skeleton', 'visible'),
    Output('total-days', 'figure'),
    Input('age-no-input', 'value'),
    Input('max-age-no-input', 'value')
)
def update_total_weeks(age, upto):
    fig = total_days_span(upto, age)
    return False, fig