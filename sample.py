import requests
r = requests.get("https://www.youtube.com/")
output = r.text
print(output)