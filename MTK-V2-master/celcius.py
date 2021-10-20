#mengubah skala fahrenheit menjadi celsius
#dengan persamaan C = (F - 32) X 5/9

fahrenheit = float(input("Masukkan nilai suhu dalam skala derajat fahrenheit :"))
celsius = float((fahrenheit - 32) * 5/9)
print("Nilai tersebut dalam skala celsius sebesar :", celsius)