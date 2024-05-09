import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[2, 2, 9],
    theta=['Speed','Energy efficiency',
           'Memory Efficiency']))
# df2 = pd.DataFrame(dict(
#     r=[2, 2, 16, 1],
#     theta=['Speed','Energy efficiency',
#            'Memory Utilisation']))
# df3 = pd.DataFrame(dict(
#     r=[2, 2, 16, 1],
#     theta=['Speed','Energy efficiency',
#            'Memory Utilisation']))

colours = ["#000080", "#1e90ff", "#b0c4de", "#87cefa"]
fig = px.line_polar(df, r='r', theta='theta', line_close=True,range_r=[25, 0])
fig.update_traces(line_color='#1e90ff', line_width=2)
# fig.add_trace(px.line_polar(df2, r='r', theta='theta', line_close=True,range_r=[20, 0]).data[0])
fig.update_traces(line_color='red', selector=dict(name=df.columns[1]))  # Change color for the first dataset

# Update polar layout to make the radial axis lines darker
fig.update_layout(polar = dict(radialaxis = dict(showticklabels = False)))
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
)
# Update polar layout to increase font size of labels
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            tickfont=dict(size=20)  # Adjust font size here
        )
    )
)
fig.update_traces(fill='toself',opacity=1)
fig.update_layout(polar=dict(radialaxis=dict(gridcolor='black', gridwidth=2)))

fig.show()