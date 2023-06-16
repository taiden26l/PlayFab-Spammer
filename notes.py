import requests, json, secrets, os, threading

/Client/LoginWithCustomID

j = json.dumps(request)
def GetURL(getParams ) : #2nd parameter see lower
    f"https://{TitleId}.playfabapi.com/Client/LoginWithCustomID"
    if getParams:
        for idx, (k, v) in enumerate(getParams.items()):
            if idx == 0:
                url.append("?")
            else:
                url.append("&")
            url.append(k)
            url.append("=")
            url.append(v)

    return "".join(url)

requestHeaders = {}
requestHeaders["Content-Type"] = "application/json"
requestHeaders["X-PlayFabSDK"] = PlayFabSettings._internalSettings.SdkVersionString
requestHeaders["X-ReportErrorAsSuccess"] = "true"
    
httpResponse = requests.post(url, data=j, headers=requestHeaders)

if httpResponse.status_code == 200:
    # again



#lower
PlayFabSettings._internalSettings.RequestGetParams

add print(getParams) into PlayFabSettings.py

??? necessary at all???

from playfab import PlayFabSettings
import playfab.PlayFabErrors as PlayFabErrors
import sys, traceback
def _GetURL(methodUrl, getParams):
    url = []
    url.append("https://")
    url.append(TitleId)

    url.append(".playfabapi.com")
    url.append(methodUrl)

    if getParams: ###########
        for idx, (k, v) in enumerate(getParams.items()):
            if idx == 0:
                url.append("?")
            else:
                url.append("&")
            url.append(k)
            url.append("=")
            url.append(v)
    print("".join(url))
    return "".join(url)

PlayFabSettings.GetURL = _GetURL