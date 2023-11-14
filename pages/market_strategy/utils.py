from ..common import *

def get_stock_data(stock, start_date):
    end_date = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    data = yf.download([stock], start=start_date, end=end_date)
    if data.shape[0] == 0:
        return data
    df = pd.date_range(start_date, end_date).to_frame()
    df=df.join(data)
    return df

def get_volume_case(df, factor=1):
    vol = df.Volume.to_frame()
    vol['shift1'] = vol['Volume'].shift(1)
    vol['shift2'] = vol['Volume'].shift(2)
    vol['case1'] = vol.apply(lambda x: x[0]<=x[1]*factor and x[1]<=x[2]*factor, axis=1)
    case1 = vol.loc[vol['case1']]
    return case1

def get_high_low_case(df, factor_bool=False):
    hldf = df[['High', 'Low']]
    factor = 0
    if factor_bool:    
        open = df.Open.tolist()[-1]
        if open>= 1000:
            factor = 0.01
        elif open >= 700:
            factor = 0.02
        elif open >= 400:
            factor = 0.03
        elif open>= 100:
            factor = 0.04
        else:
            factor = 0.05
    high_factor, low_factor = 1 + factor, 1 - factor
    hldf['highshift1'] = hldf['High'].shift(1)
    hldf['highshift2'] = hldf['High'].shift(2)
    hldf['lowshift1'] = hldf['Low'].shift(1)
    hldf['lowshift2'] = hldf['Low'].shift(2)
    hldf
    hldf['case2'] = hldf.apply(lambda x: x['High']<=x['highshift1']*high_factor and x['highshift1']<=x['highshift2']*high_factor and x['Low']>=x['lowshift1']*low_factor and x['lowshift1']>=x['lowshift2']*low_factor, axis=1)
    case2 = hldf.loc[hldf.case2]
    return case2

def main_fn(stock, date_from, Price, Mkt_Cap, name_of_stock):
    #getting data from yfinance
    df = get_stock_data(stock, date_from)
    if df.shape[0] == 0:
        return None

    #resampling to Weekly data
    ohlc_dict = {
        'Open':'first',
        'High':'max',
        'Low':'min',
        'Close':'last',
        'Volume':'sum'
        }
    dfw = df.resample('W-Fri').agg(ohlc_dict)


    #with lineancy
    #applying volume case
    case_v = get_volume_case(dfw)

    #applying high_low case
    case_hl = get_high_low_case(dfw)

    #joining 
    final_case = case_v.join(case_hl, how='inner')
    # ic(final_case).

    # with lineancy
    ## applying volume case
    case_v = get_volume_case(dfw, factor=1.2)

    ## applying high_low case
    case_hl = get_high_low_case(dfw, factor_bool=True)

    #joining 
    final_case2 = case_v.join(case_hl, how='inner')


    #plotting graph
    fig = make_subplots(rows=2, cols=1, row_heights=[0.8,0.2], shared_xaxes=True, vertical_spacing=0)

    fig.add_trace(go.Candlestick(x=dfw.index,open=dfw['Open'],high=dfw['High'],low=dfw['Low'],close=dfw['Close'],
                                             name=''), row=1, col=1)
    
    fig.add_trace(go.Bar(x=dfw.index, y=dfw['Volume']), row=2, col=1)
    ic(final_case.index.tolist(), final_case2.index.tolist())
    for i in final_case2.index.tolist():
        fig.add_shape(
                x0=i, x1=i, y0=0, y1=1, xref='x', yref='paper', line=dict(color='blue',), type='line',
                line_width=0.3)
    for i in final_case.index.tolist():
        fig.add_shape(
                x0=i, x1=i, y0=0, y1=1, xref='x', yref='paper', line=dict(color='Yellow',), type='line',
                line_width=1)
    
        
    fig.update_xaxes(
        visible=True,
        rangeslider={'visible':False},
        showspikes=False, spikemode='across', spikesnap='cursor',
        showgrid=False, zeroline=True, gridwidth=1, gridcolor='#3E464E', zerolinewidth=3, zerolinecolor='#3E464E'
    )
    fig.update_layout(
        margin={'l':0, 'b':0, 't':40},
        title = f'{name_of_stock.tolist()[0]} - {int(Price)} - {int(Mkt_Cap)}'
    )

    return fig




