








from googlesearch import search
import time
import os


os.system('clear')
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
os.system("figlet Mami Zeka")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Mami Zeka Google Arama")




query = input("Mami zeka: ")

for google_search in search(query, start=0, stop=15):
	print(google_search)


for i in range(15,0,-1):
	print(i)
	time.sleep(1)

else:
	os.system("python .mamizeka2.py")