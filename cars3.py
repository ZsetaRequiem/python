import requests
import json
newcar = ("id":8, "brand": "Opel", "model": "Astra","production_year": 1988, "convertible": True)
h_content =
try:
	keszit = requests.post("http://localhoszt:3000/cars , data = json.dumps(newcar)", headers = h_content)
	print(keszit.status_code)
	olvas = requests.get("http://localhost:3000/cars")
	print(olvas.text)
except:
	print("hiba")
