# https://plotly.com/python/reference/#scatter
# https://networkx.github.io/documentation/stable/tutorial.html

import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup, NavigableString # To get everything
import chart_studio.plotly as py
from plotly.graph_objs import *

#Paints the nodes according to the list sent with the color 'HEX VALUE'
def painter(node_color_list,the_color):
	diff_color_x = []
	diff_color_y = []
	diff_color_label = []
	Nodes = list(G.nodes)

	for ttc in node_color_list:
	  ttcl = len(ttc)
	  for i in range(len(labels)):
	    if(ttc == str(Nodes[i][:ttcl])):
	      diff_color_y.append(Yv[i])
	      diff_color_x.append(Xv[i])
	      diff_color_label.append(labels[i])

	trace=Scatter(x=diff_color_x,
	               y=diff_color_y,
	               mode='markers',
	               name='net',
	               marker=dict(symbol='circle-dot',
	                             size=5,
	                             color=the_color,
	                             line=dict(color='rgb(50,50,50)', width=0.5)
	                             ),
	               text=diff_color_label,
	               hoverinfo='text'
	               )

	return trace

output = "<html><head></head><body class='jc' id='id1'><div class='jc jc1 jc2'>String in Div tag with nested p tag<p> Hello </p></div><p>Hi There!</p></body></html>" #Output to be processed
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
i = 0
for parent in parents:
	"""This loop will have 
	<tags> [Contents inside ... incl. child 
	<childtag></childtag>] </tags>... Then goes on to explore <childtags>
	because of Line#53
	"""
	if hasattr(parent, 'contents'):
		for child in parent.contents:
			"""
			These 2 lines will take out the extra string present as a node
			# if isinstance(child, NavigableString):
			# 	continue
			"""
			"""
			Four iterations of the loop with print(child)
			<head></head>
			<body><div></div><p></p></body>
			<div></div>
			<p></p>
			"""
			if child.name != None:
				node_name = child.name+str(i)
			else:
				node_name = 'string'+str(i)
			i = i + 1
			G.add_node(node_name)
			G.add_edge(parent.name,node_name)
			x = (parent.name,node_name)
			"""
			Contents of X 4 Iterations
			('html', 'head')
			('html', 'body')
			('body', 'div')
			('body', 'p')
			"""
			if child.name != None:
				element1 = str(child.name)
				child.name = node_name
			else:
				element1 = 'string'
			if hasattr(child, 'attrs'):
				for item in child.attrs:
					#print(item,child.attrs[item])
					element1 = element1 + '<br>' + '&nbsp; &nbsp;' + item+':' + '&nbsp;' + str(child.attrs[item])
			if child.string != None:
				element1 = element1 + '<br>' + '&nbsp; &nbsp;' + 'string'+':' + '&nbsp;' + str(child.string)
			labels.append(element1)
			edges.append(x)
			parents.append(child)

			#print(parent.name,node_name)

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
['html', 'head', 'body', 'div', 'p'] This was the initial label
"""
# Xv=[pos[k][0] for k in pos.keys()] # X-coords from the above pos
# Yv=[pos[k][1] for k in pos.keys()] # Y-coords from the above pos
# labels = labels + labels 

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


# Couldn't find any different code in google : ( Sed Lyf... 
# So modified our own code to color some nodes differently 
# This code colors the nodes given in the shortest_lenth list
# Given that our shortest length calculator, calculates the length from the child_nodes ... so that the return name is p5, p3 similar to that 

shortest_path = (nx.shortest_path(G,source="html",target="p5"))
shortest_length = ['html','div','body','string']




trace5 = painter(shortest_path,'#FFA500')
trace6 = painter(shortest_length,'#FF0000')


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

# data1=[trace3, trace4]
data1=[trace3, trace4, trace5, trace6]
fig1=Figure(data=data1, layout=layout)
fig1.write_html('first_figure.html', auto_open=True)