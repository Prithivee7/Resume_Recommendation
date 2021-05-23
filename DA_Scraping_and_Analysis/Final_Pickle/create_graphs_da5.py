from typing import Dict
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle


df1 = pd.read_pickle(r'fifth_dict_da.pickle')

dict_da_1 = dict(sorted(df1.items(), key=lambda x: x[1], reverse=True)[10:20])

for i in dict_da_1:
    print(i, dict_da_1[i])

dict_da_1_final = dict(
    sorted(dict_da_1.items(), key=lambda x: x[1], reverse=True))


x_list = list(dict_da_1_final.values())
y_list = list(dict_da_1_final.keys())


x_list = [i for i in x_list]
y_list = [i.capitalize() for i in y_list]

y_list = ['SQL' if i == 'Sql' else i for i in y_list]
y_list = ['ML' if i == 'Ml' else i for i in y_list]
y_list = ['API' if i == 'Api' else i for i in y_list]
y_list = ['Statistics' if i == 'Stat' else i for i in y_list]
percent = [str(int((i/306) * 100))+"%" for i in x_list]
fig1 = go.Figure(go.Bar(
    x=x_list,
    y=y_list,
    text=percent,
    textposition='outside',
    orientation='h'
))
fig1.update_layout(
    title={
        'text': "Extracted from 306 Job Requirements",
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


def figures_to_html(figs, filename="data_analyst5.html"):
    dashboard2 = open(filename, 'w')
    dashboard2.write("<html><head></head><body>" + "\n")
    for fig in figs:
        dashboard2.write(
            '<h2 style="text-align: center">Top 10 skills for data analyst for experience of more than 12 years in 2021</h2>')
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard2.write(inner_html)
    dashboard2.write("</body></html>")


figures_to_html([fig1])
