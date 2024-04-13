import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Sample data
M_Max = [10, 20, 15, 25]  # Example numeric values for M_Max
P_Max = [15, 25, 20, 30]  # Example numeric values for P_Max

# Define colors for M_Max and P_Max
colors = ['#1f77b4', '#ff7f0e']  # Example colors, replace with your own

# Define categories
categories = ['HVS', 'INV', 'EMA', 'GBX']

# Create subplots
fig = make_subplots(rows=4, cols=2, shared_xaxes=True, vertical_spacing=0.05)

# Add M_Max and P_Max combined bars to the first subplot
combined_values = [M_Max[i] + P_Max[i] for i in range(len(M_Max))]
fig.add_trace(go.Bar(
    x=categories,
    y=M_Max,
    name='M_Max',
    marker_color=colors[0],
), row=1, col=1)

fig.add_trace(go.Bar(
    x=categories,
    y=P_Max,
    name='P_Max',
    marker_color=colors[1],
), row=1, col=1)

# Update layout for the first subplot
fig.update_xaxes(title_text='Category', row=1, col=1)
fig.update_yaxes(title_text='Maximum Value', row=1, col=1)

# Update layout for the entire figure
fig.update_layout(
    title='Maximum Values by Category',
    barmode='group'  # Change the bar mode to 'group'
)

# Show the plot
pio.show(fig)
