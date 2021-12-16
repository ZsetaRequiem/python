import requests

try:
	r = requests.get("http://localhost:3000", timeout = 0.0000000000000001)
except requests.exceptions.Timeout:
	print("Hiba Timeout")
except:
	print("Altalanos hiba")
else:
	print(r.text)

