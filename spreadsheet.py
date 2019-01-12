import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_server.json', scope)
client = gspread.authorize(creds)

sheet = client.open('pizza_bot').sheet1

#all shenanigans below

column = ["pepperoni", "margarita", "mushrooms", "pizza", "huiza"]
for i in range(1, len(column)):
    sheet.update_cell(i, 1, column[i])


