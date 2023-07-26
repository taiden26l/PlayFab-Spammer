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
