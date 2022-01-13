import requests

url = "https://httpbin.org/cookies/set/sessioncookies/19"
url2 = "https://httpbin.org/cookies"
s = requests.Session()

try:
	reply = s.get(url)
	reply = s.get(url2)

except:
	print("Hiba")
	exit()

print(reply.status_code)
print(reply.json())
