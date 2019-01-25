import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd   
import plotly.graph_objs as go  

df = pd.read_csv('kyoto_hotel_cumsum.csv', index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            figure = {
                'data':[
                    go.Scatter(
                        x = df.index,  
                        y = df['cumsum'],   
                        name = '宿泊所累計',
                    ),
                    go.Bar(
                        x = df.index,
                        y = df['count'],
                        name = '年間登録件数',
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