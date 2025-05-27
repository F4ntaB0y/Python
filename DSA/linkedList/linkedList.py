""" 
Kelas Node dan LinkedList untuk membuat struktur data linked list secara manual.
Setiap Node menyimpan data dan referensi ke node berikutnya.
LinkedList mengelola seluruh node, mulai dari node pertama (head).
"""

# Kelas Node mewakili satu simpul pada linked list
class Node:
    """
    Node merupakan elemen dasar dalam linked list yang menyimpan data
    dan referensi ke node berikutnya (next).
    """
    def __init__(self, data):
        self.data = data      # Menyimpan data
        self.next = None      # Referensi ke node berikutnya, default-nya None

    def __repr__(self):
        return self.data      # Mengembalikan representasi string dari data node

# Kelas LinkedList mewakili keseluruhan linked list
class LinkedList:
    """
    LinkedList menyimpan referensi ke node pertama (head),
    dan menyediakan metode representasi string dari seluruh isi linked list.
    """
    def __init__(self):
        self.head = None      # Head adalah simpul pertama dalam list

    def __repr__(self):
        """
        Mengembalikan string berisi data semua node dari head hingga akhir (None),
        dalam format seperti: a -> b -> c -> None
        """
        node = self.head      # Mulai dari head
        nodes = []            # List untuk menyimpan representasi data setiap node
        while node is not None:
            nodes.append(node.data)   # Tambahkan data dari setiap node
            node = node.next          # Pindah ke node berikutnya
        nodes.append("None")          # Tambahkan "None" sebagai akhir dari linked list
        return " -> ".join(nodes)     # Gabungkan elemen dengan panah

# ============================
# Contoh penggunaan struktur linked list
# ============================

# Membuat linked list kosong
llist = LinkedList()
print(llist)  # Output: None

# Membuat node pertama dengan data "a" dan menjadikannya head
first_node = Node("a")
llist.head = first_node
print(llist)  # Output: a -> None

# Membuat node kedua dan ketiga dengan data "b" dan "c"
second_node = Node("b")
third_node = Node("c")

# Menautkan node pertama ke node kedua, dan kedua ke ketiga
first_node.next = second_node
second_node.next = third_node

# Menampilkan seluruh isi linked list
print(llist)  # Output: a -> b -> c -> None
