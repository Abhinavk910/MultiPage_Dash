# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:03:17 2023

@author: abhinav.kumar
"""

#https://data-visualization.up.railway.app/apps/VideoVolunteers


import dash_mantine_components as dmc
from dash import html, dcc, Output, Input, Dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
import plotly.graph_objects as go
import numpy as np

dash.register_page(__name__, path='/VideoVolunteers')

df = pd.read_excel('assets/data_vv.xlsx')
cc_name = df.cc_name.unique().tolist()
cc_name = sorted(cc_name)
state_name = df.state_name.unique().tolist()


columns = ['uid', 'state_name', 'district','approval', 'cc_name', 'village_name', 'block_name', 'panchayat_name',
           'topic_identification_reason_2', 'issue', "themes short", "impact_steps_followed_at_local_level_short_form",
           "duration_of_problem", "underlying_reason_of_issue_2", "primary_affected_groups_2", "level_of_spread",
           "no_of_individuals_affected", "impact_raised_awareness_2", "escalate_problem_to_govt_officials_2",
           "impact_govt_official_support_details_2", "is_impact", 'people_impacted', "villages_impacted"
          ]
df3 = df[columns]
df3.loc[:, 'initial'] = "Total"

json = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.0816771698864,
          23.91914203216001
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.2829904263645,
          23.077903145729366
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          83.80980808140066,
          24.15981061074082
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.43089761805766,
          23.79596040255116
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          87.21020833094724,
          24.828665691570876
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.30161533241068,
          24.192915751249274
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.86947726903816,
          24.205704918267827
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.14591948394997,
          23.653680316423845
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.54221324271543,
          23.041961407878432
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.36206593662445,
          23.991471778399415
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.33330893068103,
          22.696720957707768
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          87.63435518912706,
          25.246526727531176
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          87.2494232670195,
          24.269455873203142
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.67852688754584,
          23.43182669095144
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.69807762121457,
          24.489461875791434
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.62388393808396,
          22.46068979095992
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.32626565225581,
          23.37105954257862
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.51765853585789,
          23.632389145648602
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          87.84695701673718,
          24.638410690978418
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          86.80325890624755,
          23.959071735174007
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.59254290465617,
          24.468085339002414
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.50069734369123,
          23.744073124067924
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          85.93202964483282,
          22.700487018620976
        ],
        "type": "Point"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          84.50376233533672,
          22.609783409459553
        ],
        "type": "Point"
      }
    },
  ]
}
district_list = ['Palamu',
 'Khunti',
 'Garhwa',
 'Dhanbad',
 'Godda',
 'Giridih',
 'Chatra',
 'Bokaro',
 'Gumla',
 'Hazaribag',
 'East Singhbhum',
 'Sahebganj',
 'Dumka',
 'Lohardaga',
 'Deoghar',
 'West Singhbhum',
 'Ranchi',
 'Ramgarh',
 'Paakur',
 'Jamtara',
 'Koderma',
 'Latehar',
 'Saraikella Kharsawan',
 'Simdega']

dd = pd.DataFrame([i['geometry']['coordinates'] for i in json['features']])
dd['district'] = district_list
dd.columns = ['Long', 'Lat', 'district']


dictionary_col_name = {
    'initial':'Total Issue',
    'topic_identification_reason_2':'Reason of topic identification',
    'issue':'Issues',
    "themes short":'Issue themes', 
    "impact_steps_followed_at_local_level_short_form":'Step follewed at local level',
    "duration_of_problem":'Tentative Duration',
    "underlying_reason_of_issue_2":"Underlying Reason of Issue",
    "primary_affected_groups_2":"Primary Affected Groups",
    "level_of_spread":'Level of Spread',
    "impact_raised_awareness_2":"Impact Raised Awarenes",
    "escalate_problem_to_govt_officials_2":"Escalate Problem to Govt. Officials",
    "impact_govt_official_support_details_2":"Govt Official Support",
    "is_impact":"Is Impacted"
}


def clean_dataframe(df, columns_select, drop_na=True, typeit='issue'):
    if typeit == 'issue':
        df4 = df[columns_select]
    else:
        df4 = df[columns_select + ['people_impacted']]
        
    if 'topic_identification_reason_2' in df4.columns:
        df4.topic_identification_reason_2 = df4.topic_identification_reason_2.replace([ 'Newspaper awareness', 
                                        'CC lives the problem', 'Other', 'Heard about an issue'], 'Other_reason')
        
        
    if 'issue' in df4.columns:
        df4['issue'] = df4.issue.replace(['Power and Energy','Forced Evictions', 'Sanitation',
               'Rural Innovation',
               'Agrarian Crisis', 'Art & Culture',
               'Governance and Accountability', 'Indigenous People',
               'Natural Disaster', 'Environment', 'Mining',
               'Courage & Inspiration', 'Trafficking & Migration',
               'Labour Rights', 'Technology', 'Corruption', 'Reproductive Rights',
               'Crumbling Infrastructure','Gender', 'Religion & Faith', 'State Repression', 'Development',
               'Impact', 'Infrastructure', 'Caste', 'Conflict'], 'Other_issue')

    if 'themes short' in df4.columns:
        df4['themes short'] = df4["themes short"].replace([ 'Systemic Problem',
               'Cultural Problem', 'Adivasi Problem'], 'Other_theme')
        

    if 'duration_of_problem' in df4.columns:
        df4.duration_of_problem = df4.duration_of_problem.replace(['Last 1 year', 'Last 3 months',
               'Last month or less', 'Last 6 months', 'Not Applicable'], 'Last 1 year or less')
        

    if 'impact_govt_official_support_details_2' in df4.columns:
        df4.impact_govt_official_support_details_2 = df4.impact_govt_official_support_details_2.replace([
        'Others officials', 'BDO Office', 'District Collector'], 'BDO/DC Official')
        

    if 'underlying_reason_of_issue_2' in df4.columns:
        df4.underlying_reason_of_issue_2 = df4.underlying_reason_of_issue_2.replace(['Land dispossession', 'Tribal infringement',
           'Community unawareness', 'Official Neglect', 'Other',
           'Corruption/bribery', 'Gender discrimination',
           'Caste discrimination'], 'Other_underlying_reason')
        

    if 'primary_affected_groups_2' in df4.columns:
        df4.primary_affected_groups_2 = df4.primary_affected_groups_2.replace(['Muslims',
           'Children', 'Youth', 'Elderly'], 'Other_affected_groups')
        
    if 'level_of_spread' in df4.columns:
        df4.level_of_spread = df4.level_of_spread.replace(['Tola/Hamlet', 'Individual',
           'Neighborhood', 'Household', 'other', 'community(samuday)'], 'Under village')
        
    
    if drop_na:
        df4.dropna(inplace=True)
    else:
        if 'level_of_spread' in df4.columns:
            df4.level_of_spread = df4.level_of_spread.replace({np.nan:'ns_spread'})
        if 'primary_affected_groups_2' in df4.columns:
            df4.primary_affected_groups_2 = df4.primary_affected_groups_2.replace({np.nan:'ns_group'})
        if 'underlying_reason_of_issue_2' in df4.columns:
            df4.underlying_reason_of_issue_2 = df4.underlying_reason_of_issue_2.replace({np.nan:'ns_underlying_reason'})
        if 'impact_govt_official_support_details_2' in df4.columns:
            df4.impact_govt_official_support_details_2 = df4.impact_govt_official_support_details_2.replace({np.nan:'ns_official'})
        if 'duration_of_problem' in df4.columns:
            df4.duration_of_problem = df4.duration_of_problem.replace({np.nan:'ns_duration'})
        if 'themes short' in df4.columns:
            df4['themes short'] = df4["themes short"].replace({np.nan: 'ns_theme'})
        if 'topic_identification_reason_2' in df4.columns:
            df4.topic_identification_reason_2 = df4.topic_identification_reason_2.replace({np.nan:'ns_reason'})
        if 'is_impact' in df4.columns:
            df4.is_impact = df4.is_impact.replace({np.nan: 0})
        if 'impact_steps_followed_at_local_level_short_form' in df4.columns:
            df4.impact_steps_followed_at_local_level_short_form = df4.impact_steps_followed_at_local_level_short_form.replace({np.nan:'ns_steps'})
        if 'impact_raised_awareness_2' in df4.columns:
            df4.impact_raised_awareness_2 = df4.impact_raised_awareness_2.replace({np.nan:'ns_awareness'})
        if 'escalate_problem_to_govt_officials_2' in df4.columns:
            df4.escalate_problem_to_govt_officials_2 = df4.escalate_problem_to_govt_officials_2.replace({np.nan:'ns_escalate'})
    return df4

def get_sankey_dataframe(df4, typeit='number'):

    labels = []
    for col in range(df4.shape[1]):
        labels+=df4.iloc[:, col].unique().tolist()
    #     print(df4.iloc[:, col].unique().tolist())

    indexes = {i:labels.index(i) for i in labels}

    data = pd.DataFrame()

    for col in range(df4.shape[1] - 1):
        ch1 = df4.groupby([df4.columns[col], df4.columns[col+1]]).size().to_frame().reset_index()
        ch1.columns = ['source', 'target', 'value']
        data = pd.concat([data, ch1])

    data['source'] = data.source.map(indexes)
    data['target'] = data.target.map(indexes)
    
    if typeit != 'number':
        total_count = df4.shape[0]
        data['value'] = 100*(data.value/total_count)
    
    return labels, data

def get_sankey_dataframe_population(dd, typeit='number'):
    dd = dd.dropna(subset=['people_impacted'])
    labels = []
    for col in range(dd.shape[1]-1):
        labels+=dd.iloc[:, col].unique().tolist()
    indexes = {i:labels.index(i) for i in labels}
    data = pd.DataFrame()

    for col in range(dd.shape[1] - 2):
        ch1 = dd.groupby([dd.columns[col], dd.columns[col+1]]).agg({'people_impacted':'sum'}).reset_index()
        ch1.columns = ['source', 'target', 'value']
        data = pd.concat([data, ch1])
    data['source'] = data.source.map(indexes)
    data['target'] = data.target.map(indexes)
    
    if typeit != 'number':
        total_sum = dd.people_impacted.sum()
        data['value'] = 100*(data.value/total_sum)
    return labels, data


def plot_sankey(labels, data, title='', bgcolor="#fff", tilecolor='blue'):

    fig = go.Figure(data=[go.Sankey(
        valueformat = ".0f",
    #     valuesuffix = "%",
        node = dict(
          pad = 15,
          thickness = 10,
          line = dict(color = "black", width = 0.5),
          label = labels,
          color = tilecolor,
    #       hovertemplate='%{label} - %{value:.0f} <extra></extra>',
        ),
        link = dict(
          source = data['source'], # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = data['target'],
          value = data['value'],
    #       customdata = [val/sum(link.value) for val in link.value],
    #       hovertemplate = "Source: %{source.label}<br>Target: %{target.label}<br>Value: %{value}<br>Percentage: %{customdata:.2%}"
      ))])

    fig.update_layout(title_text=title, title_font_size=20,plot_bgcolor=bgcolor,paper_bgcolor=bgcolor, margin=dict(t=50, l=20, r=20, b=20, pad=10))
    return fig


def build_map(df, zoom=5.5, mapboxstyle="stamen-terrain"):
    
    d = df.groupby('district').agg({'uid':'count','village_name':'nunique', 'block_name':'nunique', 'panchayat_name':'nunique'})

    ddd = dd.set_index('district').join(d).dropna()
    
    text = [f"District - {district}<br>Block - {int(block)}<br>Panchayat - {int(panchayat)}<br>Village - {int(village)}<br>Total Issues - {int(issue)}" for district, village, block, panchayat, issue in zip(ddd.index, ddd.village_name, ddd.block_name, ddd.panchayat_name, ddd.uid)]
    

    # Define the latitude and longitude coordinates for your data
    latitudes = ddd.Lat
    longitudes = ddd.Long

    # Define the data values for your contour plot
    z_values = ddd.uid

    # Create the contour plot using go.Contourmapbox()
    fig = go.Figure(go.Densitymapbox(
            lat=latitudes,
            lon=longitudes,
            z=z_values,
            text=text,
            hovertemplate ='<b>%{text}</b><extra></extra>',
            colorscale='Viridis'
    ))

    # Set the layout of your figure
    fig.update_layout(
        mapbox_style=mapboxstyle,
        mapbox=dict(
            center=dict(
                lat=23.653680,
                lon=86.145919
            ),
            zoom=zoom
        )
    )
    fig.update_traces(showscale=False)
    fig.update_layout(
        plot_bgcolor="#fff",
        font=dict(color='#999999'),
        height=300,
        margin=dict(t=0, l=0, r=0, b=0, pad=0)
      )
    return fig


def create_table(df):
    columns, values = df.columns, df.values
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Tbody(rows)]
    return table


def cc_info(dff):
    state = dff.state_name.dropna().unique()[0]
    district = dff.district.dropna().unique()[0]
    village = len(dff.village_name.dropna().unique())
    block = len(dff.block_name.dropna().unique())
    panchayat = len(dff.panchayat_name.dropna().unique())
#     total_issue = dff.shape[0]
#     no_of_approval = dff.approval.dropna().shape[0]

    data = pd.DataFrame.from_dict({
        'State':[state],
        'District':[district],
        'Block Cover':[block],
        'Panchayat Cover':[panchayat],
        'Village Cover':[village],
#         'Issue Got Approval':[f'{str(no_of_approval)}/{total_issue}']
    }, orient='index').reset_index()
    data = create_table(data)
    return data

def state_info(dff):
    district = len(dff.district.dropna().unique()) 
    village = len(dff.village_name.dropna().unique())
    block = len(dff.block_name.dropna().unique())
    panchayat = len(dff.panchayat_name.dropna().unique())

    data = pd.DataFrame.from_dict({
        'District Cover':[district],
        'Block Cover':[block],
        'Panchayat Cover':[panchayat],
        'Village Cover':[village],
#         'Issues Got Approval':[f'{str(no_of_approval)}/{total_issue} Issues']
    }, orient='index').reset_index()
    data = create_table(data)
    return data

def country_info(dff):
    state = len(dff.state_name.dropna().unique()) 
    district = len(dff.district.dropna().unique()) 
    village = len(dff.village_name.dropna().unique())
    block = len(dff.block_name.dropna().unique())
    panchayat = len(dff.panchayat_name.dropna().unique())

    data = pd.DataFrame.from_dict({
        'State Cover':[state],
        'District Cover':[district],
        'Block Cover':[block],
        'Panchayat Cover':[panchayat],
        'Village Cover':[village],
#         'Issues Got Approval':[f'{str(no_of_approval)}/{total_issue} Issues']
    }, orient='index').reset_index()
    data = create_table(data)
    return data



backcolor = "#ECF9FF"
containercolor= "#f1faee"
paper_color = "#a8dadc"
card_headline = "#1d3557"
cart_text_size = 35
name_size = 30
tilecolor = "#e63946"
selectcolor = "#457b9d"



layout = dmc.Paper(children=[
    dmc.Stack([
#         dmc.MediaQuery([
        dmc.Paper(
            children=[
                dmc.Grid(
                    children=[
                        dmc.Col(
                            children=[
                                dmc.Group([
                                    dmc.Image(
                                        src="/assets/VV_logo.png", alt="vv", width=150
                                    ),
                                    dmc.Image(
                                        src="/assets/VFSG_logo.png", alt="vv", width=150
                                    )
                                ])
                                ], xs=6, sm=6, md=8, p=0),
                        dmc.Col(
                            children=[
                                dmc.Select(
                                    data=state_name,
                                    placeholder="Select State",
                                    clearable=True,id = 'state-name',
                                    searchable=True,
                                    value="",
                                    size=20,radius=50,
                                    nothingFound="No options found",
                                    icon=DashIconify(icon="fluent:real-estate-24-filled"),
                                    styles={
                                        "input":{"color": selectcolor, "background-color": paper_color, 'fontSize':'12px',  'border':f'1px solid {selectcolor}'},
                                        "icon":{"color": selectcolor},
                                        "dropdown":{'fontSize':'12px'},
                                        "item":{'fontSize':'12px', 'padding':'2px'},
                                    },
                                    sx={
                                        "svg":{'height':'12px'}
                                        },
                                )],xs=6,  sm=6, md=2),
                        dmc.Col(
                            dmc.Select(
                                data=cc_name,
                                placeholder="CC Profile",
                                clearable=True,
                                id = 'cc-name',
                                searchable=True,
                                value="",
                                size=20,
                                radius=50,
                                nothingFound="No options found",
                                icon=DashIconify(icon="material-symbols:person"),
                                styles={
#                                         "dropdown":{"background-color": selectcolor},
                                    "input":{"color": selectcolor, "background-color": paper_color, 'fontSize':'12px', 'border':f'1px solid {selectcolor}'},
                                    "icon":{"color": selectcolor},
                                    "item":{'fontSize':'12px', 'padding':'2px'},
                                    "dropdown":{'fontSize':'12px'},
                                },
                                sx={
                                    "svg":{'height':'12px'},
                                    },
                                ),xs=6,  sm=6, md=2)
                    ],align="flex-end",justify='center', gutter="xl"),
                dmc.Divider(variant="solid", size="sm", className='my-2',style={"background-color": paper_color}),
                dmc.Paper(
                    dmc.Grid(
                        children=[
                            dmc.Col(
                                children=[
                                    dmc.Group(
                                        children=[
                                            dmc.Avatar(id='avatar-name', color="cyan", radius="xl"),
                                            dmc.Text( id='full-name',  style={"color": card_headline}, size=name_size, weight=700),
#                                             dmc.Text(align='center', id='issue-approved2')
                                        ],className='mb-3'),
                                    dmc.Table(
#                                         striped=True,
#                                         highlightOnHover=True,
#                                         withBorder=True,
#                                         withColumnBorders=True,
                                        id='descrip-table',
                                        style={"color": card_headline},
                                        fontSize=20
                                    )
                                ], style={"background-color": '','margin':'auto'}, lg=5, sm=12),
                            dmc.Col(
                                children=[
                                    dcc.Graph(id='geo-chart')
                                ], lg=7, sm=12)
                        ],gutter="xl", className='m-0'),p=15,radius=10, style={"background-color": paper_color},),
                dmc.SimpleGrid(
                    cols=5,
                    spacing="lg",
                    breakpoints=[
                        {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                    ],
                    children=[
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Text('240', align='center', id='issue-produced', size=cart_text_size, weight=700,  style={"color": card_headline})
                                ),
                                dmc.Text(
                                    "Issue Produced", align='center',size="sm", color='dimmed'
                                ),
                            ],
                            withBorder=True, shadow="sm", radius=10, style={"background-color": paper_color},),
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Text('60', align='center', id='issue-approved', size=cart_text_size, weight=700,  style={"color": card_headline})
                                ),
                                dmc.Text(
                                    "Issue Approved", align='center',size="sm", color='dimmed'
                                ),
                            ],
                            withBorder=True, shadow="sm", radius="md", style={"background-color": paper_color},),
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Text('60', align='center', id='issue-resolved', size=cart_text_size, weight=700,  style={"color": card_headline})
                                ),
                                dmc.Text(
                                    "Issue Resolved", align='center',size="sm", color='dimmed'
                                ),
                            ],
                            withBorder=True, shadow="sm", radius="md", style={"background-color": paper_color},),
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Text('240', align='center', id='affected-individuals', size=cart_text_size, weight=700,  style={"color": card_headline})
                                ),
                                dmc.Text(
                                    "Aff. Individuals per Issue", align='center',size="sm", color='dimmed'
                                ),
                            ],
                            withBorder=True, shadow="sm", radius="md", style={"background-color": paper_color},),
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Text('240', align='center', id='affected-population', size=cart_text_size, weight=700,  style={"color": card_headline})
                                ),
                                dmc.Text(
                                    "Affected Population", align='center',size="sm", color='dimmed'
                                ),
                            ],
                            withBorder=True, shadow="sm", radius="md", style={"background-color": paper_color},),
                    ],
                    className='my-2'),
                dmc.Paper(
                    dmc.Grid(
                        children=[
                            dmc.Col(
                                children=[
                                    dmc.SegmentedControl(
                                        id="sankey-value",
                                        value="issue",
                                        data=[
                                            {"value": "issue", "label": "Issue"},
                                            {"value": "population", "label": "Affected Population"},
                                        ],
                                        fullWidth=True,
                                        size='xs',
                                        radius=20,
                                        mt=10,mb=-2,
                                        color="#457b9d",
                                        styles={
                                            "input":{"color": selectcolor, "background-color": paper_color, 'fontSize':'6px', 'border':f'1px solid {selectcolor}'},
                                            "icon":{"color": selectcolor},
#                                             "item":{'fontSize':'12px', 'padding':'2px'},
                                            "value":{"color": selectcolor, "background-color": paper_color,'fontSize':'12px',},
                                            "label":{"color":selectcolor},
                                            'active':{"color":selectcolor, "background-color": selectcolor,},
                                            "root":{'color':'pink', 'background-color':paper_color, 'border':f"1px solid {selectcolor}"},
                                            
                                        },
                                    ),
                                ], sm=12, lg=3),
                            dmc.Col(
                                children=[
                                    dmc.SegmentedControl(
                                        id="sankey-value-type",
                                        value="number",
                                        data=[
                                            {"value": "number", "label": "Number"},
                                            {"value": "percentage", "label": "Percentage"},
                                        ],
                                        fullWidth=True,
                                        mt=10,
                                        radius=20,
                                        size='xs',
                                        mb=-2,
                                        color="#457b9d",
                                        styles={
                                            "input":{"color": selectcolor, "background-color": paper_color, 'fontSize':'6px', 'border':f'1px solid {selectcolor}'},
                                            "icon":{"color": selectcolor},
#                                             "item":{'fontSize':'12px', 'padding':'2px'},
                                            "value":{"color": selectcolor, "background-color": paper_color,'fontSize':'12px',},
                                            "label":{"color":selectcolor},
                                            'active':{"color":selectcolor, "background-color": selectcolor,},
                                            "root":{'color':'pink', 'background-color':paper_color, 'border':f"1px solid {selectcolor}"},
                                            
                                        },
                                    ),
                                ], sm=12, lg=3),
                            dmc.Col(
                                children=[
                                    dmc.MultiSelect(
                                        label="Select event",
                                        placeholder="Select all you like!",
                                        nothingFound="No options found",
                                        id="column-select",
                                        value=["initial", "issue", "is_impact"],
                                        icon=DashIconify(icon="material-symbols:event"),
                                        data=[{'value':i, 'label':j} for i, j in dictionary_col_name.items()],
                                        radius=50,
                                        styles={

                                            "marginBottom": 10,
                                            "input":{"color": selectcolor, "background-color": paper_color, 'fontSize':'6px', 'border':f'1px solid {selectcolor}'},
                                            "icon":{"color": selectcolor},
                                            "item":{'fontSize':'12px', 'padding':'2px'},
                                            "value":{"color": selectcolor, "background-color": paper_color,'fontSize':'12px',},
                                            "label":{"color":selectcolor, 'fontSize':'15px'},
                                            "error":{'fontSize':'12px'}
                                        },
                                        sx={
                                    "svg":{'height':'12px',"color": selectcolor,"background-color": paper_color,},
                                },
                                        size=20
                                    ),
                                ], sm=12, lg=6),
                            dmc.Col(
                                children=[
                                    dcc.Graph(id='sankey-chart'),
                                    dmc.Text("*prefix 'ns' indicates that there is no specific value in a particular row of a specific column.", align='right', size='xs', color="gray")
                                ], lg=12)
                        ],align="flex-end"),p=15,radius=10, style={"background-color": paper_color},)   
            ],className="",
            shadow="md",style={'max-width':'1200px', "background-color": containercolor},p=20, mt=30, mb=10, radius=30),
#                        ],
#                       smallerThan="md",styles={'max-width':'1200px', "background-color": containercolor, 'padding':'5px'},),
    dmc.Paper(
        dmc.Text(['Created By', dcc.Link(' Abhinav Kumar', href = 'http://www.linkedin.com/in/abhinavk910', target="_blank", style={'text-decoration': 'none', 'color':selectcolor})], align='center', color=paper_color, weight=700),
        p=10, mb=30, radius=30,shadow="md",mx=2, style={"background-color": containercolor}
    )], style={'overflow-x': 'auto'})
], className='min-vh-100 mx-sm-5 mx-md-auto d-flex justify-content-center align-items-center', 
             style={"background-color": backcolor})
#


@dash.callback(
    Output('cc-name', 'data'),
#     Output('cc-name', 'value'),
#     Output('heading', 'children'),
    Input('state-name', 'value'),
    prevent_initial_call=True)
def update_cc(val):
    if val != "":
        list_val =  sorted(df.query('state_name == @val').cc_name.unique().tolist()) 
        return list_val#, list_val[0]
    else:
        return cc_name#, 'Amit Topno'
        
@dash.callback(
    Output('state-name', 'value'),
#     Output('heading', 'children'),
    Input('cc-name', 'value'),
    prevent_initial_call=True)
def update_state(val):
    if val != "":
        try:
            return df.query('cc_name == @val').state_name.unique()[0]
        except:
            raise PreventUpdate
    else:
        return 'Jharkhand'
        
@dash.callback(Output("column-select", "error"), Input("column-select", "value"))
def select_value(value):
    return "Select at least 3." if len(value) < 3 else ""

@dash.callback(Output("sankey-chart", 'figure'), Input("column-select", "value"),
             Input("state-name", 'value'), Input('cc-name', 'value'), Input('sankey-value', 'value'), 
             Input("sankey-value-type", 'value'))
def populate_graph_sankey(value, state, cc, sankey_val, ispercentage):
    if len(value) >= 3:
        df4 = df3.copy()
        if state:
            df4 = df3.query('state_name == @state')
        if cc:
            df4 = df3.query('cc_name == @cc')
            
        if sankey_val == 'issue':
            if ispercentage == 'number':
                text = "Number of Issue Raised"
            else:
                text = "% of Issue Raised"
            df = clean_dataframe(df4, value, False)
            labels, data = get_sankey_dataframe(df, typeit=ispercentage)
        else:
            if ispercentage == 'number':
                text = "Number of Affected Population"
            else:
                text = "% of Affected Population"
            dd = clean_dataframe(df4, value, False, typeit='population')
            labels, data = get_sankey_dataframe_population(dd, typeit=ispercentage)
        
        fig = plot_sankey(labels, data,title=text, bgcolor=paper_color, tilecolor=tilecolor)
        return fig
    else:
        raise PreventUpdate

@dash.callback(Output('avatar-name', 'children'),Output('full-name', 'children'),
              Output('descrip-table', 'children'),
              Input("state-name", 'value'), Input("cc-name", 'value'))
def update_name(state,cc):
    name='India'
    df4 = df3.copy()
    table = country_info(df4)
    if state:
        name = state
        df4 = df3.query('state_name == @state')
        table = state_info(df4)
    if cc:
        name = cc
        df4 = df3.query('cc_name == @cc')
        table = cc_info(df4)
    return "".join([i[0].upper() for i in name.split(" ")]), name.upper(), table
        
@dash.callback(Output('issue-produced', 'children'),Output('issue-resolved', 'children'),
              Output('affected-individuals', 'children'), Output('affected-population', 'children'),
              Output('issue-approved', 'children'),
              Input("state-name", 'value'), Input("cc-name", 'value'))
def card_populate(state, cc):
    df4 = df3.copy()
    if state:
        df4 = df3.query('state_name == @state')
    if cc:
        df4 = df3.query('cc_name == @cc')
    
    return f"{len(df4['issue']):,}", df4.is_impact.sum(),f'{int(np.mean(df4.people_impacted.fillna(0))):,}', f'{int(np.sum(df4.people_impacted.fillna(0))):,}', df4.approval.dropna().shape[0]

@dash.callback(Output('geo-chart', 'figure'), Input("state-name", 'value'), Input('cc-name', 'value'))
def populate_graph(state, cc):
    df4 = df3.copy()
    zoom=4
    if state:
        df4 = df3.query('state_name == @state')
        zoom=5.5
    if cc:
        df4 = df3.query('cc_name == @cc')
        zoom=5.5
    
    
    fig = build_map(df4, zoom, mapboxstyle="carto-positron")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=5500)