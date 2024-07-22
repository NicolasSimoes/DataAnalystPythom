import plotly.express as px
import pandas as pd
data = {
    'id': ["A", "B", "C", "D", "E", "F", "G"],
    'parent': ["", "A", "A", "B", "B", "C", "D"],
    'value': [10, 15, 7, 8, 12, 6, 5],
}
df = pd.DataFrame(data)
fig = px.sunburst(data, names='id', parents='parent', values='value')
fig.update_layout(title_text="Sunburst Chart")
fig.show()
#pip install plotly
#pip install pandas