from ..common import *
from ..components import *
from .utils import *

def register_callbacks():

    @callback(
        Output('bse-paper-buyer', 'children'),
        Input('bse-add-new-buyer', 'n_clicks'),
        Input('bse-delete-new-buyer', 'n_clicks'),
        State('bse-paper-buyer', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-buyer':
            Ends = child[-3:]
            above = child[:-3]
            index_no = len(above) - 1
            type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
            buyer_type = select(id={'type': 'bse-buyer-type', 'index': index_no}, data=type_options, value="ZIP", label="Select Type of Buyer", righticon="", persistance=False)
            buyer_num = numberinput(id={'type': 'bse-buyer-num', 'index': index_no}, label='Select No of Buyer', min=1, max=99,step=1, value=5)
            buyer_group = group(children=[buyer_type, buyer_num], position='left')
            child = above + [buyer_group] + Ends
            return child
        elif trig == 'bse-delete-new-buyer':
            Ends = child[-3:]
            above = child[:-4]
            if len(above) == 1:
                raise PreventUpdate
            else:    
                child = above + Ends
                return child



    @callback(
        Output('bse-paper-seller', 'children'),
        Input('bse-add-new-seller', 'n_clicks'),
        Input('bse-delete-new-seller', 'n_clicks'),
        State('bse-paper-seller', 'children'),
        prevent_initial_call=True
    )
    def add_new_payer(n1, n2, child):
        trig = ctx.triggered_id
        if trig == 'bse-add-new-seller':
            Ends = child[-3:]
            above = child[:-3]
            index_no = len(above) - 1
            type_options = ["ZIP", "ZIC", "SHVR", "GVWY", "SNPR", "PRZI", "PRSH", "PRDE"]
            buyer_type = select(id={'type': 'bse-seller-type', 'index': index_no}, data=type_options, value="ZIP", label="Select Type of Seller", righticon="", persistance=False)
            buyer_num = numberinput(id={'type': 'bse-seller-num', 'index': index_no}, label='Select No of Seller', min=1, step=1, value=5)
            buyer_group = group(children=[buyer_type, buyer_num], position='left')
            child = above + [buyer_group] + Ends
            return child
        elif trig == 'bse-delete-new-seller':
            Ends = child[-3:]
            above = child[:-4]
            if len(above) == 1:
                raise PreventUpdate
            else:    
                child = above + Ends
                return child
        
    @callback(
        Output('bse-graph1', 'figure', allow_duplicate=True),
        Output('storing-ps3-pb3', 'data'),
        Output('graph-throwing-any-error1', 'children'),
        Output('graph-throwing-any-error1', 'hide'),
        Input('bse-graph1-btn', 'n_clicks'),
        State({'type': 'bse-seller-type', 'index': ALL}, 'value'),
        State({'type': 'bse-seller-num', 'index': ALL}, 'value'),
        State('bse-seller-SDRange', 'value'),
        State({'type': 'bse-buyer-type', 'index': ALL}, 'value'),
        State({'type': 'bse-buyer-num', 'index': ALL}, 'value'),
        State('bse-buyer-SDRange', 'value'),
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
        # ic(n, seller_type, seller_num, seller_range, buyer_type, buyer_num, buyer_range, sch_start, sch_end, sch_stepmode, order_interval, timemode)
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


        sup_range = tuple(seller_range)#(50, 100)
        dem_range = tuple(buyer_range)

        start_time = sch_start
        end_time = sch_end
        supply_schedule = [{'from': start_time, 'to': end_time, 'ranges': [sup_range], 'stepmode': sch_stepmode}]
        demand_schedule = [{'from': start_time, 'to': end_time, 'ranges': [dem_range], 'stepmode': sch_stepmode}]

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

        ic(tape_df)
        tape_df = tape_df.query('type == "Trade"')
        ic(tape_df)
        pb1 = tape_df.party1.map(buyer_dictionary)
        pb2 = tape_df.party2.map(buyer_dictionary)
        pb3 = pb1.fillna(pb2)
        ps1 = tape_df.party1.map(seller_dictionary)
        ps2 = tape_df.party2.map(seller_dictionary)
        ps3 = ps1.fillna(ps2)

        tape_df['to_color1'] = pb3
        tape_df['to_color2'] = ps3
        ic(tape_df)
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