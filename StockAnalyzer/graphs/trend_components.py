import plotly.express as px
from dash import dash_table
def main_trend(df,cols, title):
    fig = px.line(data_frame=df, title=title)

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