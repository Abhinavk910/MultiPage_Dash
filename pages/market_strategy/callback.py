from ..common import *
from .utils import *

def register_callback():

    @callback(
        Output('stock-name', 'data'),
        Input('range-slider-mkt-cap', 'value'),
        Input('range-slider-price', 'value'),
    )
    def get_stock(mkt_cap,price):
        df = pd.read_csv('assets/stock_data2.csv')
        fd = df.query('Mkt_Cap >= @mkt_cap[0] and Mkt_Cap <= @mkt_cap[1] and Price >= @price[0] and Price <= @price[1]')
        return fd.Symbol.tolist()
        

    @callback(
        Output('graph-output1', 'figure'),
        Output("alert-dismiss", "hide"),
        Input('run-check1', 'n_clicks'),
        State('stock-name', 'value'),
        State('date-picker1', 'value'),
        prevent_initial_call=True
    )
    def runit(n, stock_name, date_value):
        if stock_name == '':
            return dash.no_update, False
        df = pd.read_csv('assets/stock_data2.csv')
        st = df.query('Symbol == @stock_name')
        # ic(st.columns)
        fig = main_fn(stock_name, date_value, st.Price, st.Mkt_Cap, st.Name)
        if fig:
            return fig, True
        else:
            return dash.no_update, False
    
   