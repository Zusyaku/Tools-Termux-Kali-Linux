''' Program kalkulator sederhana untuk menjumlah, mengurang, mengali, dan membagi bilangan dengan menggunakan fungsi '''
import sys , os

# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu operasi
os.system("clear")
os.system("figlet MR.K7C8NG | lolcat")
print("\033[1;31;1m")
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   os.system("figlet Mohon Maaf | lolcst")
   print("Sepertinya Format Yang Anda Masukkan Salah")	
   print("Please Wait A Second")
   os.system("sleep 3"		
	os.system("python2 calcv2.py")
