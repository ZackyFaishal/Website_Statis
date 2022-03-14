import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)
# Request ke website
page =requests.get("https://www.republika.co.id/")
# Extract konten menjadi BeautifulSoup
obj = BeautifulSoup(page.text,'html.parser');

print ('\nMenampilkan semua teks headline')
print ('=================================')
for headline in obj.find_all('div',class_='conten1'):
    print (headline.find('h2').text)
    
print('\nMenampilkan kategori')
print('========================')
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

print('\nMenampilkan waktu publish')
print('========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)

current_time = now.strftime("%H:%M:%S")

print('\nMenampilkan waktu scrapping')
print('===============================')
print("waktu Scrapping =",current_time)

# Deklarasi list kosong
data=[]
# Lokasi file json
f=open(r'C:\POLBAN MATERI\SEMESTER 2\proyek pengembangan perangkat lunak desktop\Pertemuan 6\Web scrapping 1 (Beautiful Soup)\headline.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktupublish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data, indent = 2)
f.writelines(jdumps)
f.close()