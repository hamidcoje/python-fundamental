daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
print('Tampilkan variable daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal data buku')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\npop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\npop -1')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintal del')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintal del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX']
del daftar_buku[0:-2] #STAR:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things Fisrt', '4DX', 'mate', 'done']
del daftar_buku[0::2] #STAR:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])