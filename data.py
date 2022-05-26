import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()

results = response.json()
question_data = [data for data in results["results"]]
