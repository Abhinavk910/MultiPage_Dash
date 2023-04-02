import dash_mantine_components as dmc
from dash import html, dcc, Dash
import pandas as pd
import plotly.express as px
from dash_iconify import DashIconify
import numpy as np

dash.register_page(__name__, path='/mm_2023_w10')


text = """Year	Beef	Poultry	Pork
2000	100	100	100
2001	104.3	107.8	102.4
2002	101.2	112.1	103.4
2003	94.5	121.6	106.9
2004	97.6	133.3	108.8
2005	90.3	135.2	113.8
2006	92.4	134.3	118
2007	92	146.9	126.3
2008	93.2	163.3	129.9
2009	92.5	168.9	133.6
2010	93.8	180.8	139.4
2011	91.2	186.6	142.7
2012	89.4	187.1	139.2
2013	87.1	190.9	140
2014	89.2	200.1	140.6
2015	89.2	199.3	141.9
2016	90.3	200.1	142.3
2017	88.9	198.5	140.1
2018	86.7	205.9	136.1
2019	87.5	207.6	133.2
2020	85.4	211.5	130.3
2021	84.4	208.1	126.6
2022	77.5	202.1	114.2"""

data = [i.split('\t') for i in text.split("\n")]
df = pd.DataFrame(data[1:], columns=data[0])
df = df.melt(id_vars=['Year'], value_vars=['Beef', 'Poultry', 'Pork'], value_name='index_Vs_2000', var_name='Food')
df.dropna(inplace=True)
df['index_Vs_2000'] = df.index_Vs_2000.astype('float')
df['Year'] = df.Year.astype('int')


colors = {
    'Poultry': '#ef7b8b',
    'Pork': '#3e607a',
    'Beef': '#337fbc'
}

hover ='%{y:.0f}'


fig = px.line(df, x='Year', y='index_Vs_2000', color='Food',color_discrete_map=colors, line_shape='spline')

fig.update_traces(hovertemplate=hover)

fig.update_layout(showlegend=False, plot_bgcolor='white',paper_bgcolor='white', height=400,
                  hovermode="x",
                 margin={'l':10, 't':50, 'b':50, 'r':10, 'pad':0}, font={'color':'grey', 'size':7, 'family':'sans-serif'})

fig.update_xaxes(
    range=[1999, 2023],
    title="",
    ticks="outside",tickwidth=1.5,tickcolor='#AFA49C',ticklen=5,
    fixedrange=True,
    
)

fig.update_yaxes(
    range=[0, 220],
    title='Index vs. 2000',
    gridcolor='rgba(0,0,0,0.1)', gridwidth=1, zeroline=True, zerolinecolor = '#AFA49C', zerolinewidth = 2,
    fixedrange=True,

)

annotations = []
final_year = df[df.Year == 2022]
for food, val in zip(final_year.Food, final_year.index_Vs_2000):
    annotations.append(dict(xref='x', yref='y',
                            x=2022, y=val-15,
                            text=f'{food.upper()}<br>{int(val)}',
                            font=dict(family='sans-serif', size=10,
                                      color=colors[food]),
                            showarrow=False))

annotations.append(dict(xref='paper', yref='paper',
                            x=0, y=1.13,
                            text=f'Meat Production in Germany Fell Sharply in 2022',
                            font=dict(family='Inter', size=20,
                                      color='#3a3738'),
                            showarrow=False))
annotations.append(dict(xref='paper', yref='paper',
                            x=0, y=1.05,
                            text=f'Year on Year Decrease in pork and beef markedly larger than for poultry',
                            font=dict(family='Inter', size=12,
                                      color='#969093'),
                            showarrow=False))
annotations.append(dict(xref='paper', yref='paper',
                            x=1, y=-0.14,
                            text=f'Data Source: Statistisches Bundesamt (Destatis), 2023',
                            font=dict(family='Inter', size=10,
                                      color='#969093'),
                            showarrow=False))

fig.update_layout(annotations=annotations)



backcolor = "#ECF9FF"
containercolor= "#f1faee"
paper_color = "#a8dadc"
selectcolor = "#457b9d"

layout = dmc.MantineProvider(
        theme={
            'fontFamily': '"Inter", sans-serif',
            },
        children=[
			dmc.Container(children=[
			    dmc.Stack([
			        dmc.Paper(
			            dmc.Group(children=[
			                dmc.Text(['MakeOver Monday W10, 2023'], align='center', color='#033546', weight=700),
			                dmc.Group(children=[
			                      dmc.Text(['Created By ', dmc.Anchor("Abhinav Kumar",href="http://www.linkedin.com/in/abhinavk910",
			                                        target="_blank", style={'text-decoration': 'none', 'color':selectcolor})
			                      ], align='center', color=paper_color, weight=700),  
			                    html.A(
			                        dmc.Avatar(src='assets/header.jpg',
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
			                    href="https://github.com/Abhinavk910/Data-Visualization/blob/main/apps/Makeover_Mondays/year_2023/Week_10_germany_meat_production/app39.py",
			                    target="_blank",
			                    )
			                ], spacing='xs', position='right')
			            ], position='apart'),
			            
			            p=10, px=20, mb=1, radius=30,shadow="md",mx=2, style={"background-color": containercolor}
			        ),
			        dmc.Paper(
			            children=[
			                    dmc.Grid(
			                        children=[
			                            dmc.Col(
			                                children=[
			                                    dcc.Graph(figure=fig),                                
			                                ])
			                        ],align="flex-end")  
			            ],className="",
			             p=20, mb=1, radius=30,shadow="md",mx=2, style={"background-color": paper_color}
			        ),
			        dmc.Paper(children=[
			            dmc.Group([
			                dmc.Text(["Data Source : ",
			                          dmc.Anchor(
			                            "Statistisches Bundesamt (Destatis), 2023",
			                              href="https://www.destatis.de/EN/FactsFigures/EconomicSectors/AgricultureForestryFisheries/AnimalsAnimalProduction/Tables/2NumberOfSlaughteredAnimals.html",
			                              underline=False, target="_blank",
			                        )], size=10),
			                dmc.Text(["Article : ",
			                          dmc.Anchor(
			                            "Meat production in Germany",
			                              href="https://www.destatis.de/EN/Press/2023/02/PE23_051_413.html",
			                              underline=False, target="_blank",
			                        )], size=10),
			            ])
			        ],p=10, px=20, mb=10, radius=30,shadow="sm",mx=2, style={"background-color": containercolor}
			        )
			    ], style={'overflow-x': 'auto', 'width':'960px', 'min-width':'600px', 'margin':'auto'})
			], size='auto',m=0,p=20, className='min-vh-100 mx-sm-0 mx-md-auto d-flex justify-content-center align-items-center', 
			             style={"background-color": backcolor})

			])