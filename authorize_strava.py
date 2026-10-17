
import os
import json
import requests
import webbrowser
from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv

# set debug to 1 for console output debug
DEBUG = 0

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

print(
    "\nAuthorize the application. When localhost refuses "
    "the connection, copy the full URL from your browser."
)

redirected_url = input("\nPaste redirected URL here: ").strip()

# parse url and grab code 
query = parse_qs(urlparse(redirected_url).query)

if "error" in query: 
    raise RuntimeError("Strava authorization was denided.")

code = query.get("code", [None])[0]

if not code:
    raise ValueError("No authorization code found. Paste the full redirected URL from browser")

print("\nExchanging authroization code with Strava")

# send HTTP post request to Strava
response = requests.post(
    "https://www.strava.com/oauth/token",
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
    },
    timeout=30,
)

if not response.ok:
    print("Strava returned HTTP", response.status_code)
    print("Response:", response.text)
    raise RuntimeError("Token exchange failed.")

# parse response if successful 
token_data = response.json()

if "access_token" not in token_data:
    raise RuntimeError("Strava response did not contain an access token.")

# store token from strava 
token_path = Path(__file__).resolve().parent / "token.json"

with token_path.open("w", encoding="utf-8") as file:
    json.dump(token_data, file, indent=2)

print("Strava authorization completed.")
print(f"Token saved to: {token_path}")

# debugging values output
if DEBUG == 1:
    print("Client ID:", client_id, " --- ", "Client Secret Key", client_secret)
    print("STRAVA URL:",authorize_url, "\n")
    print("query: ", query)
    print("response: ", response)