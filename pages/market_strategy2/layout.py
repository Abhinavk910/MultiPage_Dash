from ..common import *

def create_layout():
    df = pd.read_csv('assets/2023-10-16.csv')
    ic(df.columns)
    df.rename(columns={'0':'Symbol'}, inplace=True)
    df2 = pd.read_csv('assets/stock_data2.csv')
    ic(df2.columns, df2.head(1))
    fdf = df.merge(df2, on='Symbol', how='inner')
    price_max, price_min = fdf.Price.max(), fdf.Price.min()
    mkt_max, mkt_min = fdf.Mkt_Cap.max(), fdf.Mkt_Cap.min()
    return dmc.Container(
        children=[
            dmc.Stack(
                mt=40,
                children=[
                    dmc.MultiSelect(
                        data = ['strict', 'some_strict'],
                        value = ['strict', 'some_strict'],
                        label = 'Select case',
                        id = 'select-case2'
                    ),
                    dmc.Text('Market Cap'),
                    dmc.RangeSlider(
                        id="range-slider-mkt-cap2",
                        w=1000,
                        max = mkt_max,
                        min = mkt_min,
                        value=[mkt_min, mkt_max],
                        marks=[
                            {"value": mkt_min, "label": str(mkt_min)},
                            {"value": mkt_max, "label": str(mkt_max)},
                        ],
                        mb=5,
                    ),
                    dmc.Text('Price'),
                    dmc.RangeSlider(
                        id="range-slider-price2",
                        w=1000,
                        max = 5000,
                        min = price_min,
                        value=[price_min, 5000],
                        marks=[
                            {"value": price_min, "label": str(price_min)},
                            {"value": 5000, "label": str(5000)}
                        ],
                        mb=35,
                    ),
                ]
            ),
            dmc.Group(
                m=10,
                children=[
                    dmc.Select(
                        label='Provide STOCK SYMBOL',
                        id='stock-name2',
                        w=150,
                        searchable=True,
                        # data = stock_list,
                    ),
                    dmc.DatePicker(
                        id="date-picker2",
                        label="Start Date",
                        description="Date from which strategy will apply",
                        maxDate=datetime.now()-timedelta(days=365),
                        value=date(2021, 1, 1),
                        style={"width": 200},
                    ),
                    dmc.Button(id='run-check2', children=['Run']),
                ]
            ),
            dmc.Alert(
                "Wrong Stock Name or timezone not included",
                title="Bummer!",
                id="alert-dismiss2",
                color="red",
                withCloseButton=True,
                hide=True
            ),
            dcc.Graph(id='graph-output2')
        ]
    )
