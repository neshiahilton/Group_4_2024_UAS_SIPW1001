from graphviz import Digraph


flowchart = Digraph(format='png')


flowchart.node('A', 'Define the Sorting Problem', shape='box', style='filled', fillcolor='lightblue')
flowchart.node('B', 'Analyze Input Characteristics', shape='box', style='filled', fillcolor='lightgreen')
flowchart.node('C', 'Select a Sorting Method', shape='box', style='filled', fillcolor='lightpink')
flowchart.node('D', 'Design the Sorting Logic', shape='box', style='filled', fillcolor='lightyellow')
flowchart.node('E', 'Implement the Algorithm', shape='box', style='filled', fillcolor='lightcyan')
flowchart.node('F', 'Test with Different Inputs', shape='box', style='filled', fillcolor='lavender')
flowchart.node('G', 'Evaluate and Optimize', shape='box', style='filled', fillcolor='lightcoral')
flowchart.node('H', 'Deploy and Use', shape='ellipse', style='filled', fillcolor='gray')


flowchart.edge('A', 'B')
flowchart.edge('B', 'C')
flowchart.edge('C', 'D')
flowchart.edge('D', 'E')
flowchart.edge('E', 'F')
flowchart.edge('F', 'G')
flowchart.edge('G', 'H')

flowchart.render('sorting_algorithm_process_flowchart')

print("Flowchart created and saved as 'sorting_algorithm_process_flowchart.png'")
