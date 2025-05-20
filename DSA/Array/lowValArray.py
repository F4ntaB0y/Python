"""
Langkah membuat DSA Array untuk temukan nilai terendah
0. harus ada list array
1. Buat variabel 'minN' dan atur sama dengan nilai pertama array.
2. Telusuri setiap elemen dalam array.
3. Jika elemen saat ini memiliki nilai yang lebih rendah dari 'minN', perbarui 'minN' ke nilai ini.
4. Setelah melihat semua elemen dalam array, variabel 'minN' sekarang berisi nilai terendah.
"""

arrayKu = [9,7,8,6,5,3,4] #step 0
minN = arrayKu[0] #step 1

for i in arrayKu: #step 2
    if i < minN: #step 3
        minN =  i
        
print("Nilai terendah: ", minN) #step 4
