import os
import requests

# Set up API key and base URL
openai_api_key = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
openai_api_base = "https://oneapi.365jpshop.com/v1"

# Set up request parameters
model_id = "code-davinci-002"
prompt = "Write a Python function to calculate the factorial of a number."
max_tokens = 100
temperature = 0.7

# Construct request body
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}",
}
data = {
    "model": model_id,
    "prompt": prompt,
    "max_tokens": max_tokens,
    "temperature": temperature,
}

# Send request and handle response
response = requests.post(openai_api_base + "completions", headers=headers, json=data)
if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["text"])
else:
    print(f"Request failed with status code {response.status_code}")
