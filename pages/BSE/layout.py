from ..common import *
from ..components import *

def create_layout():

    bse_tab = dmc.Container(
                    # fluid=True,
                    p='xl',
                    mih='100vh',
                    children=[
                        dmc.Text('BSE - Bristol Stock Exchange')
                    ]
                )
    
    buyer_title = dmc.Text(children="Buyer", size=20, color='blue')
    type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
    buyer_type = select(id={'type': 'bse-buyer-type', 'index': 0}, data=type_options, value="ZIP", label="Select Type of Buyer", righticon="", persistance=False)
    buyer_num = numberinput(id={'type': 'bse-buyer-num', 'index': 0}, label='Select No of Buyer', min=1, step=1, value=5)
    buyer_group = group(children=[buyer_type, buyer_num], position='left')
    add_new_buyer_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-buyer', icon='ic:baseline-plus'), actionicon('bse-delete-new-buyer', icon='ic:baseline-minus')])
    buyer_range = rangeslider(id='bse-buyer-SDRange', label='Select Demand Range', width="99%", margin=0, marginButtom=10)
    buyer_paper = paper(children=[buyer_title, buyer_group, add_new_buyer_btn, dmc.Divider(variant="solid", m=10,),buyer_range], id='bse-paper-buyer')

    seller_title = dmc.Text(children="Seller", size=20, color='red')
    type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
    seller_type = select(id={'type': 'bse-seller-type', 'index': 0}, data=type_options, value="ZIP", label="Select Type of Seller", righticon="", persistance=False)
    seller_num = numberinput(id={'type': 'bse-seller-num', 'index': 0}, label='Select No of Seller', min=1, step=1, value=5)
    seller_group = group(children=[seller_type, seller_num], position='left')
    add_new_seller_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-seller', icon='ic:baseline-plus'), actionicon('bse-delete-new-seller', icon='ic:baseline-minus')])
    seller_range = rangeslider(id='bse-seller-SDRange', label='Select Supply Range', width="99%", margin=0, marginButtom=10)
    seller_paper = paper(children=[seller_title, seller_group, add_new_seller_btn, dmc.Divider(variant="solid", m=10,),seller_range], id='bse-paper-seller')

    # Supply, Demand and Order Schedules 
    sch_title = dmc.Text(children="Supply, Demand and Order Schedules ", size=20, color='green')
    time_start = numberinput(id='bse-sd-scheduler-start', label='Select Time Start', min=0, step=60, value=0)
    time_end = numberinput(id='bse-sd-scheduler-end', label='Select Time End', min=60, step=60, value=600)
    stepmode_options = ["fixed", "jittered", "random"]
    stepmode_type = select(id='bse-stepmode', data=stepmode_options, value="fixed", label="Select Type of Seller", righticon="", persistance=False)
    scheduler_group = group(children=[time_start, time_end, stepmode_type], position='left')
    order_interval = numberinput(id='bse-sd-scheduler-order-interval', label='Select Order Interval', min=0, step=10, value=60)
    timemode_options = ["periodic", "drip-fixed", "drip-jitter", "drip-poisson"]
    timemode_type = select(id='bse-timemode', data=timemode_options, value="periodic", label="Select Type of Timemode", righticon="", persistance=False)
    order_group = group(children=[order_interval, timemode_type], position='left')
    sd_schedule_paper = paper(children=[scheduler_group, order_group])


    graph_btn = button(id='bse-graph1-btn', label='Generate SD Curve')
    show_segment = segmentcontrol(id='show-buyer-seller-segment', data=['Buyers', 'Sellers'], value='Buyers')
    scheduler_group = group(children=[graph_btn, show_segment], position='left')
    graph_paper = paper(children=[scheduler_group, dcc.Graph(id='bse-graph1')])
    param_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    # mih='100vh',
                    children=[
                        dmc.Text('BSE - Parameters'),
                        dcc.Store(id='storing-ps3-pb3', data={}),
                        buyer_paper,
                        seller_paper,
                        sd_schedule_paper,
                        graph_paper
                    ]
                )

    viz_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    # mih='100vh',
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
                    orientation="horizontal",
                    value='param'
                )

    main_container = dmc.Container(
                    fluid=True,
                    maw=1200,
                    # mah='100vh',
                    style={'backgroundColor':'#F9F9F9'},
                    children=[
                        get_ferry_top_pregress(init_struc, '#228BE6')
                    ]
                )

    return main_container
