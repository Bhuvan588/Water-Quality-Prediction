import json
import requests

data = {"features":[0.940, 14.470,0.030,2.880,0.003,0.800,0.430,1.380,0.110,0.670,0.670,0.135,9.750,1.890,0.006,27.170,5.420,0.080,0.190,0.020]}

url = 'http://0.0.0.0:8000/predict/'

data = json.dumps(data)
response = requests.post(url, data)
print(response.json())