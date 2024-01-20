from ..common import *
from ..components import *
from .utils import *

def register_callbacks():

    @callback(
        Output('buyer-segment-div', 'children'),
        Input('buyer-segment-control1', 'value'),
        State('bse-sd-scheduler-start', 'value'),
        State('bse-sd-scheduler-end', 'value')
    )
    def update_div(value, start, end):
        if value == 'Static':
            buyer_range = rangeslider(id={'type': 'bse-buyer-SDRange', 'index': 0}, label='Select Demand Range', width="90%", margin=0, marginButtom=10)
            buyer_range_stack = dmc.Stack(children=[buyer_range], id='buyer-range-stack1')
            add_new_range_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-buyer-range', icon='ic:baseline-plus'), actionicon('bse-delete-new-buyer-range', icon='ic:baseline-minus')])
            return [buyer_range_stack, add_new_range_btn]
        elif value == 'Dynamic':
            buyer_range = rangeslider(id={'type': 'bse-buyer-SDRange', 'index': 0}, label='Select Demand Range', width="90%", margin=0, marginButtom=10)
            buyer_range2 = rangeslider(id={'type': 'bse-buyer-SDRange', 'index': 1}, label='Select Demand Range', width="90%", margin=0, marginButtom=10)
            buyer_range_stack = dmc.Stack(children=[buyer_range, buyer_range2], id='buyer-range-stack1')
            add_new_range_btn = dmc.Group(position='right', m=10, children=[actionicon('bse-add-new-buyer-range', icon='ic:baseline-plus'), actionicon('bse-delete-new-buyer-range', icon='ic:baseline-minus')])
            mid_timing = numberinput(label='Add Mid Timing - 1',id={'type':'mid-timing', 'index':0}, min=start, max=end, step=5, value=start+50)
            mid_section_stack = dmc.Stack(children=[mid_timing], id='buyer-range-mid-section1')
            return [buyer_range_stack, add_new_range_btn, mid_section_stack]

    @callback(
        Output('buyer-range-mid-section1', 'children'),
        Input('bse-add-new-buyer-range', 'n_clicks'),
        Input('bse-delete-new-buyer', 'n_clicks'),
        Input({'type':'mid-timing', 'index':ALL}, 'value'),
        State('buyer-range-mid-section1', 'children'),
        State('buyer-segment-control1', 'value'),
        prevent_initial_update=True
    )
    def update_mid_range(add, sub, mid_val, child, segment):
        if segment == 'Dynamic':
             ic(mid_val, child)
        else:
            raise PreventUpdate



    @callback(
        Output('buyer-group-stack1', 'children', allow_duplicate=True),
        Input('bse-add-new-buyer', 'n_clicks'),
        Input('bse-delete-new-buyer', 'n_clicks'),
        State('buyer-group-stack1', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-buyer':
            index_no = len(child)
            type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
            buyer_type = select(id={'type': 'bse-buyer-type', 'index': index_no}, data=type_options, value="ZIP", label="Select Type of Buyer", righticon="", persistance=False)
            buyer_num = numberinput(id={'type': 'bse-buyer-num', 'index': index_no}, label='Select No of Buyer', min=2, max=99,step=1, value=5)
            buyer_group = group(children=[buyer_type, buyer_num], position='left')
            child.append(buyer_group)
            return child
        elif trig == 'bse-delete-new-buyer':
            if len(child) == 1:
                raise PreventUpdate
            else:    
                child = child[:-1]
                return child

    @callback(
        Output('buyer-range-stack1', 'children'),
        Input('bse-add-new-buyer-range', 'n_clicks'),
        Input('bse-delete-new-buyer-range', 'n_clicks'),
        State('buyer-range-stack1', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-buyer-range':
            index_no = len(child)
            buyer_range = rangeslider(id={'type': 'bse-buyer-SDRange', 'index': index_no}, label='Select Demand Range', width="90%", margin=0, marginButtom=10)
            child.append(buyer_range)
            return child
        elif trig == 'bse-delete-new-buyer-range':
            if len(child) == 1:
                raise PreventUpdate
            else:    
                child = child[:-1]
                return child



    @callback(
        Output('seller-group-stack1', 'children'),
        Input('bse-add-new-seller', 'n_clicks'),
        Input('bse-delete-new-seller', 'n_clicks'),
        State('seller-group-stack1', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-seller':
            index_no = len(child)
            type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
            buyer_type = select(id={'type': 'bse-seller-type', 'index': index_no}, data=type_options, value="ZIP", label="Select Type of Seller", righticon="", persistance=False)
            buyer_num = numberinput(id={'type': 'bse-seller-num', 'index': index_no}, label='Select No of Seller', min=2, step=1, value=5)
            buyer_group = group(children=[buyer_type, buyer_num], position='left')
            child.append(buyer_group)
            return child
        elif trig == 'bse-delete-new-seller':
            if len(child) == 1:
                raise PreventUpdate
            else:    
                child = child[:-1]
                return child

    @callback(
        Output('seller-range-stack1', 'children'),
        Input('bse-add-new-seller-range', 'n_clicks'),
        Input('bse-delete-new-seller-range', 'n_clicks'),
        State('seller-range-stack1', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-seller-range':
            index_no = len(child)
            seller_range = rangeslider(id={'type': 'bse-seller-SDRange', 'index': index_no}, label='Select Supply Range', width="90%", margin=0, marginButtom=10)
            child.append(seller_range)
            return child
        elif trig == 'bse-delete-new-seller-range':
            if len(child) == 1:
                raise PreventUpdate
            else:    
                child = child[:-1]
                return child


    @callback(
        Output('bse-graph1', 'figure', allow_duplicate=True),
        Output('storing-ps3-pb3', 'data'),
        Output('graph-throwing-any-error1', 'children'),
        Output('graph-throwing-any-error1', 'hide'),
        Input('bse-graph1-btn', 'n_clicks'),
        State({'type': 'bse-seller-type', 'index': ALL}, 'value'),
        State({'type': 'bse-seller-num', 'index': ALL}, 'value'),
        State({'type': 'bse-seller-SDRange', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-type', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-num', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-SDRange', 'index': ALL}, 'value'),
        State('bse-sd-scheduler-start', 'value'),
        State('bse-sd-scheduler-end', 'value'),
        State('bse-stepmode', 'value'),
        State('bse-sd-scheduler-order-interval', 'value'),
        State('bse-timemode', 'value'),
        State('show-buyer-seller-segment', 'value'),
        State('storing-ps3-pb3', 'data'),
        State('bse-graph1', 'figure',),
        prevent_initial_call=True
    )
    def update_sd_graph(n, seller_type, seller_num, seller_range, buyer_type, buyer_num, buyer_range, sch_start, sch_end, sch_stepmode, order_interval, timemode, segment, data_old, fig_old):
        ic(n, seller_type, seller_num, seller_range, buyer_type, buyer_num, buyer_range, sch_start, sch_end, sch_stepmode, order_interval, timemode)
        buyers_spec =  [(type_, num_) for type_, num_  in zip(buyer_type, buyer_num)]
        sellers_spec =  [(type_, num_) for type_, num_  in zip(seller_type, seller_num)]
        traders_spec = {'sellers':sellers_spec, 'buyers':buyers_spec}

        seller_count = 0
        seller_dictionary = dict()
        for i, j in zip(seller_type, seller_num):
            for k in range(seller_count, seller_count+j):
                seller_name = "S0"+str(k) if k<10 else "S"+str(k)
                seller_dictionary[seller_name] = i
            seller_count += j 

        buyer_count = 0
        buyer_dictionary = dict()
        for i, j in zip(buyer_type, buyer_num):
            for k in range(buyer_count, buyer_count+j):
                buyer_name = "B0"+str(k) if k<10 else "B"+str(k)
                buyer_dictionary[buyer_name] = i
            buyer_count += j

        # ic(buyer_dictionary, seller_dictionary) 

        # if len(seller_range) > 1:
        sup_range = [tuple(i) for i in seller_range]#(50, 100)
        # else:
        #     sup_range = tuple(seller_range[0])

        # if len(buyer_range) > 1:
        dem_range = [tuple(i) for i in buyer_range]#(50, 100)
        # else:
        #     dem_range = tuple(buyer_range[0])

        # dem_range = [tuple(i) for i in buyer_range]
        # ic(sup_range, dem_range)

        start_time = sch_start
        end_time = sch_end
        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': sup_range, 'stepmode': sch_stepmode}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': dem_range, 'stepmode': sch_stepmode}]

        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
               'interval': order_interval, 'timemode': timemode}
        
        trial_id = 'test'

        dump_flags = {'dump_blotters': False, 'dump_lobs': False, 'dump_strats': False,
                    'dump_avgbals': False, 'dump_tape': False}

        verbose = False
        ic(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
        try:
            tape_df = market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
        except Exception as e:
            ic('i am in exception')
            return fig_old, data_old, str(e), False

        # ic(tape_df)
        tape_df = tape_df.query('type == "Trade"')
        # ic(tape_df)
        pb1 = tape_df.party1.map(buyer_dictionary)
        pb2 = tape_df.party2.map(buyer_dictionary)
        pb3 = pb1.fillna(pb2)
        ps1 = tape_df.party1.map(seller_dictionary)
        ps2 = tape_df.party2.map(seller_dictionary)
        ps3 = ps1.fillna(ps2)

        tape_df['to_color1'] = pb3
        tape_df['to_color2'] = ps3
        # ic(tape_df)
        data = tape_df.loc[:, ['time', 'price', 'to_color1', 'to_color2']].to_json(orient='records')

        fig = px.scatter(tape_df, x="time", y="price", color='to_color1')
        fig.update_traces(mode="markers", hovertemplate="Time - %{x:.0f} Sec<br>Price - £ %{y}")
        fig.update_layout(yaxis_title='Price(£)',
            xaxis_title='Time(Sec)',modebar_orientation='v',legend=dict(
            title='Buyers' if segment == 'Buyers' else 'Sellers',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        return fig, data, dash.no_update, dash.no_update
    

    @callback(
        Output('bse-graph1', 'figure', allow_duplicate=True),
        Input('show-buyer-seller-segment', 'value'),
        State('storing-ps3-pb3', 'data'),
        prevent_initial_call=True
    )
    def update_sd_graph_legend(segment, data):
        # ic(data)
        tape_df = pd.read_json(data)
        if segment == 'Buyers':
            fig = px.scatter(tape_df, x="time", y="price", color='to_color1')
        else:
            fig = px.scatter(tape_df, x="time", y="price", color='to_color2')
        fig.update_traces(mode="markers", hovertemplate="Time - %{x:.0f} Sec<br>Price - £ %{y}")
        fig.update_layout(yaxis_title='Price(£)',
            xaxis_title='Time(Sec)',modebar_orientation='v',legend=dict(
            title='Buyers' if segment == 'Buyers' else 'Sellers',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        return fig
    
    @callback(
        Output('current-experiment-code', 'children'),
        Input('bse-code1-btn', 'n_clicks'),
        State({'type': 'bse-seller-type', 'index': ALL}, 'value'),
        State({'type': 'bse-seller-num', 'index': ALL}, 'value'),
        State({'type': 'bse-seller-SDRange', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-type', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-num', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-SDRange', 'index': ALL}, 'value'),
        State('bse-sd-scheduler-start', 'value'),
        State('bse-sd-scheduler-end', 'value'),
        State('bse-stepmode', 'value'),
        State('bse-sd-scheduler-order-interval', 'value'),
        State('bse-timemode', 'value'),
        State('show-buyer-seller-segment', 'value'),
        prevent_initial_call=True
    )
    def update_code(n, seller_type, seller_num, seller_range, buyer_type, buyer_num, buyer_range, sch_start, sch_end, sch_stepmode, order_interval, timemode, segment):
        buyers_spec =  [(type_, num_) for type_, num_  in zip(buyer_type, buyer_num)]
        sellers_spec =  [(type_, num_) for type_, num_  in zip(seller_type, seller_num)]
        traders_spec_str = "{'sellers':sellers_spec, 'buyers':buyers_spec}"

        # if len(seller_range) > 1:
        sup_range = [tuple(i) for i in seller_range]#(50, 100)
        # else:
        #     sup_range = tuple(seller_range[0])

        # if len(buyer_range) > 1:
        dem_range = [tuple(i) for i in buyer_range]#(50, 100)
        # else:
        #     dem_range = tuple(buyer_range[0])

        supply_schedule = "[{'from': start_time, 'to': end_time, 'ranges': sup_range, 'stepmode': stepmode}]"
        demand_schedule = "[{'from': start_time, 'to': end_time, 'ranges': dem_range, 'stepmode': stepmode}]"

        order_schedule = "{'sup': supply_schedule, 'dem': demand_schedule, 'interval': order_interval, 'timemode': timemode}"
        
        dump_flag = "{'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True, 'dump_avgbals': True, 'dump_tape': True}"

        code = f"""
sellers_spec = {sellers_spec}
num_sellers = {sum(seller_num)}
buyers_spec = {buyers_spec}
num_buyers = {sum(buyer_num)}
traders_spec = {traders_spec_str}

sup_range = {sup_range}
dem_range = {dem_range}

plot_sup_dem(num_sellers, sup_range, num_buyers, dem_range, '{sch_stepmode}')

start_time = {sch_start}
end_time = {sch_end}
stepmode = '{sch_stepmode}'
supply_schedule = {supply_schedule}
demand_schedule = {demand_schedule}

order_interval = {order_interval}
timemode = '{timemode}'
order_sched = {order_schedule}

trial_id = 'test_1'

dump_flags = {dump_flag}

verbose = False

# Now, run the market session
market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

plot_trades('test_1')
        """
        return code