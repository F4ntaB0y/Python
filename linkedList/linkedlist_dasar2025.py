"""
Date: 28 Mei 2025
Note: Latihan membuat LinkedList step by step
"""

#* Step 1: Membuat Kelas Node
class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai/data
        self.next = None # Pointer ke node berikutnya (default: None

#* test
# node1 = Node(5)
# print(node1.data) # Output: 5
# print(node1.next) # Output: None

#* Step 2: Buat kelas LinkedList
class LinkedList:
    def __init__(self):
        self.head = None # Node pertama (awal dari linked list)

    #* Step 3: Tambahkan fungsi append untuk menambah node di akhir
    def append(self, data):
        newNode = Node(data) # 1. Buat node baru
        if self.head is None: # 2. Jika kosong, set sebagai head
            self.head = newNode
            return
        current = self.head # 3. Mulai dari head
        while current.next: # 4. Cari node terakhir
            current = current.next
        current.next = newNode # 5. Sambungkan node baru

    #* Step 4: Tambahkan fungsi untuk melihat isi linkedList
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

#* Penggunaan
ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")

print(ll)
