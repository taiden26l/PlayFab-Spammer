# PlayFab Spamming
This PlayFab spamer was built purely focusing on speed.
The only output you will get is each thread counting successful requests.
Generally half of the successful requests will silently fail.
On average this should create 5000 accounts in 2 minutes if you have 16 CPU cores
> The code is messy, i know.

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
**note:** PlayFab Docs are garbage so these currently wont work
## Adding access policies
 - Open your title's dashboard
 - Click settings > Title settings
 - API Features tab
 - Locate ENTITY GLOBAL TITLE POLICY
 - Insert new policies into the existing Policy JSON array
