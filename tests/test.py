import requests
from concurrent import futures

def send_request(url, payload):
    while True:
        response = requests.post(url, json=payload)
        # Process the response if needed

url = "http://example.com/your-endpoint"
payload = {"key": "value"}

with futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Send multiple requests concurrently using threads
    futures_list = [executor.submit(send_request, url, payload) for _ in range(10)]

    # Keep the main thread alive
    while True:
        continue
