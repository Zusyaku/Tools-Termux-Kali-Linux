#!/bin/python2
import os
os.system('clear')

print '============================================================'
print '(-)Author : MR.FAGHP BLACK-404/F'
print '(-)Team   : Mavia Teknologi Indonesia'
print '(-)Aliran : BLACK HAT/EVILHACKER'
print '============================================================'

print '================[MENU]================'
print '(1). Penambahan'
print '(2). Pengurangan'
print '(3). Perkalian'
print '(4). Pembagian'
print '======================================='
pilih = input('Masukan Pilihan Anda : ')
if pilih == 1:
      print
      angka_1 = input('Masukan Angka Pertama: ')
      angka_2 = input('Masukan Angka Kedua: ')
      total = angka_1 + angka_2
      print 'Hasil Penambahan',total


elif pilih == 2:
        print
        angka_1 = input('Masukan Angka Pertama: ')
        angka_2 = input('Masukan Angka Kedua: ')
        total = angka_1 - angka_2
        print 'Hasil Pengurangan',total

elif pilih == 3:
        print
        angka_1 = input('Masukan Angka Pertama: ')
        angka_2 = input('Masukan Angka Kedua: ')
        total = angka_1 * angka_2
        print 'Hasil Perkalian',total


elif pilih == 4:
       print
       angka_1 = input('Masukan angka Pertama: ')
       angka_2 = input('Masukan Angka Kedua: ')
       total = angka_1 / angka_2
       print 'Hasil Pembagian',total
