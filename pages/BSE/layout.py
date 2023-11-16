from ..common import *
from ..components import *

def create_layout():

    bse_tab = dmc.Container(
                    # fluid=True,
                    p='xl',
                    mih='100vh',
                    children=[
                        dmc.Text('BSE - Bristol Stock Exchange', weight=700, size='xl'),
                        html.Hr(),
                        dmc.Text("BSE is simulation of a limit order book (LOB) exchange. There are a number of trading algorithms already built in and it provides a wide range of customizations to suit a large variety of experiments."),
                        html.Hr(),
                        dmc.Text("At a high level, BSE works as follows. First, you set a number of configuration parameters (specifying the trading agents in the market, the demand and supply in the market, and how demand and supply is allocated over time) that describe the experiment you want to conduct. You then ask BSE to simulate a number of market sessions that follow those configuration parameters. BSE's simulation will produce a number of output files that result from these simulated trading sessions. Data in these output files can then be analysed.  ")
                    ]
                )
    
    buyer_title = dmc.Text(children="Buyer", size=20, color='blue')
    type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
    buyer_type = select(id={'type': 'bse-buyer-type', 'index': 0}, data=type_options, value="ZIP", label="Select Type of Buyer", righticon="", persistance=False, lefticon="iconamoon:category")
    buyer_num = numberinput(id={'type': 'bse-buyer-num', 'index': 0}, label='Select No of Buyer', min=2, step=1, value=5, licon="line-md:buy-me-a-coffee-twotone")
    buyer_group = group(children=[buyer_type, buyer_num], position='left')
    buyer_stack = dmc.Stack(children=[buyer_group], id='buyer-group-stack1')
    add_new_buyer_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-buyer', icon='ic:baseline-plus'), actionicon('bse-delete-new-buyer', icon='ic:baseline-minus')])
    buyer_range = rangeslider(id={'type': 'bse-buyer-SDRange', 'index': 0}, label='Select Demand Range', width="90%", margin=0, marginButtom=10)
    buyer_range_stack = dmc.Stack(children=[buyer_range], id='buyer-range-stack1')
    add_new_range_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-buyer-range', icon='ic:baseline-plus'), actionicon('bse-delete-new-buyer-range', icon='ic:baseline-minus')])
    buyer_paper = paper(children=[buyer_title, buyer_stack, add_new_buyer_btn, dmc.Divider(variant="solid", m=10,),buyer_range_stack, add_new_range_btn], id='bse-paper-buyer')

    seller_title = dmc.Text(children="Seller", size=20, color='red')
    type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
    seller_type = select(id={'type': 'bse-seller-type', 'index': 0}, data=type_options, value="ZIP", label="Select Type of Seller", righticon="", persistance=False, lefticon="iconamoon:category")
    seller_num = numberinput(id={'type': 'bse-seller-num', 'index': 0}, label='Select No of Seller', min=2, step=1, value=5, licon="line-md:buy-me-a-coffee-twotone")
    seller_group = group(children=[seller_type, seller_num], position='left')
    seller_stack = dmc.Stack(children=[seller_group], id='seller-group-stack1')
    add_new_seller_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-seller', icon='ic:baseline-plus'), actionicon('bse-delete-new-seller', icon='ic:baseline-minus')])
    seller_range = rangeslider(id={'type': 'bse-seller-SDRange', 'index': 0}, label='Select Supply Range', width="90%", margin=0, marginButtom=10)
    seller_range_stack = dmc.Stack(children=[seller_range], id='seller-range-stack1')
    add_new_range_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-seller-range', icon='ic:baseline-plus'), actionicon('bse-delete-new-seller-range', icon='ic:baseline-minus')])
    seller_paper = paper(children=[seller_title, seller_stack, add_new_seller_btn, dmc.Divider(variant="solid", m=10,),seller_range_stack, add_new_range_btn], id='bse-paper-seller')

    # Supply, Demand and Order Schedules 
    sch_title1 = dmc.Text(children="StepModes", size=20, color='green')
    time_start = numberinput(id='bse-sd-scheduler-start', label='Select Time Start', min=0, step=60, value=0, max=1140, licon="carbon:time")
    time_end = numberinput(id='bse-sd-scheduler-end', label='Select Time End', min=60, step=60, value=600, max=1200, licon="carbon:time", flip='horizontal')
    stepmode_options = ["fixed", "jittered", "random"]
    stepmode_type = select(id='bse-stepmode', data=stepmode_options, value="fixed", label="Select Type of Stepmodes", righticon="", persistance=False)
    scheduler_group = group(children=[time_start, time_end, stepmode_type], position='left', style={'marginTop':'2px'})
    sch_title2 = dmc.Text(children="Market Session", size=20, color='green', mt=10)
    order_interval = numberinput(id='bse-sd-scheduler-order-interval', label='Select Order Interval', min=0, step=10, value=60, max=600, licon="carbon:time")
    timemode_options = ["periodic", "drip-fixed", "drip-jitter", "drip-poisson"]
    timemode_type = select(id='bse-timemode', data=timemode_options, value="periodic", label="Select Type of Timemode", righticon="", persistance=False)
    order_group = group(children=[order_interval, timemode_type], position='left', style={'marginTop':'2px'})
    sd_schedule_paper = paper(children=[sch_title1, scheduler_group,sch_title2, order_group])


    graph_btn = button(id='bse-graph1-btn', label='Plot Trades', licon="mdi:chart-scatter-plot")
    show_segment = segmentcontrol(id='show-buyer-seller-segment', data=['Buyers', 'Sellers'], value='Buyers')
    scheduler_group = group(children=[graph_btn, show_segment], position='left')
    alert_comp = alert(id='graph-throwing-any-error1')
    graph_paper = paper(children=[scheduler_group,alert_comp, dcc.Graph(id='bse-graph1', config ={'doubleClick' :'reset', 'displaylogo':False, 'modeBarButtonsToRemove':['resetViews', 'sendDataToCloud', 'select2d', 'lasso2d']})])

    sch_title1 = dmc.Text(children="Code", size=20, color='green')
    code_btn = button(id='bse-code1-btn', label='Plot Trades', licon="ant-design:code-outlined")
    code_space = dmc.Code(children="Code will be Like - ", id="current-experiment-code", block=True,)
    code_paper = paper(children=[sch_title1, code_btn, code_space])


    param_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    # mih='100vh',
                    children=[
                        dcc.Store(id='storing-ps3-pb3', data={}),
                        buyer_paper,
                        seller_paper,
                        sd_schedule_paper,
                        graph_paper,
                        code_paper
                    ]
                )

    viz_tab = dmc.Container(
                    fluid=True,
                    p='xl',
                    # mih='100vh',
                    children=[
                        dmc.Text('BSE - Viz, WOP')
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
                    color='#228BE6',
                    orientation="horizontal",
                    value='bse',
                    persistence="true",
                    persistence_type="session",
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
