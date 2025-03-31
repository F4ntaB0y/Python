import os

#? membersihkan terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#? program to-do list
def todo_list():
    tasks = []

    while True:
        clear_terminal()
        print("\nTo-Do List")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

todo_list()