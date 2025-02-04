from dash import Dash
from dash_html_components import Div, H1, P

app = Dash(__name__)

app.layout = Div(
    children=[
        H1("ola mundo"), 
        P('Bem vindo ao dash2_')
    ]
)

app.run_server(debug = True) 