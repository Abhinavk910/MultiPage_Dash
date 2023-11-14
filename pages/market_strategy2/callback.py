from ..common import *
from .utils import *

def register_callback():

    @callback(
        Output('stock-name2', 'data'),
        Input('range-slider-mkt-cap2', 'value'),
        Input('range-slider-price2', 'value'),
        Input('select-case2', 'value'),
    )
    def get_stock(mkt_cap,price, cases):
        df = pd.read_csv('assets/2023-10-16.csv')
        df.rename(columns={'0':'Symbol'}, inplace=True)
        for i in cases:
            df = df.query('case == @i')
        df2 = pd.read_csv('assets/stock_data2.csv')
        fdf = df.merge(df2, on='Symbol', how='inner')
        fd = fdf.query('Mkt_Cap >= @mkt_cap[0] and Mkt_Cap <= @mkt_cap[1] and Price >= @price[0] and Price <= @price[1]')
        return fd.Symbol.tolist()
        

    @callback(
        Output('graph-output2', 'figure'),
        Output("alert-dismiss2", "hide"),
        Input('run-check2', 'n_clicks'),
        State('stock-name2', 'value'),
        State('date-picker2', 'value'),
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
    
   