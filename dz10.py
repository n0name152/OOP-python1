import sqlite3
from bs4 import BeautifulSoup
import requests
from datetime import datetime

response = requests.get("https://meteo.ua/164/dnepr-dnepropetrovsk#2025-02-28--16-00")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="menu-basic__degree")
    temperature = soup_list[0].text.strip().replace("", "")
    connection = sqlite3.connect("Temperature_DB.sl3",timeout=5)
    cur = connection.cursor()
    # cur.execute("CREATE TABLE weather_data (name TEXT);")
    current_time = datetime.now().strftime('%Y-%m-%d')
    cur.execute("INSERT INTO weather_data (datetime, temperature) VALUES (?, ?)", (current_time, temperature))

    connection.commit()
# print(connection)
# print(cur)
    connection.close()