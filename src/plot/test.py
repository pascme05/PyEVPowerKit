import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
bar_names = ['Bar 1', 'Bar 2', 'Bar 3']
values = [
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45],
    [30, 40, 50]
]

# Creating subplots
fig = make_subplots(rows=4, cols=2, shared_xaxes=True, vertical_spacing=0.05)

# Adding traces to each subplot
for i in range(len(categories)):
    trace = go.Bar(
        x=bar_names,
        y=values[i],
        name=categories[i]
    )
    fig.add_trace(trace, row=(i // 2) + 1, col=(i % 2) + 1)

# Update layout
fig.update_layout(
    title='Grouped Bar Chart with 5 categories and 3 bars each',
    xaxis=dict(title='Bars'),
    yaxis=dict(title='Values'),
    barmode='group'  # Grouped bar mode
)

# Show plot
fig.show()