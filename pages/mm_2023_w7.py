import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import itertools
from dash_breakpoints import WindowBreakpoints
import dash_mantine_components as dmc
import dash
from dash import html, dcc, Dash, Input, Output
from dash_iconify import DashIconify

dash.register_page(__name__, path='/mm_2023_w7') 


text = """Brands	Q1 2021	Q2 2021	Q3 2021	Q4 2021	Q1 2022	Q2 2022	Q3 2022	Q4 2022
BYD Auto	5 	7 	11 	12 	14 	16 	20 	20 
Tesla	17 	15 	15 	14 	15 	12 	13 	12 
Volkswagen	5 	7 	6 	5 	4 	4 	4 	4 
Wuling	9 	7 	6 	5 	5 	5 	5 	4 
BMW	6 	5 	4 	4 	4 	4 	3 	4 
Others	58 	59 	58 	60 	58 	59 	55 	56 """

data = [i.split('\t') for i in text.split("\n")]
df = pd.DataFrame(data[1:], columns=data[0])
to_join = df.iloc[:,1:].astype('float')
df = pd.concat([df['Brands'],to_join], axis=1)

final = pd.DataFrame(df.Brands)

for i, col in enumerate(['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022','Q2 2022', 'Q3 2022', 'Q4 2022']):
    ch1 = df.loc[:, ['Brands', col]]
    ch1.sort_values(col, inplace=True)
    ch1[f'y{i}_upper'] = ch1[col].cumsum()
    ch1[f'y{i}_lower'] = ch1[f'y{i}_upper'].shift(1)
    ch1 = ch1.fillna(0)
    ch1[f'y{i}'] = ch1.apply(lambda x: (x[f'y{i}_upper']+x[f'y{i}_lower'])/2, axis=1)
    final = final.merge(ch1.iloc[:, [0, 2, 3, 4]], on='Brands')
    
def getupperlower(brand):
    ch1 = final.query('Brands == @brand')
    upper_col = [i for i in ch1.columns if 'upper' in i]
    lower_col = [i for i in ch1.columns if 'lower' in i]
    upper_data = ch1[upper_col].values.tolist()[0]
    lower_data = ch1[lower_col].values.tolist()[0]
    annotate_place = ch1['y0'].values.tolist()[0]
    return upper_data, lower_data, annotate_place

def get_val(x,sub=0.1, axis='x'):
    if axis != 'x':
        a = [[i, i]for i in x]
    else:
        a = [[i-sub, i+sub ]for i in x]
    return list(itertools.chain.from_iterable(a))

colors={'BYD Auto':'#72c6e8', 'Tesla':'#E41A37', 'Wuling':'#5c606d', 'Volkswagen':'#12618F', 'BMW':'#d9871b', 'Others':'rgba(0,0,0,0.1)'}
colors2 =[i for i in colors.values()]


backcolor = "#ECF9FF"
containercolor= "#f1faee"
paper_color = "#a8dadc"
card_headline = "#1d3557"
cart_text_size = 35
name_size = 30
tilecolor = "#e63946"
selectcolor = "#457b9d"
mmw7_2033_layout = dmc.Container(children=[
    dmc.Stack([
        dmc.Paper(
            dmc.Group(children=[
                dmc.Text(['MakeOver Monday W10, 2023'], align='center', color='#033546', weight=700),
                dmc.Group(children=[
                      dmc.Text(['Created By ', dmc.Anchor("Abhinav Kumar",href="http://www.linkedin.com/in/abhinavk910",
                                        target="_blank", style={'text-decoration': 'none', 'color':selectcolor})
                      ], align='center', color=paper_color, weight=700),  
                    html.A(
                        dmc.Avatar(src='/assets/header.jpg',
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
            ], id='heading-group-mm7-2023', position='apart'),
            
            p=10, px=20, mt=10, radius=10,shadow="md",mx=2, id='heading-paper-mm7-2023', style={"background-color": containercolor}
        ),
        dmc.Paper(
            children=[
                    dmc.Grid(
                        children=[
                            dmc.Col(
                                children=[
                                    dmc.LoadingOverlay(
                                    dcc.Graph(id='figure_mm7_2023'),  
                                    )
                                ])
                        ],align="flex-end")  
            ],className="",
             p=20, mb=1, radius=10,shadow="md",mx=2, id='graph-paper-mm7-2023', style={"background-color": paper_color}
        ),
        dmc.Paper(children=[
            dmc.Group([
                dmc.Text(["Data Source : ",
                          dmc.Anchor(
                            "Counterpoint Research",
                              href="https://www.counterpointresearch.com/global-electric-vehicle-market-share/",
                              underline=False, target="_blank",
                        )], size=10),
            ])
        ],p=10, px=20, mb=10, radius=10,shadow="sm",mx=2, id='source-paper-mm7-2023', style={"background-color": containercolor}
        )
    ], style={'overflow-x': 'auto', 'max-width':'900px',  'margin':'auto'})
], size='auto',m=0,p=20,id='outer-mm7-2023', className='min-vh-100 mx-sm-0 mx-md-auto d-flex justify-content-center align-items-center', 
             style={"background-color": backcolor})

layout = dmc.MantineProvider(
        theme={
            'fontFamily': '"Inter", sans-serif',
            },
        inherit=True,
        withGlobalStyles=True,
        withNormalizeCSS=True,
        
        children=[mmw7_2033_layout,
                  WindowBreakpoints(
                    id="breakpoints_mm7",
                    widthBreakpointThresholdsPx=[766],
                    widthBreakpointNames=["sm", "md"],
                )])

dash.clientside_callback(
    """
    function(widthBreakpoint) {
        if (widthBreakpoint === "sm") {
            return [0, 0,10,10,10,10, 'center'];
        } else {
            return [20, 0, 20,20,20,0, 'apart'];
        }
    };
    """,
    Output('outer-mm7-2023', 'p'),
    Output('outer-mm7-2023', 'm'),
    Output('graph-paper-mm7-2023', 'p'),
    Output('source-paper-mm7-2023', 'px'),
    Output('heading-paper-mm7-2023', 'px'),
    Output('heading-paper-mm7-2023', 'mt'),
    Output('heading-group-mm7-2023', 'position'),
    Input("breakpoints_mm7", "widthBreakpoint"),
    prevent_initial_call=True
)

@dash.callback(
    Output('figure_mm7_2023','figure'),
    Input("breakpoints_mm7", "widthBreakpoint")
)
def update_fig(bp):
    if bp == 'sm':
        title = 'Electric Vehicle Market Share'
        l = 50
        r = 0
        b = 30
        annot_size=8
    else:
        title = 'Global Passenger Electric Vehicle Market Share, Q1 2021 - Q4 2022'
        l = 100
        r = 100
        b = 10
        annot_size=14
    
    fig = go.Figure()

    x = (np.arange(df.shape[1]-1)+1).tolist()
    x = get_val(x, sub=0.15)
    x_rev = x[::-1]

    annotations = []

    for i, brand in enumerate(df.Brands):

        upper_col, lower_col, annotate_place = getupperlower(brand)
        y_upper = get_val(upper_col, axis='y')
        y_lower = get_val(lower_col, axis='y')
        y_lower = y_lower[::-1]
        fig.add_trace(go.Scatter(
            x=x+[x[-1]+1, x[-1]+1]+x_rev,
            y=y_upper+[y_upper[-1], y_lower[0]]+y_lower,
            fill='toself',
            fillcolor=colors2[i],
            opacity=0.5,
            line_color='rgba(0,0,0,0.2)',
            showlegend=False,
            name=brand,
            line_shape='spline',
            mode='lines',
    #         marker=dict(size=20),
            hovertemplate=' '
        ))
        annotations.append(dict(xref='paper', yref='y',
                                x=-0.005, y=annotate_place,
                                text=brand,align="right",xanchor='right',
                                font=dict(family='sans-serif', size=annot_size,
                                          color=colors2[i]),
                                showarrow=False))




    ch1 = df.set_index('Brands')
    for i,j in enumerate(['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022']):

        ch2 = pd.DataFrame(ch1.T.iloc[i])
        ch2.columns = [i+1]
        ch2.sort_values(i+1, ascending=True, inplace=True)
        fig_px = px.bar(ch2.T,  color_discrete_map=colors, opacity=0.7, text_auto=True)
        fig_px.update_traces(hovertemplate='<b>%{x}</b>, %{value}%')
        fig_px.update_traces(textfont=dict(size=9,color='black'), textposition='auto', cliponaxis=False, texttemplate='%{value}%')
        for trace in fig_px['data']:
            fig.add_trace(trace)





    fig.update_layout(barmode='stack',  bargap=0.7,showlegend=False)

    fig.update_layout(plot_bgcolor='#f2f3f4', paper_bgcolor='#f2f3f4', margin=dict(t=100, l=l,b=b, r=r,pad=0))
    fig.update_xaxes(range=[0.85,8.15],tickmode = 'array',showticklabels=True,
                ticktext = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 'Q1 2022','Q2 2022', 'Q3 2022', 'Q4 2022'],
                tickvals = [1, 2, 3, 4, 5, 6,7,8],fixedrange=True, tickfont=dict(size=annot_size,family='sans-serif',))
    fig.update_yaxes(range=[0,101],showticklabels=False, showgrid=False, fixedrange=True, zeroline=False)
    fig.update_layout(annotations=annotations)
    fig.update_layout(title=title, font_family='sans-serif',)

    
    return fig