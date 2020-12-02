graph = {'A': ['B','C'],
         'B': ['A','D','E'],
         'C': ['F','G','A'],
         'D': ['B'],
         'E': ['H','B'],
         'F': ['C'],
         'G': ['C'],
         'H': ['E']
        }
def bfs(graph, root):
    visited, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)

def visit(n): print(n)
bfs(graph, 'A')
