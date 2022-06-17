from datetime import datetime as dt
from loggers import logger as lg
from dash import dcc, html, Input, Output, callback, long_callback, dash_table, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import re
import yfinance as yf
from graphs import trend_components as tc
from dash_bootstrap_templates import ThemeChangerAIO
from components.reusable import nav, controls, table_trend_data, table_balance_sheet
import pandas as pd

header = html.H4(
    "Stock Analysis Dashboard", className="bg-primary text-white p-2 mb-2 text-center"
)



tab1 = dbc.Tab([

    dcc.Graph(id="container-main-trend")
    ],label="Graph")
tab2 = dbc.Tab([table_trend_data], label="Trend Data", className="p-4")
tab3 = dbc.Tab([table_balance_sheet], label="Stock Info", className="p-4")
tabs = dbc.Tabs([tab1, tab2, tab3])

store = dcc.Store(id='session-data')
bs_store = dcc.Store(id='session-bs')

layout = dbc.Container(
    [
        store,
        bs_store,
        header,
        nav,
        dcc.Loading([], type='graph',id='main-loader',fullscreen=True,style={'opacity':'70%'}),
        dbc.Row(
            [
                dbc.Col([ThemeChangerAIO(aio_id="theme"),controls], width=4),
                dbc.Col(tabs, width=8),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)


@callback(
    Output('session-data','data'),
    Output('session-bs','data'),
    Output('main-loader','className'),
    Input('butt-stock-data','n_clicks'),
    State('period-dropdown','value'),
    State('tickers','value'),
    State('metric-dropdown','value')
)
def fetch_data(nclicks, period, tickers, metric):
    if nclicks in [0, None]:
        raise PreventUpdate
    else:
        #get tickers into list
        t = re.split(r"-|,|\n|\s+",tickers)
        #fetch trend data for graph
        #data for our summary tables. For this example we will hard code in Financials and Balancesheet.
        #A better method would be a select list for a user to choose which to view and then cahce locally
        balance_sheet = pd.DataFrame()
        ticker_obj = yf.Tickers(tickers)
        for i, t in enumerate(list(ticker_obj.tickers.keys())):
            inf = ticker_obj.tickers[t].info
            try:
                if i == 0:
                    balance_sheet['Attribute'] = list(inf.keys())
                    balance_sheet[t] = list(inf.values())
                else:
                    balance_sheet[t] = list(inf.values())
            except ValueError as e:
                lg.log('An issue occured on {}: {}'.format(dt.strftime(dt.now(),'%Y-%m-%d'),e),'ERROR')
        data_trend = ticker_obj.download(period=period)
        data_trend = data_trend[metric].to_json(orient='index')
        return data_trend, balance_sheet.to_json(orient='records'), str(nclicks)


@callback(
    Output('container-main-trend','figure'),
    Input('session-data','data'),
    State('period-dropdown','value'),
    State('tickers','value'),
    State('metric-dropdown','value')
)
def update_chart(data, period, tickers, metric):
    t = re.split(r"-|,|\n|\s+",tickers)
    data = pd.read_json(data).T
    title = '<b>{}</b><br>Over the last: {}'.format(metric, period)
    chart = tc.main_trend(df=data,cols=t,title=title)
    return chart

@callback(
    Output('table-trend','data'),
    Output('table-trend','columns'),
    Input('session-data','data')
)
def datatable(data):
    df = pd.read_json(data).T
    df['Date'] = df.index
    cols = [
        {"name":i, "id": i} for i in df.columns
    ]
    df = df.applymap(lambda x: 'NA' if x==[] else x)
    return df.to_dict('records'),cols


@callback(
    Output('table-bs','data'),
    Output('table-bs','columns'),
    Input('session-bs','data')
)
def datatable_bs(data):
    df = pd.read_json(data, orient='records')
    cols = [
        {"name":i, "id": i} for i in df.columns
    ]
    df = df.applymap(lambda x: 'NA' if x==[] else x)
    return df.to_dict('records'),cols