from typing import Dict
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import pickle


df1 = pd.read_pickle(r'third_dict_da.pickle')

dict_da_1 = dict(sorted(df1.items(), key=lambda x: x[1], reverse=True)[20:])


dict_da_1.pop('ml', None)
dict_da_1.pop('math', None)
# dict_da_1.pop('model', None)
dict_da_1.pop('vision', None)
dict_da_1.pop('css', None)
dict_da_1.pop('api', None)
dict_da_1.pop('deployment', None)
dict_da_1.pop('artificial intelligence', None)
# dict_da_1.pop('testing', None)
# dict_da_1.pop('git', None)
# dict_da_1.pop('business intelligence', None)
# # dict_da_1.pop('testing', None)
# # dict_da_1.pop('analytics', None)
# # dict_da_1.pop('dl', None)
# dict_da_1.pop('aws', None)
# dict_da_1.pop('data science', None)
# # dict_da_1.pop('azure', None)
# dict_da_1.pop('java', None)
dict_da_1.pop('pipelines', None)
dict_da_1.pop('devops', None)
dict_da_1.pop('hadoop', None)
dict_da_1.pop('tableau', None)


dict_da_1_final = dict(
    sorted(dict_da_1.items(), key=lambda x: x[1], reverse=True))


x_list = list(dict_da_1_final.values())[:11]
y_list = list(dict_da_1_final.keys())[:11]


print(y_list)
p, q, r, s = 0, 0, 0, 0
for i in range(len(y_list)):
    if(y_list[i] == "business intelligence"):
        p = i
    if(y_list[i] == "aws"):
        q = i
    if(y_list[i] == "etl"):
        r = i
    if(y_list[i] == "cd"):
        s = i

y_list[p] = "BI"
y_list[q] = "AWS"
y_list[r] = "ETL"
y_list[s] = "CD"
print(y_list)


x_list = [i*2 for i in x_list]
y_list = [i.capitalize() for i in y_list]
y_list = ['BI' if i == 'Bi' else i for i in y_list]
y_list = ['AWS' if i == 'Aws' else i for i in y_list]
y_list = ['ETL' if i == 'Etl' else i for i in y_list]
y_list = ['CD' if i == 'Cd' else i for i in y_list]
y_list = ['SAS' if i == 'Sas' else i for i in y_list]


x_list.pop(9)
y_list.pop(9)
percent = [str(int((i/742) * 100))+"%" for i in x_list]
fig3 = go.Figure(go.Bar(
    x=x_list,
    y=y_list,
    text=percent,
    textposition='outside',
    orientation='h'
))
fig3.update_layout(
    title={
        'text': "Extracted from 742 Job Requirements",
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
fig3.update_layout(
    autosize=False,
    width=1500,
    height=690,)


def figures_to_html(figs, filename="data_analyst3.html"):
    dashboard2 = open(filename, 'w')
    dashboard2.write("<html><head></head><body>" + "\n")
    for fig in figs:
        dashboard2.write(
            '<h2 style="text-align: center">Top 10 skills for data analyst for experience of 5-8 years in 2021</h2>')
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard2.write(inner_html)
    dashboard2.write("</body></html>")


figures_to_html([fig3])
