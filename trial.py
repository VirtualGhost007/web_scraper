import requests

# Define the proxy
proxy = {
    "http": "http://209.97.150.167:3128",
    "https": "http://209.97.150.167:3128"
}

# Example URL to test
url = "http://httpbin.org/ip"

try:
    # Send a request through the proxy
    response = requests.get(url, proxies=proxy, timeout=10)

    # Check response
    if response.status_code == 200:
        print("Proxy request successful!")
        print("Response:", response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.ProxyError:
    print("Proxy Error: Unable to connect to the proxy.")
except requests.exceptions.Timeout:
    print("Timeout Error: Request timed out.")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
