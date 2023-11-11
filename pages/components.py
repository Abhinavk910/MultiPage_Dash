
from pages.common import *

def select(id, data, value='', label='', placeholder='', style={"width": 200}, width=200, margin=10):
    return dmc.Select(
                id=id,
                data=data,
                value=value,
                label=label,
                clearable=True,
                style=style,
                persistence=True,
                persistence_type='session'
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

def numberinput(id, label, description:str=None, value:int=0, min:int=0, step:int=1,precision:int=0, style:dict={'width':'200px'}, licon="fa6-solid:weight-scale"):
    return dmc.NumberInput(
                id=id,
                label=label,
                description=description,
                value=value,
                min=min,
                step=step,
                style=style,
                precision=precision,
                icon=DashIconify(icon=licon),
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

def modal(id:str, children:list, title:str='',zIndex:int=1000, size:str|int="55%", centered:bool=True, overflow:str='outside', opened:bool=False, lockScroll:bool=True):
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