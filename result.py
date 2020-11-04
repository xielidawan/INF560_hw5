''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve result.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/result
in your browser.
'''
import pandas as pd
from bokeh.models import HoverTool, FactorRange, Select, ColumnDataSource, annotations, Label, Title
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# Task 3.a
data = pd.read_csv('latimes-state-totals.csv')
data['date_time'] = pd.to_datetime(data['date'])
new_data = data[['date_time', 'new_confirmed_cases']]
new_data = new_data[(new_data["date_time"] >= "2020-08-01") & (new_data["date_time"] <= "2020-08-31")]

# Create a plot

p_a = figure(tools=TOOLS,
             y_axis_label='New Confirmed Cases',
             title='new confirmed cases of Coronavirus [note:The data is up to date to Oct. 29, 2020.]',
             x_axis_type='datetime',
             plot_height=400
             )

text_a_publish = 'Published throughout the day at latimes.com/coronavirustracker'
text_a_provide = 'Provided by local public health agencies.'
text_a_ava = 'Available on The Times database'
text_a_Link = "Access: https://github.com/datadesk/california-coronavirus-data"

p_a.add_layout(Title(text=text_a_Link, text_font_style="italic"), 'above')
p_a.add_layout(Title(text=text_a_ava, text_font_style="italic"), 'above')
p_a.add_layout(Title(text=text_a_provide, text_font_style="italic"), 'above')
p_a.add_layout(Title(text=text_a_publish, text_font_style="italic"), 'above')

p_a.line('date_time', 'new_confirmed_cases', source=new_data, line_width=2)
p_a.circle('date_time', 'new_confirmed_cases', source=new_data, fill_color='red', size=6)

p_a.add_tools(HoverTool(
    tooltips=[
        ('date', '@date_time{%Y-%m-%d}'),
        ('new cases', '@new_confirmed_cases')
    ],

    formatters={
        '@date_time': 'datetime',  # use 'datetime' formatter for '@date_time' field
    }
))

# Task 3.b
origin_data = pd.read_csv('cdph-race-ethnicity.csv')
new_data_bc = origin_data[origin_data["age"] == "all"]
date = sorted(list(set(new_data_bc['date'])), reverse=True)
race = sorted(list(set(new_data_bc['race'])))

new_data_b = new_data_bc[['date', 'race', 'confirmed_cases_percent', 'population_percent']]

data_format_b = ['confirmed_cases_percent', 'population_percent']
temp_data_b = new_data_b[new_data_b["date"] == date[0]]

data_b = {'race': race,
          'confirmed_cases_percent': temp_data_b['confirmed_cases_percent'],
          'population_percent': temp_data_b['population_percent']}

x_b = [(r, df) for r in race for df in data_format_b]

y_b = sum(zip(data_b['confirmed_cases_percent'], data_b['population_percent']), ())  # like an hstack

source_b = ColumnDataSource(data=dict(x=x_b, y=y_b))

p_b = figure(tools=TOOLS, x_range=FactorRange(*x_b), plot_height=800,
             title="Confirmed_case VS Population [note:The data is up to date to Oct. 29, 2020.]")

r_b = p_b.vbar(x='x', top='y', width=0.9, source=source_b,
               fill_color=factor_cmap('x', palette=['firebrick', 'navy'], factors=data_format_b, start=1, end=2))

text_bc_publish = 'Published throughout the day at latimes.com/coronavirustracker'
text_bc_provide = 'Provided by the California Department of Public Health.'
text_bc_Link = "Access: https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx"
text_a_ava = 'Or Available on The Times database'
text_bc_Link_2 = 'Access: https://github.com/datadesk/california-coronavirus-data'
p_b.add_layout(Title(text=text_bc_Link_2, text_font_style="italic"), 'above')
p_b.add_layout(Title(text=text_a_ava, text_font_style="italic"), 'above')
p_b.add_layout(Title(text=text_bc_Link, text_font_style="italic"), 'above')
p_b.add_layout(Title(text=text_bc_provide, text_font_style="italic"), 'above')
p_b.add_layout(Title(text=text_bc_publish, text_font_style="italic"), 'above')

p_b.y_range.start = 0
p_b.x_range.range_padding = 0.2
p_b.xaxis.major_label_orientation = 1.4
p_b.xgrid.grid_line_color = None

p_b.add_tools(HoverTool(
    tooltips=[
        ('Classification', '@x'),
        ('percentage', '@y')
    ]
))

# Task 3.c
new_data_c = new_data_bc[['date', 'race', 'deaths_percent', 'population_percent']]

data_format_c = ['deaths_percent', 'population_percent']
temp_data_c = new_data_c[new_data_c["date"] == date[0]]

data_c = {'race': race,
          'deaths_percent': temp_data_c['deaths_percent'],
          'population_percent': temp_data_c['population_percent']}

x_c = [(r, df) for r in race for df in data_format_c]

y_c = sum(zip(data_c['deaths_percent'], data_c['population_percent']), ())  # like an hstack

source_c = ColumnDataSource(data=dict(x=x_c, y=y_c))

p_c = figure(tools=TOOLS, x_range=FactorRange(*x_c), plot_height=800,
             title="Deaths VS Population [note:The data is up to date to Oct. 29, 2020.]")

r_c = p_c.vbar(x='x', top='y', width=0.9, source=source_c,
               fill_color=factor_cmap('x', palette=['firebrick', 'navy'], factors=data_format_c, start=1, end=2)
               )

p_c.add_layout(Title(text=text_bc_Link_2, text_font_style="italic"), 'above')
p_c.add_layout(Title(text=text_a_ava, text_font_style="italic"), 'above')
p_c.add_layout(Title(text=text_bc_Link, text_font_style="italic"), 'above')
p_c.add_layout(Title(text=text_bc_provide, text_font_style="italic"), 'above')
p_c.add_layout(Title(text=text_bc_publish, text_font_style="italic"), 'above')

p_c.y_range.start = 0
p_c.x_range.range_padding = 0.2
p_c.xaxis.major_label_orientation = 1.4
p_c.xgrid.grid_line_color = None

p_c.add_tools(HoverTool(
    tooltips=[
        ('Classification', '@x'),
        ('percentage', '@y')
    ]
))

# Creating select box
select_b = Select(title="Graph_2_Option:", value=date[0], options=date)
select_c = Select(title="Graph_3_Option:", value=date[0], options=date)


def update_b(attrname, old, new):
    temp_new_data_b = new_data_b[new_data_b["date"] == select_b.value]
    y_b_update = sum(zip(temp_new_data_b['confirmed_cases_percent'], temp_new_data_b['population_percent']), ())
    r_b.data_source.data['y'] = y_b_update


def update_c(attrname, old, new):
    temp_new_data_c = new_data_c[new_data_c["date"] == select_c.value]
    y_c_update = sum(zip(temp_new_data_c['deaths_percent'], temp_new_data_c['population_percent']), ())
    r_c.data_source.data['y'] = y_c_update


select_b.on_change('value', update_b)
select_c.on_change('value', update_c)

curdoc().add_root(row(p_a, width=800))
curdoc().add_root(row(p_b, column(select_b), p_c, column(select_c), width=1000))
curdoc().title = 'INF560_HW7'
