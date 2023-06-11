

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 01:02:11 2023

@author: abhinav.kumar
"""

import dash_mantine_components as dmc
from dash import html,  dcc
from dash_iconify import DashIconify



layout_mc = html.Div(
    style={'backgroundColor':'#fff'},
    children=[
        dmc.Container(
            id='conpetition-setup-p8',
            style={'backgroundColor':'whitesmoke', 'minHeight':'100vh'},
            px=0,
            size='lg',
            children=[
                dcc.Interval(id='interval1-p8', interval=9*1000, n_intervals=0, max_intervals=1, disabled=False),
                dcc.Store(id='competition-data-p8', data={'contender-count':0, 'keys':{},    
                                                          'answered_question':0,
                                                          'current_question':1}, storage_type='local'),
                dmc.Stack(
                    id='hero',
                    align='center',
                    children=[
                        #one can also use dmc.header
                        dmc.Paper(
                            px=20,
                            p=10,
                            mt=0,
                            w='100%',
                            shadow="sm",
                            mx=-2,
                            style={"backgroundColor": '#f1faee'},
                            children=[
                                dmc.Group(
                                    position='apart',
                                    children=[
                                        dmc.Text( id='header-text-p8', align='center', color='', weight=700),
                                        dmc.Group(
                                            spacing='xs',
                                            position='right',
                                            children=[
                                                dmc.Text(
                                                    align='center',
                                                    color="#033546",
                                                    weight=700,
                                                    children=['Created By ',
                                                          dmc.Anchor("Abhinav Kumar",href="http://www.linkedin.com/in/abhinavk910",
                                                                target="_blank", style={'textDecoration': 'none', 'color':"#457b9d"})
                                                    ], 
                                                ),  
                                                html.A(dmc.Avatar(src='/assets/header.jpg',size="xs",radius="lg"),
                                                        href="https://abhinavk910.github.io/portfolio/",target="_blank",
                                                ),
                                                html.A(dmc.Avatar(DashIconify(icon="mdi:linkedin", width=15, color="#a8dadc"),
                                                    size="xs",radius="xs"), href="http://www.linkedin.com/in/abhinavk910", target="_blank",
                                                ),
                                                html.A(dmc.Avatar(DashIconify(icon="mdi:github", width=15, color="#a8dadc"),#'#24292f'
                                                       size="xs",radius="xs"), href="https://github.com/Abhinavk910/MultiPage_Dash/blob/main/pages/modelcompetition.py",
                                                       target="_blank",
                                                )
                                            ]
                                        )
                                    ]
                                ),
                            ]
                        ),
                        html.Div(
                            hidden=False,
                            id='html-div-to-hide',
                            style={'margin':'10px'},
                            children=[
                                html.H1(

                                    style={'fontSize':'4rem'},
                                    children=[
                                        'Model Competition',
                                        html.Span(className='start'),
                                        html.Span(className='reverse')
                                    ],
                                ),
                                html.H1(
                                    style={'fontSize':'.9rem', 'margin':'0px'},
                                    children=[
                                        'Director and Producer : Abhinav Kumar',
                                        html.Span(className='start'),
                                        html.Span(className='reverse')
                                    ],
                                )
                            ]
                        ),
                        html.Div(
                            id='html-div-to-hide2',
                            hidden=True,
                            style={'width':'95%'},
                            children=[
                                dmc.ActionIcon(DashIconify(icon='iconamoon:restart-fill'), id='back-to-start', style={'display':'none'}),
                                dmc.Center(
                                    style={'flexWrap':'wrap'},
                                    m=20,
                                    children=[
                                        dmc.Spoiler(
                                            showLabel="Show more",
                                            hideLabel="Hide",
                                            maxHeight=35,
                                            styles = {'root':{'fontSize':'10px'}},
                                            children=[
                                                dmc.Text(
                                                    style={"maxWidth": 600}, weight=400, size=11, mb=10,  color="dimmed",
                                                    children=[
                                                    """
                                                    Model Competition is an innovative application designed for comparing and evaluating LLM models.
                                                    With this application, users can engage in friendly competitions between two or more LLM models
                                                    to determine the most efficient and accurate model for a specific task. The process begins by
                                                    selecting the number of competitors or models to participate in the competition. Next, you have 
                                                    to ask series of questions or tasks and the models compete against each other to provide the 
                                                    quickest response time. The model that consistently delivers the fastest responses is declared 
                                                    the winner. Model Competition provides an interactive and dynamic platform for users to assess 
                                                    the performance of LLM models and make informed decisions based on their speed and efficiency.
                                                    """
                                                    ]
                                                ),

                                            ],
                                        ),
                                    ]
                                ),
                                dmc.Accordion(
                                    id='competition-accordion-p8',
                                    style={'display':''},
                                    mb=50,
                                    children=[
                                        dmc.AccordionItem(
                                            value='competition-setup',
                                            children=[
                                                dmc.AccordionControl('Competition Setup'),
                                                dmc.AccordionPanel(
                                                    children=[
                                                        dmc.NumberInput(
                                                            id='competitor-count-p8',
                                                            label='Competitors',
                                                            description='Number of Models to Compete',
                                                            min=2,
                                                            max=5,
                                                            step=1,
                                                            value=2,
                                                            icon=dmc.ActionIcon(DashIconify(icon='icon-park-outline:come'))
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                dmc.Text(id='check'),
                                                                dmc.Stack(
                                                                    id='competitor-selection-p8',
                                                                    mt=10,
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                dmc.Accordion(
                                    id='competition-accordion-api-p8',
                                    style={'display':''},
                                    children=[]
                                ),
                                html.Div(
                                    id='compete-page-p8',
                                    style={'padding':'10px'},
                                    hidden=True,
                                    children=[
                                        dmc.Group(
                                            spacing=5,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(icon='ep:back'),
                                                    id='back-question-p8',
                                                    variant='outline',
                                                    disabled=True
                                                ),
                                                dmc.ActionIcon(
                                                    DashIconify(icon='ep:back', flip='horizontal'),
                                                    id='next-question-arrow-p8',
                                                    variant='outline',
                                                    disabled=True
                                                )
                                            ]
                                        ),
                                        dmc.Textarea(
                                            id='question-input-p8',
                                            label='Ask Question',
                                            my=20,
                                        ),
                                        dmc.ActionIcon(
                                            DashIconify(icon='simple-icons:askubuntu', width=70),
                                            my=20,
                                            size='xl',
                                            mx='auto',
                                            variant='subtle',
                                            id='answer-output-p8'
                                        ),
                                        dmc.Center(
                                            dmc.Button("Next",
                                                       id='next-btn-p8',
                                                       leftIcon=DashIconify(icon='tabler:player-track-next'),
                                                       my=20,
                                                       style={'display':'none'},
                                                       variant="gradient"),
                                        ),
                                        dmc.Divider(variant="dashed", mb=20),
                                        dmc.Grid(
                                            id='competitor-card-p8',
                                            align='space_around',
                                            justify='center'
                                        ),
                                        dmc.Divider(variant="dashed", m=50),
                                        dmc.Alert(children=['Atleast ask one question.'],
                                                          id='no-question-asked-p8',
                                                          color='red',
                                                          hide=True,
                                                          duration=10000
                                        ),
                                        dmc.Center(
                                            style={'marginTop':'20px'},
                                            children=[

                                                dmc.Button("Download xlsx", id="btn-xslx-p8",
                                                       leftIcon=DashIconify(icon="material-symbols:download-rounded"),
                                                       style={'width':'200px', 'margin':'auto'}),
                                                dcc.Download(id="download-xslx-p8")
                                            ]   
                                        )
                                        
                                    ]
                                )
                            ]
                        )
                    ],
                )
            ]
        )
    ]
)
