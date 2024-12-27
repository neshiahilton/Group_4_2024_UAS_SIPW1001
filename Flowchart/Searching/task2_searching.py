from graphviz import Digraph

# Create a Digraph object
flowchart = Digraph(format='png')

# Define the nodes
flowchart.node('A', 'Define the Searching Problem', shape='box', style='filled', fillcolor='lightblue')
flowchart.node('B', 'Analyze the Dataset', shape='box', style='filled', fillcolor='lightgreen')
flowchart.node('C', 'Choose the Searching Algorithm', shape='box', style='filled', fillcolor='lightpink')
flowchart.node('D', 'Plan the Search Logic', shape='box', style='filled', fillcolor='lightyellow')
flowchart.node('E', 'Design the Algorithm', shape='box', style='filled', fillcolor='lightcyan')
flowchart.node('F', 'Implement the Algorithm', shape='box', style='filled', fillcolor='lavender')
flowchart.node('G', 'Test with Different Scenarios', shape='box', style='filled', fillcolor='lightcoral')
flowchart.node('H', 'Optimize and Analyze', shape='box', style='filled', fillcolor='lightgray')
flowchart.node('I', 'Finalize and Document', shape='ellipse', style='filled', fillcolor='white')

# Define the edges
flowchart.edge('A', 'B')
flowchart.edge('B', 'C')
flowchart.edge('C', 'D')
flowchart.edge('D', 'E')
flowchart.edge('E', 'F')
flowchart.edge('F', 'G')
flowchart.edge('G', 'H')
flowchart.edge('H', 'I')

# Render the flowchart to a file
flowchart.render('searching_algorithm_process_flowchart')

print("Flowchart created and saved as 'searching_algorithm_process_flowchart.png'")
