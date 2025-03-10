import heapq

# Uniform Cost Search (UCS)
def uniform_cost_search(goal, start):
    global graph, cost
    answer = {}

    # Priority Queue (heap)
    queue = []
    heapq.heappush(queue, (0, start, []))  # (biaya, simpul, jalur)

    # Set untuk menyimpan simpul yang sudah dikunjungi
    visited = set()

    while queue:
        biaya_sekarang, simpul, jalur = heapq.heappop(queue)

        if simpul in visited:
            continue

        visited.add(simpul)
        jalur = jalur + [simpul]

        # Jika sudah sampai di tujuan, kembalikan hasilnya
        if simpul in goal:
            return biaya_sekarang, jalur

        # Mengeksplorasi tetangga dari simpul saat ini
        for tetangga in graph[simpul]:
            if tetangga not in visited:
                total_biaya = biaya_sekarang + cost[(simpul, tetangga)]
                heapq.heappush(queue, (total_biaya, tetangga, jalur))

    return float("inf"), []  # Jika tujuan tidak dapat dicapai

# Fungsi utama
if __name__ == '__main__':
    # Graph dengan simpul berupa huruf
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }

    # Menetapkan biaya antar simpul
    cost = {
        ('A', 'B'): 4,
        ('A', 'C'): 3,
        ('B', 'D'): 5,
        ('B', 'E'): 6,
        ('C', 'E'): 2,
        ('C', 'F'): 4,
        ('D', 'G'): 3,
        ('E', 'G'): 2,
        ('F', 'G'): 5
    }

    # Menetapkan simpul tujuan
    tujuan = {'G'}

    # Menjalankan Uniform Cost Search dari simpul A ke simpul tujuan G
    biaya_minimum, jalur = uniform_cost_search(tujuan, 'A')

    # Output hasil pencarian UCS dalam bahasa Indonesia
    print("Biaya minimum dari simpul A ke simpul G adalah:", biaya_minimum)
    print("Jalur yang ditempuh:", " → ".join(jalur))