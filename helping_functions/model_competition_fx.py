
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 00:57:01 2023

@author: abhinav.kumar
"""

import dash_mantine_components as dmc
from dash_iconify import DashIconify
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.llms import AI21
from langchain.schema import HumanMessage
from langchain.llms import Replicate

model_data = [
        'OpenAI - gpt-3.5-turbo',
        'OpenAI - gpt-3.5-turbo-0301', 
        'OpenAI - text-davinci-003',
        'OpenAI - text-davinci-002',
        'AI21 - j1-large',
        'AI21 - j1-grande',
        'AI21 - j1-jumbo',
        'AI21 - j2-large',
        'AI21 - j2-grande',
        'AI21 - j2-grande-instruct',
        'AI21 - j2-jumbo',
        'AI21 - j2-jumbo-instruct',
        'Replicate - vicuna-13b',
        'Replicate - stability-ai/stablelm-tuned-alpha-7b',
        # 'Replicate - llama-7b',
        # 'Replicate - dolly-v2-12b',
        # 'Replicate - oasst-sft-1-pythia-12b',
        # 'Replicate - gpt-j-6b'
]


#helping Functions
def get_model_grid(i, id1, id2):
    """
    function create two single select dropdown
    one is for llm name , second is temp
    """
    return dmc.Grid(
        align='center',
        justify='space-around',
        style={'width':'90%'},
        mb=5,
        children=[
            dmc.Col(
                span=6,
                sm=4,
                children=[
                    dmc.Select(
                        id=id1,
                        label='Models',
                        description='Select atleast one',
                        data=model_data,
                        searchable=True,
                        required=True,
                        persistence=id1,
                        persistence_type='session'
                    )
                ]
            ),
            dmc.Col(
                span=6,
                sm=4,
                children=[
                    dmc.NumberInput(
                        id=id2,
                        label="Temperature",
                        description='Setting temperature to 0 will make the outputs mostly deterministic',
                        value=0.5,
                        precision=1,
                        min=0,
                        step=0.1,
                        max=1,
                    ) 
                ]
            )
        ]
    )
        
        
def create_acccordion_item(value, control_name, password_id, button_id, alert1_id, alert2_id, api_description=''):
    return dmc.AccordionItem(
                value=value,
                children=[
                    dmc.AccordionControl(control_name),
                    dmc.AccordionPanel(
                        children=[
                            dmc.Grid(
                                align='center',
                                children=[
                                    dmc.Col(
                                        span=12,
                                        sm=6,
                                        children=[
                                            dmc.PasswordInput(
                                                id=password_id,
                                                label="API Key",
                                                description=api_description,
                                                placeholder="Your Key",
                                                # style={"width": 250},
                                                icon=DashIconify(icon="material-symbols:key-outline"),
                                            ),
                                        ]
                                    ),
                                    dmc.Col(
                                        span=12,
                                        sm=6,
                                        children=[
                                            dmc.Center(
                                                mt=14,
                                                children=[
                                                    dmc.Button('Register',
                                                        id=button_id,
                                                        variant='gradient',
                                                        leftIcon=DashIconify(icon="pajamas:api"),
                                                        style={'textAlign':'center'},
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                            dmc.Alert(
                                id=alert1_id,
                                children=['API key registered!!!'],
                                title="Success!",
                                color="green",
                                hide=True,
                                duration=10000
                            ),
                            dmc.Alert(
                                id=alert2_id,
                                children=['API key not registered. Problem in Key'],
                                title="Failure",
                                color="red",
                                hide=True,
                                duration=10000
                            ),
                        ]
                    )
                ]
            )


def create_card_p8(i, model, temp, id1, id2, id3, id4):
    return dmc.Col(
            span=12,
            sm=6,
            md=4,
            children=[
                dmc.Card(
                    id=id3,
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"height": '100%'},
                    children=[
                        dmc.CardSection(
                            dmc.Title(model+ " - " +str(temp), order=2, p=15, style={'height':'100px'}),
                        ),
                        dmc.Group(
                            [
                                dmc.Badge(" ", color="grey", variant="light", id=id4),
                                dmc.Badge(" ", color="grey", variant="light", id=id1),
                            ],
                            position="apart",
                            mt="md",
                            mb="xs",
                        ),
                        dmc.Textarea(
                            id=id2,
                            size="sm",
                            variant="filled",
                            placeholder='Answer',
                            autosize=True,
                            minRows=6,
                        ),
                    ]
                )
            ]
        )


def get_answer_openai(question, model, api_key, temp):
    if model == 'gpt-3.5-turbo' or model == 'gpt-3.5-turbo-0301':
        llm = ChatOpenAI(model_name=model, openai_api_key=api_key, temperature=temp)
        text = llm([HumanMessage(content=question)])
        text = text.content
        return text
    else:
        llm = OpenAI(model_name=model, openai_api_key=api_key, temperature=temp)
        text = llm(question)
        return text
    
    
def get_answer_ai21(question, model, api_key, temp):
    llm = AI21(model=model, ai21_api_key=api_key, temperature=temp)
    text = llm(question)
    return text


def get_answer_replicate(question, model, api_key, temp):
    llm = Replicate(model = model, model_kwargs=[{'temperature':temp, 'max_token':100}])
    text = llm(question)
    return text
