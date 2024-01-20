
from pages.common import *

def select(id, data, value='', label='', placeholder='', style={"width": 200}, width=200, margin=10,
           clearable=False, persistance=True,
            lefticon="radix-icons:magnifying-glass", righticon="radix-icons:chevron-down"):
    return dmc.Select(
                id=id,
                data=data,
                value=value,
                label=label,
                clearable=clearable,
                style=style,
                persistence=persistance,
                persistence_type='session',
                icon=DashIconify(icon=lefticon),
                rightSection=DashIconify(icon=righticon) if righticon != "" else "",
            )

def feffery_select(id:str, placeholder:str,options:list,label:str='write label',
                   persistence:bool=False,style:dict={'width':'200px'}, spacing='0px'):
    return dmc.Stack(
        spacing=spacing,
        children=[
            dmc.Text(children=label, m=0, style={'fontSize': '14px', 'fontWeight': 500}),
            fuc.FefferyStyle(
                    rawStyle='''
                        .ant-select-selector {
                            height:35px;
                        }'''
                    ),
            fac.AntdCascader(
                id=id,
                placeholder=placeholder,
                options=options,
                persistence=persistence,
                style=style,
                className='ant-select-selector'
            )
        ]
    )
    
def textinput(id, label, placeholder, licon='ic:round-alternate-email'):
    return dmc.TextInput(
                id=id,
                label=label,
                placeholder=placeholder,
                icon=DashIconify(icon=licon),
            )

def numberinput(id, label, description:str=None, value:int=0, min:int=0, max:int=99, step:int=1,precision:int=0, style:dict={'width':'200px'}, licon="fa6-solid:weight-scale", flip=None):
    if flip:
        icon = DashIconify(icon=licon, flip=flip)
    else:
        icon = DashIconify(icon=licon)
    return dmc.NumberInput(
                id=id,
                label=label,
                description=description,
                value=value,
                min=min,
                max=max,
                step=step,
                style=style,
                precision=precision,
                icon=icon,
            )

def rangeslider(id:str, label:str, width:int=1000, max=500, min=10, value:list=[10, 200], marginButtom=0, margin=10):
    return dmc.Stack(
        spacing=0,
        children=[
            dmc.Text(children=label),
            dmc.RangeSlider(
                id=id,
                w=width,
                max = max,
                min = min,
                value=value,
                marks=[
                    {"value": i, "label": str(i)}
                    for i in value
                ],
                mb=marginButtom,
                m=margin,
                step=10
            )
        ]
    )


def segmentcontrol(id:str, data:list, value:str, margintop:int=0):
    """
    data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
    ]
    """
    return dmc.SegmentedControl(
            id=id,
            value=value,
            data= data,
            mt=margintop
        )

def button(id, label, variant='filled', color='blue', licon='fluent:settings-32-regular', disabled=False):
    return dmc.Button(
                label,
                id=id,
                variant=variant,
                leftIcon=DashIconify(icon=licon),
                color=color,
                disabled=disabled
            )

def actionicon(id, icon, icon_width:int=20,variant:str='filled', size:str='sm'):
    return dmc.ActionIcon(
            DashIconify(icon=icon, width=icon_width),
            size=size,
            variant=variant,
            id=id,
            n_clicks=0
        )

def datepicker(id, label='Write Label', description:str=None, minDate=date(2020, 8, 5), value=datetime.now().date(), style:dict={"width": 200}):
    return dmc.DatePicker(
            id=id,
            label=label,
            description=description,
            minDate=minDate,
            maxDate=value,
            value=value,
            style=style
        )

def feffery_datepicker(id, label='Time', spacing='0px'):
    return dmc.Stack(
        spacing=spacing,
        children=[
            dmc.Text(label),
            fac.AntdDatePicker(
                id=id,
                placeholder='Pick Date and Time',
                showTime=True
            )
        ]
    )

def alert(id, message="Problem!!", title='Problem!!', color='red', duration=3000,hide=True, withCloseButton=True):
    return dmc.Alert(
        id=id,
        children=message,
        title=title,
        color=color,
        duration=duration,
        hide=hide,
        withCloseButton=withCloseButton,
    )

# table
def ferry_table(id:str="", rowselectiontype:str='checkbox', 
                data=[{0: '123', 1: '1.23', 2: 'asdf', 3: datetime.now()}] * 3,
                columns=[{'title': str(i), 'dataIndex': str(i)} for i in range(4)],
                sortOptions={'sortDataIndexes': ['1','2']},
                filterOptions={}):
    """
    filterOptions = {'1': {'filterSearch': True}}
    """
    return fac.AntdTable(
                id=id,
                locale='en-us',
                rowSelectionType=rowselectiontype,
                selectedRowsSyncWithData=True,
                columns=columns,
                data=data,
                sortOptions=sortOptions,
                filterOptions = filterOptions
            ) 

#group
def group(children:list,id:str='',  position:str='center', spacing:int=5, align:str='center', grow:bool=False, style:dict={}  ):
    """
    align (a value equal to: 'initial', 'inherit', 'left', 'right', 'center', 'justify', 'end', 'start', '-moz-initial', 'revert', 'unset', 'match-parent'; optional):
    position (a value equal to: 'left', 'right', 'center', 'apart'; optional):
    """
    return dmc.Group(
        id=id,
        position=position,
        align=align,
        grow=grow,
        spacing=spacing,
        children=children,
        style=style
    )

#container
def paper(children:list, id='', padding='xs',margin=10,radius:int=0, shadow='sm', withborder:bool=False):
    """ 
    shadow - Predefined box-shadow from theme.shadows (xs, sm, md, lg, xl) or
            ny valid css box-shadow property.
    """
    return dmc.Paper(
        id=id,
        p=padding,
        m=margin,
        radius=radius,
        shadow=shadow,
        withBorder=withborder,
        children=children
    )

def modal(id:str, children:list, title:str='',zIndex:int=1000, size="55%", centered:bool=True, overflow:str='outside', opened:bool=False, lockScroll:bool=True):
    """
    overflow (a value equal to: 'outside', 'inside'; optional):Control vertical overflow behavior.
    opened (boolean; default False): Mounts modal if True.
    lockScroll (boolean; optional): Determines whether scroll should be locked when modal is opened, defaults to True.

    """
    return dmc.Modal(
        id=id,
        children=children,
        centered=centered,
        title=title,
        zIndex=zIndex,
        size=size,
        overflow=overflow,
        opened=opened,
        lockScroll=lockScroll
    )


def get_ferry_top_pregress(children:list, color:str):
    return fuc.FefferyTopProgress(
        children=children,
        color=color,
        id='top-progress',
        # listenPropsMode='exclude',
        style={'width':'-webkit-fill-available'}
    )

def get_graph_skeleton(graph_id:str, fig={'data': [],
                                        'layout': {'xaxes':{'showgrid':'false', 'showticklabels':'false', 'zeroline':'false'}},
                                        'frames': []}, config:dict=None, style:dict=None,
                        className:str='none', responsive:bool=True):
    if not config:
        config = {"displaylogo": False,
                  'modeBarButtonsToRemove': ['lasso2d', 'zoom', 'select', 'autoScale']}
    if not style:
        style = {"width": "100%", "height": "100%"}
    return dmc.Skeleton(
        height="100%",
        width="100%",
        visible=True,
        id=graph_id+"-skeleton",
        children=[
            dcc.Graph(id=graph_id, figure=fig, style=style, className=className, config=config,
                          responsive=responsive)
        ]
    )