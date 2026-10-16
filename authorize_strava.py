
import os
import json
import requests
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv

DEBUG = 1

# load keys from .env file 
load_dotenv()

client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")

# verify strava credentials exist
if not client_id or not client_secret:
    raise ValueError("Missing Strava Credentials in .env file")

strava_url_params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost/exchange_token",
    "approval_prompt": "auto",
    "scope": "read,activity:read_all",
}

authorize_url = "https://www.strava.com/oauth/authorize?" + urlencode(strava_url_params)


print("Opening Strava Authorization")
webbrowser.open(authorize_url)

### incomplete
print("\nAuthorize the application in your browser.")
print("After approval browser will redirect to localhost. (you will see connection refused, this is expected, look code in between 'code=' and '&' somewhere in URL and it worked")
redirected_url = input("\nPaste redirected URL here: ").strip()

# debugging values output
if DEBUG == 1:
    print("Client ID:", client_id, " --- ", "Client Secret Key", client_secret)
    print("STRAVA URL:",authorize_url, "\n")