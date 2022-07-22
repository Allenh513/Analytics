from dash import Dash, dcc, html, Input, Output, callback
from pages import main
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

app = DashProxy(__name__
                ,external_stylesheets=[dbc.themes.DARKLY, dbc_css],
                suppress_callback_exceptions=True,
                transforms=[MultiplexerTransform()],
                prevent_initial_callbacks=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return main.layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)