# Protecting your game from PlayFab spamming
## You can use API access policy to disable the APIs you are not using, such as:
 - Login With Custom ID.
```
{
    "Resource": "pfrn:api--/Client/LoginWithCustomID",
    "Action": "*",
    "Effect": "Deny",
    "Principal": "*",
    "Comment": "Deny client access to LoginWithCustomID"
}
```
 - Register PlayFab User
```
{
    "Resource": "pfrn:api--/Client/RegisterPlayFabUser",
    "Action": "*",
    "Effect": "Deny",
    "Principal": "*",
    "Comment": "Deny client access to RegisterPlayFabUser"
}
```
```
{
    "Action": "*",
    "Effect": "Deny",
    "Principal": "*",
    "Resource": "pfrn:api--/Client/RegisterPlayFabUser",
    "Condition": {
        "NumericLessThanEquals": {
            "playfab/Request/ApiRequestsPerMinutePerUser": 10
        }
    },
    "Comment": "Rate limit client access to RegisterPlayFabUser"
}
```
```
{
    "Action": "*",
    "Effect": "Deny",
    "Principal": "*",
    "Resource": "pfrn:api--/Client/RegisterPlayFabUser",
    "Condition": {
        "NumericLessThanEquals": {
            "playfab/Request/ApiRequestsPerMinute": 10
        }
    },
    "Comment": "Rate limit client access to RegisterPlayFabUser (globally)"
}
```
**note:** I got those last two rate limit policies partially from ChatGPT, they might not be real.
## Adding access policies
 - Open your title's dashboard
 - Click settings > Title settings
 - API Features tab
 - Locate ENTITY GLOBAL TITLE POLICY
 - Insert new policies into the existing Policy JSON array
