from dash import Dash
from dash_html_components import Div, H1, P, H3
from dash_core_components import Graph

app = Dash(__name__)

app.layout = Div(
    children=[
        H1("ola mundo"), 
        P('Bem vindo ao dash_2'),
        H3('grafico de pizza'),
        Graph(
            figure={
                'data': [
                    {'x': [1, 2, 3, 4]}
                        ]
                   }     
            )  
            ]

)

app.run_server(debug = True) 