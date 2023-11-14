from ..common import *

def create_layout():
    df = pd.read_csv('assets/stock_data2.csv')
    price_max, price_min = df.Price.max(), df.Price.min()
    mkt_max, mkt_min = df.Mkt_Cap.max(), df.Mkt_Cap.min()
    return dmc.Container(
        children=[
            dmc.Stack(
                mt=40,
                children=[
                    dmc.Text('Market Cap'),
                    dmc.RangeSlider(
                        id="range-slider-mkt-cap",
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
                        id="range-slider-price",
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
                        id='stock-name',
                        w=150,
                        searchable=True,
                        # data = stock_list,
                    ),
                    dmc.DatePicker(
                        id="date-picker1",
                        label="Start Date",
                        description="Date from which strategy will apply",
                        maxDate=datetime.now()-timedelta(days=365),
                        value=date(2021, 1, 1),
                        style={"width": 200},
                    ),
                    dmc.Button(id='run-check1', children=['Run']),
                ]
            ),
            dmc.Alert(
                "Wrong Stock Name or timezone not included",
                title="Bummer!",
                id="alert-dismiss",
                color="red",
                withCloseButton=True,
                hide=True
            ),
            dcc.Graph(id='graph-output1')
        ]
    )
