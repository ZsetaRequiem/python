import requests, os, hashlib

kep = "image1.jpg"
kepmeret = os.path.getsize(kep)
jelszo = input("jelszot! ")
sha = hashlib.sha512(jelszo.encode("utf-8")).hexdigest()
url = "http://docker.lan:8420/"
d = {'password': sha, 'filesize': kepmeret}
try:
        f = open(kep, 'rb')
        valasz = requests.post(url, data = d, files = {'upfile': f})
        f.close()
except:
        print("Hiba")
        exit()
a = valasz.status_code
if a == 200:
        print("Jol mukodik")
elif a == 400:
        print("Nem adott meg fajlmeretet")
elif a == 401:
        print("Nem adtal meg jelszot")
elif a == 403:
        print("Nem jo jelszot adtal meg!")
elif a == 409:
        print("A fajl mar letezik")
elif a == 411:
        print("Nem jo a filemeret")
else:
        print("Belso hiba")
