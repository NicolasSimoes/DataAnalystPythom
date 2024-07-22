import plotly.express as px
data ={
  'x':[1,2,3,4,5],
  'y' : [2,3,5,7,11]
  }
fig= px.line(data, x='x', y='y',
                title="Line Graph",markers=True)

fig.show()