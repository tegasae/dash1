
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import sqlite3
import datetime

from dash import Dash, html
import pandas as pd
from dash.dash_table import DataTable





conn = sqlite3.connect('telebot.db')
date_now=datetime.date.today().isoformat()
date_now= (datetime.date.today() - datetime.timedelta(days=2)).isoformat()
query=(
f"SELECT u.name, STRFTIME('%H:%M',min(l.time_s)), "
f"CASE when l.client is not NULL then l.client "
f"when l.client is NULL then l.synonym  "
f"else NULL "
f"end as client_name "
f"from users u left join log l "
f"on u.user_id =l.user_id and date(l.time_s)='{date_now}' and STRFTIME('%H',l.time_s)>'08' "
f"where  u.status =2 and u.confirmed =2 group by u.name")
df = pd.read_sql_query(query, conn)
df.columns=["Имя", "Время начала","Клиент"]
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
style_data_conditional = [
    {
        # Highlight rows where "Время начала" is empty
        'if': {
            'filter_query': '{Время начала} = ""',  # Check for empty string
            'column_id': 'Время начала'
        },
        'backgroundColor': '#FFFFFF',  # Yellow background
        'color': '#000000',  # Black text
    },
    {
        # Highlight rows where "Время начала" is greater than "09:15"
        'if': {
            'filter_query': '{Время начала} > "09:15"',  # Compare time as string
            'column_id': 'Время начала'
        },
        'backgroundColor': '#FFCCCC',  # Light red background
        'color': '#FF0000',  # Red text
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