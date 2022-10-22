#Libraries
from operator import ge
import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, dcc  
import dash_bootstrap_components as dbc 

#Dataset
bands = pd.read_csv("finishedbands.csv")
german_bands = bands[bands["Country"] == "Germany"]
swedish_bands = bands[bands["Country"] == "Sweden"]
finnish_bands = bands[bands["Country"] == "Finland"]
british_bands = bands[bands["Country"] == "United Kingdom"]
danish_bands = bands[bands["Country"] == "Denmark"]
countries = ["Germany","Sweden","Finland","United Kingdom","Denmark & Territories",
            "Norway", "Italy", "France", "Ireland", "Hungary", "Switzerland", "Austria",
            "Netherlands", "Poland", "Russia", "Spain", "Belgium"]
n_of_bands = [37, 18, 13, 8, 4, 8, 5, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]
year_ger_bands_sorted = [1980, 1983, 1984, 1989, 1992, 1993, 1995, 1996, 1998,
 1999, 2000, 2001, 2003, 2004, 2005, 2006, 2008, 2009, 2011, 2012, 2019]
ger_bands_sorted = [1, 2, 1, 2, 1, 1, 3, 1, 2, 2, 1, 3, 2, 2, 2, 1, 2, 1, 1, 1, 1]
british_bands_by_year = british_bands[["Band Name", "Year Formed"]].sort_values("Year Formed")


#App

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
mytitle = dcc.Markdown(children="Erik's Metal Bands")
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Main Bands', "German Bands", "Swedish Bands", 
    "Finnish Bands", "Danish Bands", "Uk's Bands"],
                        value='Main Bands',
                        clearable=False)

#Layout

app.layout = dbc.Container([mytitle, mygraph, dropdown])


@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):
    if user_input == 'Main Bands':
        fig = px.pie(data_frame=bands, values=n_of_bands, names=countries,
         title= "Main European Bands", hole=.3)
        
    
    elif user_input == 'German Bands':
        fig = fig = px.bar(german_bands, x=year_ger_bands_sorted, y=ger_bands_sorted,  
         title="German Bands formed by Year")

    elif user_input == 'Swedish Bands':
        fig = fig = go.Figure(data=[go.Pie( title= "Swedish Bands N° of Albums",
        labels=swedish_bands["Band Name"], values=swedish_bands["N° of Albums"],
        pull=[0.2,0.1,0,0,0.3,0,0,0,0,0,0.2,0,0,0,0.1,0.1,0])])


    elif user_input == 'Finnish Bands':
        fig = px.histogram(finnish_bands, x=finnish_bands["Band Name"],
        y=finnish_bands["Spotify Listeners"],  color=finnish_bands["Band Name"],
        title= "Finnish bands Spotify Monthly Listeners")

    elif user_input == 'Danish Bands':
        fig =go.Figure(go.Sunburst(
        labels=["Bands", "Faroese Bands", "Týr", "Heljareyga", "Danish Bands", "Vanir","Svartsot","Danheim"],
        parents=["", "Bands", "Faroese Bands", "Faroese Bands", "Bands", "Danish Bands", "Danish Bands", "Danish Bands" ],
        values=[10, 4, 10, 10, 8, 6, 6, 6],))
        fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    elif user_input == "Uk's Bands":
        fig = px.line(british_bands, x=british_bands_by_year["Band Name"], y=british_bands_by_year["Year Formed"],  
        title="Uk's Bands by Year Formed")


    return fig 



if __name__ == "__main__":
    app.run(debug=True)