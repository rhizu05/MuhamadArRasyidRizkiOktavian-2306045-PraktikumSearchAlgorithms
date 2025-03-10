import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start, goal):
        visited, queue = set(), collections.deque([(start, [start])])
        visited.add(start)

        while queue:
            vertex, path = queue.popleft()
            print(vertex, end=' ')  # Cetak urutan kunjungan

            if vertex == goal:
                print("\nJalur ditemukan:", " -> ".join(path))
                return

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [neighbour]))

        print(f"\nTidak ada jalur dari {start} ke {goal}")

if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'D')
    g.addEdge('B', 'E')
    g.addEdge('C', 'F')
    g.addEdge('E', 'F')

    print("BFS mencari jalur dari A ke F:")
    g.BFS('A', 'F')