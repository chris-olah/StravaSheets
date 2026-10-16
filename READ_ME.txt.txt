In Source Folder Powershell: 
python -m venv .venv
.venv\Scripts\activate

pip install requests python-dotenv gspread google-auth

1) Get Strava Subscription for API access 
2) Create Google Cloud account and create StravaSheets project, create service account, create and download key to service account
3) Create python file to verify connection to google
4) Create Strava API application
5) Create .env file and update with strava client id and secret client id
6) Create python file to authorize strava api access 