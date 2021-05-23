from typing import Dict
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle


df1 = pd.read_pickle(r'fourth_dict_da.pickle')

dict_da_1 = dict(sorted(df1.items(), key=lambda x: x[1], reverse=True)[1:11])


dict_da_1_final = dict(
    sorted(dict_da_1.items(), key=lambda x: x[1], reverse=True))


x_list = list(dict_da_1_final.values())
y_list = list(dict_da_1_final.keys())


x_list = [i for i in x_list]
y_list = [i.capitalize() for i in y_list]

y_list = ['CI' if i == 'Ci' else i for i in y_list]
y_list = ['AI' if i == 'Ai' else i for i in y_list]
y_list = ['BI' if i == 'Bi' else i for i in y_list]
y_list = ['Statistics' if i == 'Stat' else i for i in y_list]
percent = [str(int((i/1400) * 100))+"%" for i in x_list]
fig1 = go.Figure(go.Bar(
    x=x_list,
    y=y_list,
    text=percent,
    textposition='outside',
    orientation='h'
))
fig1.update_layout(
    title={
        'text': "Extracted from 1400 Job Requirements",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis=dict(
        title='Top skills',
        autorange="reversed"
    ),
    xaxis=dict(
        title='Number of Occurences',
    )
)
fig1.update_layout(
    autosize=False,
    width=1500,
    height=690,)


def figures_to_html(figs, filename="data_analyst4.html"):
    dashboard2 = open(filename, 'w')
    dashboard2.write("<html><head></head><body>" + "\n")
    for fig in figs:
        dashboard2.write(
            '<h2 style="text-align: center">Top 10 skills for data analyst for experience of 8 to 11 years in 2021</h2>')
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard2.write(inner_html)
    dashboard2.write("</body></html>")


figures_to_html([fig1])
