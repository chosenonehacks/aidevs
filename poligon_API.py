import requests
import json

# Step 1: Fetch the two strings from the URL
url = "https://poligon.aidevs.pl/dane.txt"
response = requests.get(url)
strings = response.text.strip().split()

print(strings)

# Step 2: Prepare the JSON payload in tabular format
payload = {
    "task": "POLIGON",
    "apikey": "xxxxxxxxxxxxxxxxx", # Replace with the actual API key
    "answer": strings
}

# Print the JSON payload to the console before sending it
print("JSON payload to be sent:")
print(json.dumps(payload, indent=4))

# Step 3: Send the strings to the API via a POST request
api_url = "https://poligon.aidevs.pl/verify"  # Replace with the actual API URL
headers = {'Content-Type': 'application/json'}
response = requests.post(api_url, json=payload, headers=headers)

# Step 4: Print the response from the API to the console
print(response.json())

# JSON semantic checker https://jsoncrack.com/editor