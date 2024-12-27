from graphviz import Digraph


flowchart = Digraph(format='png')


flowchart.node('A', 'Define the Problem', shape='box', style='filled', fillcolor='lightblue')
flowchart.node('B', 'Analyze the Array', shape='box', style='filled', fillcolor='lightgreen')
flowchart.node('C', 'Plan the Logic', shape='box', style='filled', fillcolor='lightpink')
flowchart.node('D', 'Choose the Algorithm', shape='box', style='filled', fillcolor='lightyellow')
flowchart.node('E', 'Design the Algorithm', shape='box', style='filled', fillcolor='lightcyan')
flowchart.node('F', 'Implement the Algorithm', shape='box', style='filled', fillcolor='lavender')
flowchart.node('G', 'Test with Various Inputs', shape='box', style='filled', fillcolor='lightcoral')
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


flowchart.render('array_algorithm_process_flowchart')

print("Flowchart created and saved as 'array_algorithm_process_flowchart.png'")
