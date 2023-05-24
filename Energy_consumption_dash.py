import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#loads the dataset
data =  pd.red_csv('')

#Create a dash application
app = dash.Dash(__name__)

#create an app layout
app.layout = html.Div(children=[html.H1()]
    
)