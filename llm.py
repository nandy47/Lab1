import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("NVIDIA_API_KEY")
#print(API_KEY)

URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def call_model(messages):
    
    headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    }
    
    payload = {
    "messages": messages,
    "model": "meta/llama-3.1-8b-instruct",
    }

    #solving for invalid(403)/missing(401) API keys
    try:
        response = requests.post(URL, headers= headers, json = payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.exceptions.HTTPError as e: 
        status = e.response.status_code

        if status == 401:
            print("Error: NVIDIA_API_KEY is not set. Please add a valid API key.")
        elif status == 403:
            print("Error: Invalid NVIDIA_API_KEY")
        
        raise SystemExit(1) #ends program

    #solving for wi-fi disconnection

    except requests.exceptions.ConnectionError:
        print("Network error: Unable to connect to the NVIDIA API. Please check your internet connection.")
        return None

