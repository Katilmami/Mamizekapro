#!/usr/bin/env python3

import os

os.system("clear")
os.system("pkg install git -y")
os.system("pkg install nmap -y")
os.system("pkg install whois")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet MAMI")
print("""
İslemler

1) Site İslemleri
2) Hacker İslemleri
3) discord bot islemleri
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        os.system("clear")
        os.system("python3 mamihackersite.py")
elif islemno=="2":
          os.system("clear")
          os.system("python3 mamihackerhacker.py")
elif islemno=="3":
          os.system("clear")
          os.system("python3 botekrani.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     quit()
