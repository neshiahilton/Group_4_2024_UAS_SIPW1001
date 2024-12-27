from graphviz import Digraph


flowchart = Digraph(format='png')


flowchart.node('A', 'Define the Problem', shape='box', style='filled', fillcolor='lightblue')
flowchart.node('B', 'Plan the Approach', shape='box', style='filled', fillcolor='lightgreen')
flowchart.node('C', 'Choose the Tools', shape='box', style='filled', fillcolor='lightpink')
flowchart.node('D', 'Design the Algorithm', shape='box', style='filled', fillcolor='lightyellow')
flowchart.node('E', 'Implement the Algorithm', shape='box', style='filled', fillcolor='lightcyan')
flowchart.node('F', 'Test with Sample Inputs', shape='box', style='filled', fillcolor='lavender')
flowchart.node('G', 'Evaluate and Optimize', shape='box', style='filled', fillcolor='lightcoral')
flowchart.node('H', 'Finalize and Deploy', shape='ellipse', style='filled', fillcolor='gray')


flowchart.edge('A', 'B')
flowchart.edge('B', 'C')
flowchart.edge('C', 'D')
flowchart.edge('D', 'E')
flowchart.edge('E', 'F')
flowchart.edge('F', 'G')
flowchart.edge('G', 'H')


flowchart.render('basic_algorithm_process_flowchart')

print("Flowchart created and saved as 'basic_algorithm_process_flowchart.png'")

