import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd   
import plotly.graph_objs as go  

df = pd.read_csv('tourist_data_csv.csv', index_col=0)
df = df.dropna()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            figure = {
                'data':[
                    go.Scatter(
                        x = df.index,  
                        y = df['日帰り'],   
                        name = '日帰り人数',
                        stackgroup='one'
                    ),
                    go.Scatter(
                        x = df.index,
                        y = df['宿泊'],
                        name = '宿泊人数',
                        stackgroup='one'
                    )  
                ],
                'layout':
                    go.Layout(
                        height = 600,

                    )
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)