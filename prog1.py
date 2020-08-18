# https://plotly.com/python/reference/#scatter
# https://networkx.github.io/documentation/stable/tutorial.html


import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import chart_studio.plotly as py
from plotly.graph_objs import *

output = "<html><head></head><body><div></div><p></p></body></html>"
soup = BeautifulSoup(output, 'lxml')
result = soup.findAll("html")



G = nx.DiGraph()

G.add_node(result[0].name)
parent = result[0]
parents = [parent]
labels=[parent.name]
edges = []
for parent in parents:
	for child in parent.contents:
		G.add_node(child.name)
		G.add_edge(parent.name,child.name)
		x = (parent.name,child.name)
		labels.append(child.name)
		edges.append(x)
		parents.append(child)

pos = nx.spiral_layout(G)
# nx.draw(G,pos,with_labels=True, font_weight='bold')
# print(parents)
# plt.show()
g=nx.Graph()
g.add_nodes_from(parents)
g.add_edges_from(edges)# E is the list of edges

pos=nx.fruchterman_reingold_layout(g)


N = len(parents)

Xv=[pos[k][0] for k in pos.keys()]
Yv=[pos[k][1] for k in pos.keys()]
Xed=[]
Yed=[]
for edge in edges:
    Xed+=[pos[edge[0]][0],pos[edge[1]][0], None]
    Yed+=[pos[edge[0]][1],pos[edge[1]][1], None]

trace3=Scatter(x=Xed,
               y=Yed,
               mode='lines',
               line=dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace4=Scatter(x=Xv,
               y=Yv,
               mode='markers',
               name='net',
               marker=dict(symbol='circle-dot',
                             size=5,
                             color='#6959CD',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               text=labels,
               hoverinfo='text'
               )

# annot="This networkx.Graph has the Fruchterman-Reingold layout<br>Code:"+\
# "<a href='http://nbviewer.ipython.org/gist/empet/07ea33b2e4e0b84193bd'> [2]</a>"

axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

width=800
height=800
layout=Layout(title= "Just Checking",
    font= dict(size=12),
    showlegend=False,
    autosize=False,
    width=width,
    height=height,
    xaxis=layout.XAxis(axis),
    yaxis=layout.YAxis(axis),
    margin=layout.Margin(
        l=40,
        r=40,
        b=85,
        t=100,
    ),
    hovermode='closest',
    annotations=[
           dict(
           showarrow=False,
            text='This igraph.Graph has the Kamada-Kawai layout',
            xref='paper',
            yref='paper',
            x=0,
            y=-0.1,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=14
            )
            )
        ]
    )


data1=[trace3, trace4]
fig1=Figure(data=data1, layout=layout)
# fig1['layout']['annotations'][0]['text']=annot
fig1.write_html('first_figure.html', auto_open=True)