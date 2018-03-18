from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py

data1 = quandl.get("FRED/GDP", authtoken = "9vAJtSzhfwk-z4ikxWiB")
data2 = quandl.get("WIKI/GOOGL", authtoken = "9vAJtSzhfwk-z4ikxWiB")
data3 = quandl.get("BCHARTS/ABUCOINSUSD", authtoken = "9vAJtSzhfwk-z4ikxWiB")

#graph1
x_values_1_f1 = ["X8","X7","X6","X5"]
x_values_2_f1 = ["X4","X3","X2","X1"]

y_values_1_f1 = [17,45,17,20]
y_values_2_f1 = [-17,-45,-5,-37]


trace_1_f1 = go.Bar(y=x_values_1_f1, x=y_values_1_f1, name="<b>Negative</b>", orientation="h",
                 marker=dict(
                     color="pink",
                     line=dict(
                         color="maroon",
                         width=1.5))
                )

trace_2_f1 = go.Bar(y=x_values_2_f1, x=y_values_2_f1, name="Positive", orientation="h",
                 marker=dict(
                     color="lightblue",
                     line=dict(
                         color="blue",
                         width=1.5))
                 )

layout_f1 = dict(title="<b>Correlation with employees probability of churn</b>",
                 yaxis=dict(title="Variable"))


data_f1 = [trace_1_f1,trace_2_f1]
f1 = dict(data=data_f1, layout=layout_f1)

#graph2
x_values_f2 = pd.to_datetime(data1.index.values)
y_values_f2 = data1.Value

trace_f2 = go.Scatter(x=x_values_f2, y=y_values_f2,
                      mode="lines", fill= "tozeroy")

layout_f2 = dict(title="<b>US GDP over time</b>",
              )

data_f2 = [trace_f2]
f2 = dict(data=data_f2, layout=layout_f2)

#graph3
x_values_1_f3 = data2.Open.pct_change()
x_values_2_f3 = data3.Open.pct_change()

trace_1_f3 = go.Box(x=x_values_2_f3, name="<b>Bitcoin</b>")
trace_2_f3 = go.Box(x=x_values_1_f3, name="<b>Google</b>")


layout_f3 = dict(title="<i>Distribution of Price changes</i>")

data_f3 = [trace_1_f3,trace_2_f3]
f3 = dict(data=data_f3, layout=layout_f3)

#graph4
header= dict(values=["Google","Bitcoin"],
             align=["left", "center"],
             font=dict(color="white", size=12),
             fill=dict(color="#119DFF")
            )

data2["PC"]=data2.Open.pct_change()
data3["PC"]=data3.Open.pct_change()

data2_1=data2.iloc[1:5,-1:].round(3)
data3_1=data3.iloc[1:5,-1:].round(3)

data2_2=data2_1.values
data3_2=data3_1.values

cells = dict(values=[data2_2, data3_2],
             align = ["left","center"],
             fill = dict(color=["yellow","white"])
            )
trace_f4 = go.Table(header=header, cells=cells)

data_f4 = [trace_f4]
layout_f4 = dict(width=500, height=300)
f4 = dict(data=data_f4, layout=layout_f4)

#graph5
trace_f5=[dict(Task="Task 1", Start="2018-01-01", Finish="2018-01-31", Resource="Idea Validation"),
          dict(Task="Task 2", Start="2018-03-01", Finish="2018-04-15", Resource="Team formation"),
          dict(Task="Task 3", Start="2018-04-15", Finish="2018-09-30", Resource="Prototyping")]

data_f5= ff.create_gantt(trace_f5,
                         colors=["#3333ff", "#ff6600", "#009933"],
                         title="Startup Roadmap",
                         index_col="Resource",
                         show_colorbar=True)