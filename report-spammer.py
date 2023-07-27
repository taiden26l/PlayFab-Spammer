import playfab
from playfab import PlayFabClientAPI, PlayFabSettings

# WORK IN PROGRESS THIS OBV DOESNT WORK
PLAYFAB_TITLE_ID = "83BF3"
PlayFabSettings.TitleId = PLAYFAB_TITLE_ID

def login_callback(result, error):
    player_id = '00000000'
    report_comment = 'Hello World.'
    send_report(player_id, report_comment)

def report_callback(result, error):
    print(result)

def login_with_custom_id(custom_id):
    request = {
        "CustomId": custom_id,
        "CreateAccount": True
    }
    PlayFabClientAPI.LoginWithCustomID(request, login_callback)

def send_report(player_id, comment):
    report_request = {
        "ReporteeId": player_id,
        "Comment": comment
    }
    result = PlayFabClientAPI.ReportPlayer(report_request, report_callback)

    print(result)

if __name__ == '__main__':
    custom_id = '12345678'
    login_with_custom_id(custom_id)
