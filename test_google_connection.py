import gspread
from google.oauth2.service_account import Credentials

credentials_file = "google_credentials.json"
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1T2SUtCpL4yDKkuqk81uvtR-cZVQkQ6xeufx0psliEeo/edit?gid=455751764#gid=455751764"

# set read/write permissions for sheet 
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# loads google service account credentials from credentials json file
credentials = Credentials.from_service_account_file(
    credentials_file,
    scopes=scopes
)

client = gspread.authorize(credentials)
spreadsheet = client.open_by_url(spreadsheet_url)

print("Connected successfully!")
print("Spreadsheet:", spreadsheet.title)
print("Worksheets:", [sheet.title for sheet in spreadsheet.worksheets()])

