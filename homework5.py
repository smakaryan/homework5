import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py


from homework5_figures import f1
from homework5_figures import f2
from homework5_figures import f3
from homework5_figures import f4
from homework5_figures import data_f5

data_gdp = quandl.get("FRED/GDP", authtoken = "9vAJtSzhfwk-z4ikxWiB")

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title="Homework 5"

app.layout=html.Div([
	
	#row1

	html.Div([html.H1(children="Homework 5", style={"color":"maroon", "text-align":"center", "font-family":"cursive",
		"font-weight":"bold", "font-size":"40px",})],
		className="twelve columns"),

	#row2

		html.Div([
			
			html.Div([

			dcc.RadioItems(id="radio", options=[
            {"label": "Employee Churn", "value": f1}],
            value="show"),

            dcc.RadioItems(id="radio", options=[
            {"label": "Startup RoadMap", "value": data_f5}],
            value="show")

            ], className="three columns"),

			
			html.Div([
			dcc.Graph(id="Graphs")],
			className="nine columns"),

			], className="twelve columns"),


	#row3

		html.Div([
			html.Div([dcc.Dropdown(
				id = 'dropdown',
				options=[
	            {'label': 'Google', 'value': 'GOOGL'},
	            {'label': 'Apple', 'value': 'AAPL'},
	            {'label': 'Microsoft', 'value': 'MSFT'},
	            {'label': 'Amazon', 'value': 'AMZN'},
	            {'label': 'General Electric', 'value': 'GE'}

	            ], placeholder='Please, select a stock', multi=True),
			
			html.Button(id='submit',n_clicks=0, children='Submit'),
			], className="two columns"),

			html.Div([
			dcc.Graph(id="Boxplot")],
			className="five columns"),

			html.Div([
			dcc.Graph(id="Table")],
			className="five columns"),

			], className="twelve columns"),



	#row4
		
		html.Div([
			html.Div([dcc.RangeSlider(id = 'option_in', min=0, max=len(data_gdp.index), value=[0, len(data_gdp.index)])],
			className="four columns"),

			html.Div([dcc.Graph(id="GDP")],
			className="eight columns"),
			
			], className="twelve columns")
		
		




		])

#button

@app.callback(
    Output(component_id="Graphs", component_property="figure"),
    [Input(component_id="radio", component_property="value")])

def update_graph(input_value1):
    figure=input_value1
    return figure

    


#dropdown boxplot

@app.callback(
    Output(component_id='Boxplot', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')])

def update_graph(clicks, input_value2):
	quandl_input_1 = "WIKI/"+input_value2[0]
	quandl_input_2 = "WIKI/"+input_value2[1]
	
	stock_data_1 = quandl.get(quandl_input_1, authtoken = "9vAJtSzhfwk-z4ikxWiB")
	stock_data_2 = quandl.get(quandl_input_2, authtoken = "9vAJtSzhfwk-z4ikxWiB")
	
	x_values_1 = stock_data_1.Open.pct_change()
	x_values_2 = stock_data_2.Open.pct_change()
	
	trace_1 = go.Box(x=x_values_1, name=input_value2[0])
	trace_2 = go.Box(x=x_values_2, name=input_value2[1])
	
	layout_f3 = dict(title="<i>Distribution of Price changes</i> "+input_value2[0]+" and "+input_value2[1])
	data_f3 = [trace_1,trace_2]
	figure = dict(data=data_f3, layout=layout_f3)
	return figure

#dropdown table

@app.callback(
    Output(component_id='Table', component_property='figure'),
    [Input(component_id='submit', component_property="n_clicks")],
    [State(component_id='dropdown', component_property='value')]
)

def update_table(clicks, input_value2):
	quandl_input_3 ="WIKI/"+input_value2[0]
	quandl_input_4 = "WIKI/"+input_value2[1]
	
	stock_data_3 = quandl.get(quandl_input_3, authtoken = "9vAJtSzhfwk-z4ikxWiB")
	stock_data_4 = quandl.get(quandl_input_4, authtoken = "9vAJtSzhfwk-z4ikxWiB")
	
	stock_data_3["PC"]=stock_data_3.Open.pct_change()
	stock_data_4["PC"]=stock_data_4.Open.pct_change()
	
	stock_data3=stock_data_3.iloc[1:5,-1:].round(3)
	stock_data4=stock_data_4.iloc[1:5,-1:].round(3)
	
	header= dict(values=[input_value2[0],input_value2[1]],
				align=["left", "center"],
				font=dict(color="white",
				size=12),
				fill=dict(color="#119DFF"))
	
	cells=dict(values=[stock_data3.values, stock_data4.values],
			align=["left", "center"],
			fill=dict(color=["yellow", "white"]))
	
	trace_t=go.Table(header=header, cells=cells)
		
	data_t=[trace_t]	
	layout_f4=dict(width=500, height=300)	
	table=dict(data=data_t, layout=layout_f4)
	
	return table



#slider

@app.callback(
    Output(component_id='GDP', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)
def update_graph(input_value3):

	gdp_index = data_gdp.index[input_value3[0]:input_value3[1]]
	gdp_values = data_gdp.Value[input_value3[0]:input_value3[1]]

	trace_gdp = [go.Scatter(x=gdp_index,y=gdp_values,fill="tozeroy")]
	layout_gdp = dict(title = '<b>US GDP over time</b>')
	figure = dict(data=trace_gdp, layout = layout_gdp)
	return figure


if __name__ == '__main__':
    app.run_server()