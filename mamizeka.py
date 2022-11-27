#!/usr/bin/env python3

import os

os.system("clear")
os.system("clear")
os.system("figlet Mami Zeka")
print("""
İslemler

1) Google Arama Mami zeka (yarı çalışıyor)
2) Sohbet Mami zeka (tamamlanmamış)
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        os.system("clear")
        os.system("python .mamizeka2.py")
elif islemno=="2":
          os.system("clear")
          os.system("python .mamizeka.py")
elif islemno=="3":
          os.system("clear")
          os.system("")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
