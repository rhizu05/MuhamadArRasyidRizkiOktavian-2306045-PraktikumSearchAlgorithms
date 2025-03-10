from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, goal, visited, path):
        visited.add(v)  # Tandai sebagai dikunjungi
        path.append(v)  # Tambahkan ke jalur saat ini

        if v == goal:  # Jika node tujuan ditemukan
            print("Jalur ditemukan:", " -> ".join(path))
            return True

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFSUtil(neighbour, goal, visited, path):
                    return True  # Hentikan jika jalur ditemukan

        path.pop()  # Hapus dari jalur jika tidak berhasil
        return False

    def DFS(self, start, goal):
        visited = set()
        path = []
        if not self.DFSUtil(start, goal, visited, path):
            print(f"Tidak ada jalur dari {start} ke {goal}")

if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'D')
    g.addEdge('B', 'E')
    g.addEdge('C', 'F')
    g.addEdge('E', 'F')

    print("DFS mencari jalur dari A ke F:")
    g.DFS('A', 'F')