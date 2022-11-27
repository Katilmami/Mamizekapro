
	
	
from gtts import gTTS
import random
from os import path
import os


















tts = gTTS(text="hoşgeldin", lang="tr")
tts.save('hoşgeldin.mp3')
os.system("mpv hoşgeldin.mp3")
os.system("rm hoşgeldin.mp3")
os.system("clear")


print(" ")
print(" ")
print(" ")
os.system("figlet Mami Zeka")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Hoşgeldin")













hosbulduk_komutu = "hoşbulduk"
tamam_komutu = "tamam"
by_komutu = "byby"
baybay_komutu = "baybay"
canim_komutu = "canim"
canım_komutu = "canım"
neden_komutu = "neden"
ensevdin_komutu = "beni seviyor musun"
seni_komutu = "seni seviyorum"
deli_komutu = "deli"
nerelisin_komutu = "nerelisin"
selam_komutu = "selam"
exit_command = "exit"
espiri_komutu = "espiri"
espiri2_komutu = "espiri yap"
şaka2_komutu = "şaka yap"
şaka_komutu = "saka"
merhaba_komutu ="merhaba"
nasılsın_komutu ="nasılsın"
nasilsin_komutu ="nasilsin"
adin_komutu ="adin ne"
adın_komutu ="adın ne"
sa_komutu ="sa"
senkimsin_komutu ="sen kimsin"
günaydin_komutu = "günaydin"
günaydın_komutu = "günaydın"
neyapmalıyım_komutu = "neyapmalıyım"
neyapmaliyim_komutu = "neyapmaliyim"
sg_komutu = "sg"
beyinsiz_komutu = "beyinsiz"
yaş_komutu = "kaç yasindasin"
en_iyi_komut = "anladığımdan emin değilim de"










saka_havuzu = ["Gitme dur. Niye ne oIdu? – Duracak mısın diye merak ettim şimdi git. 🤣🤣🤣🤣", "AIo Emin’Ie görüşecektim yanIış numara – Emin misin?- Evet – Hani yanIış numaraydı. hahahahahahahahah","İçimden bir ses kaIk ders çaIış diyor. Acaba annemi mi yedim Ia."]
neyapmalıyım_havuzu =["halay çek🕺🕺","müzik dinle🎶🎶","bu uygulamayı benim için arkadaşlarinla paylaş🤪","biraz uyu bence💤💤💤","ben nerden bilim tipe  bak treekk😡😡🤬😈", "spor yap🏋⛹🚴🤽","su iç evede csnimmm"]



while True:
   user_input = input().lower()
   if user_input == exit_command:
       break
   elif hosbulduk_komutu == user_input:
   	print(" ")
   elif deli_komutu == user_input:
       print ("evt çok deliyim🥸")       
   elif seni_komutu == user_input:
       print ("bende seni seviyorum bebegim 😍😘 ")
   elif ensevdin_komutu == user_input:
       print ("seni tanimiyorum")
   elif neden_komutu == user_input:
       print ("bilmemki sen bilirsin🤨🤨")
   elif canim_komutu == user_input or canım_komutu == user_input:
       print ("bu me samimiyet🤭")
   elif baybay_komutu == user_input or by_komutu == user_input:
       print ("güle güle")
   elif tamam_komutu == user_input:
       print ("okey")
   elif yaş_komutu == user_input:  
       print ("ben sonsuza kadar yaşiycam")
   elif beyinsiz_komutu == user_input:
       print("çok üzüldüm")  
   elif nasılsın_komutu == user_input or nasilsin_komutu == user_input:
       print("çok iyiyim🤪🤪")
   elif adin_komutu == user_input or adın_komutu == user_input:
       print("CİNO👻") 
   elif sa_komutu == user_input:
       print("aleyküm selam")
   elif senkimsin_komutu == user_input:
       print("ben benim 😉")      
   elif en_iyi_komut == user_input:
       print("sirinin boktan özeliği bende yok")   
   elif günaydin_komutu == user_input:
       print ("sanada günaydin 🛌🛌🛌")
   elif günaydın_komutu == user_input:
       print ("sanada günaydin 🛌🛌🛌")
   elif merhaba_komutu == user_input:
       print(" sanada merhaba😎😎") 
   elif sg_komutu == user_input:
       print(" çok üzüldüm")   
   elif selam_komutu == user_input:
       print("selam 😎😁")
   elif nerelisin_komutu == user_input:
       print("siber dünyaliyim")
         	
   
   
   
   
   elif neyapmalıyım_komutu == user_input or neyapmaliyim_komutu == user_input:
       havuzun_boyutu = len(neyapmalıyım_havuzu)
       rastgelesayi = random.randrange(0, havuzun_boyutu)
       neyapmalıyım = neyapmalıyım_havuzu[rastgelesayi]
       print(neyapmalıyım) 
   
   elif şaka_komutu == user_input or espiri_komutu == user_input or şaka2_komutu == user_input or espiri2_komutu == user_input:
       havuzun_boyutu = len(saka_havuzu)
       rastgelesayi = random.randrange(0, havuzun_boyutu)
       saka = saka_havuzu[rastgelesayi]
       print(saka)
   else:
       print("buna vericek cevabım yok malesef 🤯🤯")
print("by by")










