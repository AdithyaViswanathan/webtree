# https://plotly.com/python/reference/#scatter
# https://networkx.github.io/documentation/stable/tutorial.html

import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup # To get everything
import chart_studio.plotly as py
from plotly.graph_objs import *

output = "<html><head></head><body><div></div><p></p></body></html>" #Output to be processed
soup = BeautifulSoup(output, 'lxml')
result = soup.findAll("html") #The result will point to the top node <html>
"""
The findAll method traverses the tree, starting at the given point, and 
finds all the Tag and NavigableString objects that match the criteria you give. 

"""


G = nx.DiGraph() #Empty Graph with no nodes and no edges.

G.add_node(result[0].name) 	# result[0].name --> html
parent = result[0] 			#<html><head></head><body><div></div><p></p></body></html>
parents = [parent] 			#[<html><head></head><body><div></div><p></p></body></html>]
labels=[parent.name] 		#['html']
edges = []
for parent in parents:
	"""This loop will have 
	<tags> [Contents inside ... incl. child 
	<childtag></childtag>] </tags>... Then goes on to explore <childtags>
	because of Line#53
	"""
	for child in parent.contents:
		"""
		Four iterations of the loop with print(child)
		<head></head>
		<body><div></div><p></p></body>
		<div></div>
		<p></p>
		"""
		G.add_node(child.name)
		G.add_edge(parent.name,child.name)
		x = (parent.name,child.name)
		"""
		Contents of X 4 Iterations
		('html', 'head')
		('html', 'body')
		('body', 'div')
		('body', 'p')
		"""
		labels.append(child.name)
		edges.append(x)
		parents.append(child)

"""
print(parents)

[<html><head></head><body><div></div><p></p></body></html>, 
<head></head>, <body><div></div><p></p></body>, <div></div>, <p></p>]

print(edges)

[('html', 'head'), ('html', 'body'), ('body', 'div'), ('body', 'p')]
-
"""

pos = nx.spiral_layout(G)


"""
spiral_layout(G, scale=1, center=None, dim=2, resolution=0.35, equidistant=False)

G (NetworkX graph or list of nodes) – A position will be assigned to every node in G.
scale (number (default: 1)) 		– Scale factor for positions.
center (array-like or None) 		– Coordinate pair around which to center the layout.
dim (int) 							– Dimension of layout, currently only dim=2 is supported. Other dimension values result in a ValueError.
resolution (float) 					– The compactness of the spiral layout returned. Lower values result in more compressed spiral layouts.
equidistant (bool) 					– If True, nodes will be plotted equidistant from each other.

"""


# nx.draw(G,pos,with_labels=True, font_weight='bold')
# print(parents)
# plt.show()

g=nx.Graph()
g.add_nodes_from(parents)
g.add_edges_from(edges) # E is the list of edges

pos=nx.fruchterman_reingold_layout(g)

"""
Example print(pos) #They vary each time

{
 <html><head></head><body><div></div><p></p></body></html>: array([-0.13771074,  0.92185995]),
 <head></head>: array([ 0.93064586, -0.40409817]),
 <body><div></div><p></p></body>: array([0.48708524, 0.72255242]), 
 <div></div>: array([-0.71727669,  0.71954607]), 
 <p></p>: array([-1.        ,  0.09307196]), 
 'html': array([-0.01867046, -0.41227352]), 
 'head': array([-0.14941259, -0.46630504]), 
 'body': array([ 0.1421822 , -0.38726024]), 
 'div': array([ 0.23439108, -0.283171  ]), 
 'p': array([ 0.22876609, -0.50392243])
 }

"""

"""
# This part of code eliminates the extra nodes that are present in the graph
# I didnt know if you want those extra nodes or not..

N = len(parents) # ?
counter = 0
Xv = []
Yv = []
for k in pos.keys():
	if(counter>=N):
		Xv.append(pos[k][0])
		Yv.append(pos[k][1])
	counter+=1
"""


"""
['html', 'head', 'body', 'div', 'p'] This was the initial label
"""
Xv=[pos[k][0],for k in pos.keys()] # X-coords from the above pos
Yv=[pos[k][1],for k in pos.keys()] # Y-coords from the above pos
labels = labels + labels 

"""
After I did this ... the labels turned out to be
['html', 'head', 'body', 'div', 'p', 'html', 'head', 'body', 'div', 'p'] 
So now everything is getting marked ..
We have to either take the extra tags from pos out or do this 
"""

Xed=[]
Yed=[]
for edge in edges:
	Xed+=[pos[edge[0]][0],pos[edge[1]][0],None]
	Yed+=[pos[edge[0]][1],pos[edge[1]][1],None]

trace3=Scatter(x=Xed,
               y=Yed,
               mode='lines',
               line=dict(color='rgb(210,210,210)', width=1),
               hoverinfo='text'
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
fig1.write_html('first_figure.html', auto_open=True)