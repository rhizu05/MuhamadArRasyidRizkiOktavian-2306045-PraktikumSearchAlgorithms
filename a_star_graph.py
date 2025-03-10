from queue import PriorityQueue

# Fungsi untuk algoritma A* Graph Search
def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan f(n) = g(n) + h(n)
    frontier.put((0, start, []))  # (biaya, simpul, jalur)
    explored = {}  # Dictionary untuk menyimpan biaya terendah ke setiap simpul

    while not frontier.empty():
        current_cost, current_node, path = frontier.get()  # Ambil simpul dengan prioritas terendah
        path = path + [current_node]  # Tambahkan simpul ke jalur

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", current_cost)
            return  # Berhenti jika simpul tujuan ditemukan

        explored[current_node] = current_cost  # Tandai simpul sebagai dieksplorasi

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost  # g(n)
            total_cost = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)

            # Jika simpul belum dieksplorasi atau ditemukan jalur dengan biaya lebih rendah
            if neighbor not in explored or new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                frontier.put((total_cost, neighbor, path))  # Masukkan simpul ke frontier

    print("\nSimpul tujuan tidak ditemukan!")

# Daftar heuristik untuk setiap simpul
heuristic = {
    'P': 6,
    'Q': 4,
    'R': 3,
    'S': 5,
    'T': 2,
    'U': 1,
    'V': 0  # Simpul tujuan memiliki nilai heuristik 0
}

# Graf berbobot dalam bentuk adjacency list
graph = {
    'P': {'Q': 3, 'S': 2},
    'Q': {'R': 4, 'T': 6},
    'S': {'U': 5},
    'R': {'V': 6},
    'T': {'V': 3},
    'U': {'T': 2}
}

# Titik awal dan tujuan
start_node = 'P'
goal_node = 'V'

# Panggil fungsi A* Graph Search
a_star_graph_search(graph, start_node, goal_node, heuristic)