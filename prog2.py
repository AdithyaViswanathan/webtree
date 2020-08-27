import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup # To get everything
import chart_studio.plotly as py
from plotly.graph_objs import *

output = "<html><head></head><body class='jc' id='id1'><div>String in Div tag with nested p tag<p> Hello </p></div><p>Hi There!</p></body></html>" #Output to be processed
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

			print(parent.name,node_name)



"""
print(parents)

[<html><head></head><body><div></div><p></p></body></html>, 
<head></head>, <body><div></div><p></p></body>, <div></div>, <p></p>]

print(edges)

[('html', 'head'), ('html', 'body'), ('body', 'div'), ('body', 'p')]
-
"""

pos = nx.spiral_layout(G)