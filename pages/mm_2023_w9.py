import dash_mantine_components as dmc
import dash
from dash import html, dcc, Dash, Input, Output
import pandas as pd
import plotly.express as px
from dash_iconify import DashIconify
import numpy as np

dash.register_page(__name__, path='/mm_2023_w9') 

text = """Chain	Product	caffeine_mg	drink_size_ml
Caffe Nero	Single-shot Espresso	45	30
Caffe Nero	Cappuccino	115	355
Costa	Single-shot Espresso	100	30
Costa	Cappuccino	325	362
Greggs	Single-shot Espresso	75	28
Greggs	Cappuccino	197	341
Greggs	Filter/Brewed Coffee	225	341
Pret	Single-shot Espresso	180	30
Pret	Cappuccino	180	350
Pret	Filter/Brewed Coffee	271	350
Starbucks	Single-shot Espresso	33	25
Starbucks	Cappuccino	66	350
Starbucks	Filter/Brewed Coffee	102	350"""

data = [i.split('\t') for i in text.split("\n")]
df = pd.DataFrame(data[1:], columns=data[0])
df['caffeine_mg'] = df.caffeine_mg.astype('float')
df['drink_size_ml'] = df.drink_size_ml.astype('float')
df['caffeine_normalize'] = df.apply(lambda x:x['caffeine_mg']/x['drink_size_ml'], axis=1)

product = df.Product.unique().tolist()


backcolor = "#ECF9FF"
containercolor= "#f1faee"
paper_color = "#a8dadc"
card_headline = "#1d3557"
cart_text_size = 35
name_size = 30
tilecolor = "#e63946"
selectcolor = "#457b9d"
layout = dmc.MantineProvider(
    theme={
            'fontFamily': '"Inter", sans-serif',
                'body'  : {
              'overflow-x': 'auto'
                }
            },
    children=[
        dmc.Container(children=[
            dmc.Stack([
                    dmc.Paper(
                        dmc.Group(children=[
                            dmc.Text(['MakeOver Monday W9, 2023'], align='center', color='#033546', weight=700),
                            dmc.Group(children=[
                                  dmc.Text(['Created By ', dmc.Anchor("Abhinav Kumar",href="http://www.linkedin.com/in/abhinavk910",
                                                    target="_blank", style={'text-decoration': 'none', 'color':selectcolor})
                                  ], align='center', color=paper_color, weight=700),  
                                html.A(
                                    dmc.Avatar(src='assets/image.jpg',
                                        size="xs",radius="lg"),
                                href="https://abhinavk910.github.io/portfolio/",
                                target="_blank",
                                ),
                                html.A(
                                    dmc.Avatar(DashIconify(icon="mdi:linkedin", width=15, color=paper_color),#'#0a66c2'
                                        size="xs",radius="xs"),
                                href="http://www.linkedin.com/in/abhinavk910",
                                target="_blank",
                                ),
                                html.A(
                                    dmc.Avatar(DashIconify(icon="mdi:github", width=15, color=paper_color),#'#24292f'
                                        size="xs",radius="xs"),
                                href="https://github.com/Abhinavk910/Data-Visualization/tree/main/apps/Makeover_Mondays",
                                target="_blank",
                                )
                            ], spacing='xs', position='right')
                        ], position='apart'),

                        p=10, px=20, mb=1, radius=30,shadow="md",mx=2, style={"background-color": containercolor}
                    ),
                    dmc.Paper(
                        children=[
                            dmc.Stack([
                                dmc.Container(
                                    fluid=True,
                                    children=[
                                        dmc.MediaQuery([
                                            dmc.Text("Are you drinking a safe amount of caffeine?", weight=500, size=30),
                                        ], smallerThan="sm", styles={'display': 'none'}),
                                        dmc.MediaQuery([
                                            dmc.Text("TOO MUCH CAFFEINE?", weight=500, size=40),
                                        ], largerThan="sm", styles={'display': 'none'}),
                                        
                                        
                                        dmc.Text("The U.S. FDA considers 400miligram(about 4 cup brewed \
                                              coffee) a safe amount of caffeine for healthy adults to consume daily",
                                                       color="dimmed", size=13)
                                    ], style={"backgroundColor": "#fff", 'width':"100%", 'boxSizing': 'border-box', 'padding':'10px'}
                                ),
                                dmc.Divider(variant="dashed",size=3),
                                dmc.Grid(
                                            gutter=0,
                                            justify="center",
                                            align="strech",
                                            children=[
                                                dmc.Col(
                                                    span=12,
                                                    md=9,
                                                    order=2,
                                                    orderMd=2,
                                                    children=[
                                                        dcc.Graph( id='figure_mm9_2023', config={'displayModeBar': False}),                                
                                                        ]
                                                ),
                                                dmc.Col(
                                                    span=12,
                                                    md=3,
                                                    order=1,
                                                    orderMd=2,
                                                    children=[
                                                        dmc.Container(
                                                            children=[
                                                                dmc.Text('DRINK OPTIONS', align='center',weight=600, style={'margin-bottom':'15px'}),
                                                                dmc.MediaQuery([
                                                                        dmc.Container(children=[dmc.Text("".join(['x' for i in range(190)]), size=1, align='center', style={'line-height':'1px'})],
                                                                                      fluid=True, style={'background-color':'black', 'margin':'20px' })
                                                                    ], smallerThan="md", styles={'display': 'none'}),
#                                                                 dmc.Divider(variant="dashed",size=4),
                                                                
                                                                
                                                                dmc.Grid(
                                                                    children=[
                                                                        dmc.Col(
                                                                            span=4,
                                                                            md=12,
                                                                            children=[
                                                                                dmc.Select(
                                                                                    label="DRINK TYPE",
                                                                                    placeholder="Select one",
                                                                                    id="drink_select_mm9_2023",
                                                                                    data=product,
                                                                                    value=product[1],
                                                                                    searchable=True,
                                                                                    nothingFound="No options found",
                                                                                    style={"marginBottom": 10},
                                                                                    icon=DashIconify(icon="mingcute:drink-line"),
                                                                                    size='xs'
                                                                                ),
                                                                            ]
                                                                        ),
                                                                        dmc.Col(
                                                                            span=4,
                                                                            md=12,
                                                                            children=[
                                                                                dmc.TextInput(
                                                                                    label='DRINK SIZE(ML)',
                                                                                    placeholder="350 ml",
                                                                                    id='size_mm9_2023',
                                                                                    icon=DashIconify(icon="fluent-mdl2:test-beaker-solid"),
                                                                                    size='xs',
                                                                                    type='number',
                                                                                    value=350,
                                                                                    style={"marginBottom": 10},
                                        
                                                                                ),
                                                                            ]
                                                                        ),
                                                                        dmc.Col(
                                                                            span=4,
                                                                            md=12,
                                                                            children=[
                                                                                dmc.TextInput(
                                                                                    label='DRINK PER DAY',
                                                                                    placeholder="Qty.",
                                                                                    value=2,
                                                                                    id='num_mm9_2023',
                                                                                    type='number',
                                                                                    icon=DashIconify(icon="mdi:counter"),
                                                                                    size='xs',
                                                                                    style={"marginBottom": 10},
                                                                                )
                                                                            ]
                                                                        )
                                                                    ]
                                                                ) 
                                                            ], style={'background-color':"#fff", 'height':'100%', 'padding':'20px', 'boxSizing': 'border-box' }
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                            ], spacing=0),    
                        ],className="",p=20, mb=1, radius=30,shadow="md",mx=2, style={"background-color": paper_color}
            #             shadow="md",style={'max-width':'900px', "background-color": containercolor, 'margin':'auto'},p=20, radius=30
                    ),
                    dmc.Paper(children=[
                        dmc.Group([
                            dmc.Text(["Data Source : ",
                                      dmc.Anchor(
                                        "Which?",
                                          href="https://www.which.co.uk/",
                                          underline=False, target="_blank",
                                    )], size=10),
                        ])
                    ],p=10, px=20, mb=10, radius=30,shadow="sm",mx=2, style={"background-color": containercolor}
                    )
                ], style={'overflow-x': 'auto', 'max-width':'900px', 'min-width':'600px', 'margin':'auto', 'boxSizing': 'border-box',})
            ], size='auto',m=0,p=20, className='min-vh-100 mx-sm-0 mx-md-auto d-flex justify-content-center align-items-center', 
             style={"background-color": backcolor, 'boxSizing': 'border-box',})

    ]
)



@dash.callback(
    Output('figure_mm9_2023', 'figure'),
    Input('drink_select_mm9_2023', 'value'),
    Input('size_mm9_2023', 'value'),
    Input('num_mm9_2023', 'value')
)
def update_graph(drink, size, num):
    
    select_size=int(size)
    select_product=drink
    select_cup=int(num)

    df2 = df.query('Product == @select_product').loc[:, ['Chain', 'caffeine_normalize']]
    df2['caffeine_normalize'] = round(df2.caffeine_normalize*select_cup*select_size)
    df2['color'] = np.where(df2.caffeine_normalize<400, 'lower', 'upper')

    colors={
        'lower': '#787d87',
        'upper': '#d16676',
    }
    df2.sort_values('caffeine_normalize', inplace=True)
    label = [f'<b><span style="font-size:25px;">{int(i)}</span></b> mg per day' for i in df2.caffeine_normalize]
    fig = px.bar(df2, x='caffeine_normalize', y='Chain', color='color',
           color_discrete_map=colors, text=label)

    fig.add_vline(x=400,
                  fillcolor="#667175", opacity=0.9,
                  layer="below", line_width=1,
                  line_color = 'black',
                  line_dash="dash",#'solid', 'dot', 'dash', 'longdash', 'dashdot','longdashdot'
                  annotation_text="400",
                  annotation_position="bottom right"
                 )

    fig.update_layout(showlegend=False,transition_duration=500,transition_easing='cubic',
                      plot_bgcolor='white', font=dict(family='sans-serif', size=15), hovermode=False,
                     margin=dict(t=10, r=10, b=10, l=10, pad=1))
    fig.update_traces(textfont=dict( family='sans-serif', size=13), textposition='auto', insidetextanchor='start')
    fig.update_xaxes(title="", showgrid=False, showticklabels=False)
    fig.update_yaxes(title="", showgrid=False, ticklen=7, ticks='outside', tickcolor='white', tickfont=dict(size=15))
    return fig
