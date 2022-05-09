import requests

dummy_data = {
    "date": '2022-05-09',
    "size": 10,
    "message": "For testing"
}

if __name__ == "__main__":
    response = requests.post("http://localhost:5000/doublesize", json=dummy_data)
    if response:
        print(response.json())