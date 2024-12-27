from graphviz import Digraph


flowchart = Digraph(format='png')


flowchart.node('A', 'Define the Graph Problem', shape='box', style='filled', fillcolor='lightblue')
flowchart.node('B', 'Analyze the Graph', shape='box', style='filled', fillcolor='lightgreen')
flowchart.node('C', 'Choose the Graph Algorithm', shape='box', style='filled', fillcolor='lightpink')
flowchart.node('D', 'Plan the Approach', shape='box', style='filled', fillcolor='lightyellow')
flowchart.node('E', 'Design the Algorithm', shape='box', style='filled', fillcolor='lightcyan')
flowchart.node('F', 'Implement the Algorithm', shape='box', style='filled', fillcolor='lavender')
flowchart.node('G', 'Test with Different Graphs', shape='box', style='filled', fillcolor='lightcoral')
flowchart.node('H', 'Optimize and Analyze', shape='box', style='filled', fillcolor='lightgray')
flowchart.node('I', 'Finalize and Document', shape='ellipse', style='filled', fillcolor='white')


flowchart.edge('A', 'B')
flowchart.edge('B', 'C')
flowchart.edge('C', 'D')
flowchart.edge('D', 'E')
flowchart.edge('E', 'F')
flowchart.edge('F', 'G')
flowchart.edge('G', 'H')
flowchart.edge('H', 'I')


flowchart.render('graph_algorithm_process_flowchart')

print("Flowchart created and saved as 'graph_algorithm_process_flowchart.png'")
