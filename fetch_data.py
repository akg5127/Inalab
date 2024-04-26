import requests
import json

def fetch_data():
    url = 'http://localhost:5000/data'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print('Failed to retrieve data')

if __name__ == "__main__":
    fetch_data()
