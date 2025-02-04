
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import sqlite3
import datetime

from dash import Dash, html
import pandas as pd
from dash.dash_table import DataTable





conn = sqlite3.connect('telebot.db')
date_now=datetime.date.today().isoformat()
query=(f"select u.name, STRFTIME('%H:%M',(select time_s from log l where l.user_id=u.user_id and date(time_s)='{date_now}' "
       f"and  strftime('%H', l.time_s)>='08')) from users u where status =2 and confirmed =2")
df = pd.read_sql_query(query, conn)
df.columns=["Имя", "Время начала"]
df["Время начала"] = df["Время начала"].fillna("No Data")
conn.close()
dt=DataTable(
        id='dataframe-table',
        columns=[
            {"name": i, "id": i} for i in df.columns
        ],
    data=df.to_dict('records'),  # Convert DataFrame to list of dictionaries
    style_table={'overflowX': 'auto','witdh':'50%'},
    style_cell={'textAlign': 'left'},
    page_size=15,  # Pagination: Show 5 rows per page
    sort_action="native",  # Enable sorting by clicking on column headers
    filter_action="native",  # Enable filtering by entering text in column headers
    style_header={
            'backgroundColor': '#f4f4f4',  # Light gray header background
            'fontWeight': 'bold',
        },
    style_data_conditional=[
{
            # Highlight rows where "Время time" equals "09:11"
            'if': {
                'filter_query': '{Время начала} =""',  # Correct filter_query syntax
                'column_id': 'Время начала'
            },
            'backgroundColor': '#FFFF00',  # Light red background color
            'color': '#000000',  # Red text color
        },
        {
            # Highlight rows where "Время time" equals "09:11"
            'if': {
                'filter_query': '{Время начала} > "09:15"',  # Correct filter_query syntax
                'column_id': 'Время начала'
            },
            'backgroundColor': '#FFCCCC',  # Light red background color
            'color': '#FF0000',  # Red text color
        },

    ]
)

def generate_table(dataframe, max_rows=10):

    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col],  style={'background-color': '#66c2a5'}) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])




app = Dash()

app.layout = html.Div([
    html.H4(children=f'Первая отметка о начале работ {date_now}'),
    #generate_table(df),
    dt

])

if __name__ == '__main__':
    app.run(debug=True)