import plotly.express as px
from dash import dash_table
import plotly.graph_objects as go

def main_trend(df, tickers,has_model,model):
    charts = list()
    for t in tickers:
        charts.append(
            go.Candlestick(
                x=df.index,
                open=df["('Open', '{}')".format(t)],
                high=df["('High', '{}')".format(t)],
                low=df["('Low', '{}')".format(t)],
                close=df["('Close', '{}')".format(t)],
                name=t,
                legendgroup=t,
                increasing={'fillcolor':'#009E73'},
                decreasing={'fillcolor':'#D55E00'}
            )
        )
    fig = go.Figure(data=charts)

    if has_model:
        if model['TYPE'] == 'Simple Moving Average':
            for t in tickers:
                df['Avg {}'.format(t)] = (df["('High', '{}')".format(t)] + df["('Low', '{}')".format(t)]) / 2
                fig.add_trace(go.Scatter(
                    x=df.index,
                    y=df['Avg {}'.format(t)].rolling('{}D'.format(model['MA_INPUT'])).mean(),
                    mode='lines',
                    name='{} {} Day MA'.format(t, model['MA_INPUT']),
                    legendgroup=t,
                    fillcolor='#3f3c59'
                ))
        fig.update()
    return fig

def data_table(data):
    table = dash_table.DataTable(
        id="table",
        columns=[{"name": i, "id": i, "deletable": True} for i in data.columns],
        data=data.to_dict("records"),
        page_size=10,
        editable=False,
        cell_selectable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
    )
    return table

def add_forecast_sma(data,interval,tickers):
    df=data
    trace = list()
    charts = list()
    for t in tickers:
        charts.append(
            go.Candlestick(
                x=df.index,
                open=df["('Open', '{}')".format(t)],
                high=df["('High', '{}')".format(t)],
                low=df["('Low', '{}')".format(t)],
                close=df["('Close', '{}')".format(t)],
                name=t,
                legendgroup=t
            )
        )
    fig = go.Figure(data=charts)
    for t in tickers:
        df['Avg {}'.format(t)] = (df["('High', '{}')".format(t)] + df["('Low', '{}')".format(t)])/2
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['Avg {}'.format(t)].rolling('{}D'.format(interval)).mean(),
            mode='lines',
            name='{} {} Day MA'.format(t,interval),
            legendgroup=t
        ))
    fig.update()
    return fig