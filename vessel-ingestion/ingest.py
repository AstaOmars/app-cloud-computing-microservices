import requests

url = "http://localhost:5001/ingest"
files = {'file': open('/path/to/yourfile.json', 'rb')}

response = requests.post(url, files=files)
print(response.json())
