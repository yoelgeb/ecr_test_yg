from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

headers = ['country','continent','year','lifeExp','pop','gdpPercap']

country_data_list = [['Canada','Americas',1950,68.28,14011422,10581.26552],
                        ['Canada','Americas',1951,68.55,14330675,10932.46678],
                        ['Canada','Americas',1952,68.75,14785584,11367.16112],
                        ['Canada','Americas',1953,69.13,15183375,11586.61455],
                        ['Canada','Americas',1954,69.39,15606744,11839.97948],
                        ['Canada','Americas',1955,69.69,16048021,12040.24253],
                        ['Canada','Americas',1956,69.95,16515244,12299.63486],
                        ['Canada','Americas',1957,70.25,17010154,12440.17937],
                        ['Canada','Americas',1958,70.45,17519212,12618.32141],
                        ['Canada','Americas',1959,70.75,18044056,12863.89202],
                        ['Canada','Americas',1960,71.05,18584172,13081.99825],
                        ['Canada','Americas',1961,71.45,19140048,13462.48555],
                        ['Canada','Americas',1962,71.75,19711214,13877.89939],
                        ['Canada','Americas',1963,72.05,20297755,14270.28025],
                        ['Canada','Americas',1964,72.45,20898210,14647.88156],
                        ['Canada','Americas',1965,72.85,21512196,15040.71078],
                        ['Canada','Americas',1966,73.25,22139679,15523.27645],
                        ['Canada','Americas',1967,73.65,22780697,16076.58803],
                        ['Canada','Americas',1968,74.05,23435961,16709.58368],
                        ['Canada','Americas',1969,74.45,24105257,17430.60125],
                        ['Canada','Americas',1970,74.85,24785512,18154.40526],
                        ['Canada','Americas',1971,75.25,25476321,19018.74046],
                        ['Canada','Americas',1972,75.65,26176096,20099.90787],
                        ['Canada','Americas',1973,76.05,26884524,21308.38425]]

df = pd.DataFrame(country_data_list ,columns = headers)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run_server(debug=True,
                    port=8050,
                    host='0.0.0.0')