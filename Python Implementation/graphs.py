from collections import deque

class Graphs:
    def bfs(self, graph, start):
        """
        Breadth-First Search (BFS)
        :param graph: Graph represented as adjacency list
        :param start: Starting node
        :return: List of visited nodes in BFS order
        """
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(graph[node])

        return result

    def dfs(self, graph, start, visited=None):
        """
        Depth-First Search (DFS)
        :param graph: Graph represented as adjacency list
        :param start: Starting node
        :param visited: Set of visited nodes
        :return: List of visited nodes in DFS order
        """
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)
        return visited

    def dijkstra(self, graph, start):
        """
        Dijkstra's Algorithm for shortest path
        :param graph: Graph represented as adjacency list
        :param start: Starting node
        :return: Shortest distance to all nodes
        """
        import heapq
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Testing
if __name__ == "__main__":
    graphs = Graphs()

    # Testing BFS
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS Traversal:", graphs.bfs(graph, 'A'))

    # Testing DFS
    print("DFS Traversal:", graphs.dfs(graph, 'A'))

    # Testing Dijkstra's Algorithm
    graph_with_weights = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print("Shortest distances from 'A':", graphs.dijkstra(graph_with_weights, 'A'))
