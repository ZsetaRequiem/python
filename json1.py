import json

d = {"nev":"Pisti","telefonszam":"06309799499"}
with open("json-dump1",'w') as f:
	json.dump(d,f)
