from dash import dcc, html, Input, Output, callback, dash_table, State
import dash_bootstrap_components as dbc

nav = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("GitHub",href='https://github.com/Allenh513/Analytics')),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem("Market Summary",href="/"),
            dbc.DropdownMenuItem("Analysis",href="/analysis")
        ],
        nav=True,
        in_navbar=True,
        label="Navigation"
    )
],
    brand="AH-Analytics",
    brand_href="#",
    color="secondary",
    dark=True,
    style={'margin-bottom':'.5em'}

)

ticker_area = html.Div([
    dbc.Label('Market Summary'),
    dcc.Textarea(
        title='Enter Tickers',
        id='tickers',
        style={
            'width': '100%',
            'height': 200
        },
    )
    ],className='mb-4'
)
period_dropdown = html.Div([
    dcc.Dropdown({
        '1d':'1d',
        '5d':'5d',
        '1mo':'1mo',
        '3mo':'3mo',
        '6mo':'6mo',
        '1y':'1y',
        '5y':'5y',
        'max':'max',
        'ytd':'ytd'
    },
        id='period-dropdown',placeholder='Select Time Period')
    ], className='mb-4'
)
metric_dropdown = html.Div([
    dcc.Dropdown({
        'Close':'Close',
        'High':'High',
        'Low':'Low',
        'Open':'Open',
        'Volume':'Volume'
    },className='mb-4', id='metric-dropdown', placeholder='Select Metric')
    ]
)
data_button = html.Div([
    html.Button(
        'Fetch Data',
        id='butt-stock-data',
        n_clicks=0,
        className='btn btn-outline-primary'
    ),
    ], className='mb-4'
)

controls = dbc.Card([ticker_area, period_dropdown, metric_dropdown, data_button], body=True,)

table_trend_data = dash_table.DataTable(
        id="table-trend",
        page_size=15,
        editable=False,
        cell_selectable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
        export_headers="display",
        export_format="xlsx"
    )


table_balance_sheet = dash_table.DataTable(
        id="table-bs",
        page_size=25,
        editable=False,
        cell_selectable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
        export_headers="display",
        export_format="xlsx"
    )