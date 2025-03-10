from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Best-First Search
def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan heuristik
    frontier.put((heuristic[start], start))  # Menambahkan simpul awal dengan nilai heuristik
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi
    visited_order = []  # List untuk mencatat urutan kunjungan simpul

    while not frontier.empty():
        _, current_node = frontier.get()  # Ambil simpul dengan heuristik terendah
        visited_order.append(current_node)
        print("Mengunjungi simpul:", current_node)

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:", " → ".join(visited_order))
            return True  # Berhenti jika simpul tujuan ditemukan

        explored.add(current_node)  # Tandai sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Nilai heuristik sebagai prioritas
                frontier.put((priority, neighbor))  # Tambahkan ke antrian

    print("\nSimpul tujuan tidak ditemukan!")
    print("Urutan kunjungan simpul:", " → ".join(visited_order))
    return False  # Jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'P': 9,
    'Q': 6,
    'R': 4,
    'S': 5,
    'T': 2,
    'U': 3,
    'V': 0  # Simpul tujuan memiliki nilai heuristik 0
}

# Graf berbentuk adjacency list
graph = {
    'P': {'Q', 'S'},
    'Q': {'R', 'T'},
    'S': {'U'},
    'R': {'V'},
    'T': {'V'},
    'U': {'T'}
}

# Titik awal dan tujuan
start_node = 'P'
goal_node = 'V'

# Panggil fungsi Greedy Best-First Search
greedy_best_first_search(graph, start_node, goal_node)