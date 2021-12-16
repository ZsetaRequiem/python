import requests

valasz = requests.get("http://localhost:300")
print (valasz.status_code)
print (valasz.txt)
