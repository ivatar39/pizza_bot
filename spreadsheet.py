import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_server.json', scope)
client = gspread.authorize(creds)

sheet_pizza = client.open('pizza_bot').get_worksheet(0)
sheet_sushi = client.open('pizza_bot').get_worksheet(1)
pp = pprint

#all shenanigans below

pp.pprint(sheet_pizza.get_all_values())
pp.pprint(sheet_sushi.get_all_values())

