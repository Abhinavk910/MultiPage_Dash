from ..common import *

def create_layout():

    bse_tab = dmc.Container(
                    # fluid=True,
                    p='xl',
                    mih='100vh',
                    children=[
                        dmc.Text('BSE - Bristol Stock Exchange') for i in range(100)
                    ]
                )
    
    param_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    mih='100vh',
                    children=[
                        dmc.Text('BSE - Parameters')
                    ]
                )

    viz_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    mih='100vh',
                    children=[
                        dmc.Text('BSE - Viz')
                    ]
                )


    init_struc = dmc.Tabs([
                    dmc.TabsList([
                        dmc.Tab("BSE", value="bse"),
                        dmc.Tab("Parameters", value="param"),
                        dmc.Tab("Visualization", value="viz"),
                    ]),
                    dmc.TabsPanel(bse_tab, value="bse"),
                    dmc.TabsPanel(param_tab, value="param"),
                    dmc.TabsPanel(viz_tab, value="viz"),
                    ],
                    color="red",
                    orientation="vertical",
                    value='bse'
                )

    main_container = dmc.Container(
                    fluid=True,
                    maw=900,
                    mah='100vh',
                    style={'backgroundColor':'grey'},
                    children=[
                        init_struc
                    ]
                )

    return main_container
