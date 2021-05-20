from typing import Dict
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle


df1 = pd.read_pickle(r'first_dict_da.pickle')

dict_da_1 = dict(sorted(df1.items(), key=lambda x: x[1], reverse=True)[5:28])


for i in dict_da_1:
    if(i == "ml"):
        dict_da_1["machine learning"] += dict_da_1["ml"]
    if(i == "math"):
        dict_da_1["stat"] += dict_da_1["math"]

dict_da_1.pop('ml', None)
dict_da_1.pop('math', None)
dict_da_1.pop('model', None)
dict_da_1.pop('vision', None)
dict_da_1.pop('css', None)
dict_da_1.pop('api', None)
dict_da_1.pop('deployment', None)
dict_da_1.pop('testing', None)
dict_da_1.pop('git', None)
dict_da_1.pop('business intelligence', None)
dict_da_1.pop('testing', None)
dict_da_1.pop('analytics', None)
dict_da_1.pop('dl', None)

dict_da_1_final = dict(
    sorted(dict_da_1.items(), key=lambda x: x[1], reverse=True))

for i in dict_da_1_final:
    print(i, dict_da_1_final[i])


x_list = list(dict_da_1_final.values())
y_list = list(dict_da_1_final.keys())


x_list = [i*3 for i in x_list]
y_list = [i.capitalize() for i in y_list]
percent = [str(int((i/6800) * 100))+"%" for i in x_list]
fig1 = go.Figure(go.Bar(
    x=x_list,
    y=y_list,
    text=percent,
    textposition='outside',
    orientation='h'
))
fig1.update_layout(
    title={
        'text': "Extracted from 6800 Job Requirements",
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


def figures_to_html(figs, filename="data_analyst1.html"):
    dashboard2 = open(filename, 'w')
    dashboard2.write("<html><head></head><body>" + "\n")
    for fig in figs:
        dashboard2.write(
            '<h2 style="text-align: center">Top 10 skills for data analyst for experience of 0-2 years in 2021 April</h2>')
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard2.write(inner_html)
    dashboard2.write("</body></html>")


figures_to_html([fig1])
