from bs4 import BeautifulSoup
import requests


def get_usd_rate():
    response = requests.get("https://sensebank.ua/currency-exchange")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all(class_="exchange-rate-tabs__info-value h4")

        if soup_list:
            res = soup_list[0].text.strip()
            res = res.replace(",", ".").strip()
            try:
                usd_rate = float(res)
                return round(usd_rate, 2)
            except ValueError:
                pass



def convertor():
    usd_rate = get_usd_rate()

    if usd_rate:
        try:
            amount = float(input("Введіть значення в гривнях: "))
            converted = round(amount / usd_rate, 2)
            print(f"{amount} грн = {converted} USD")
        except ValueError:
            print("Введить коректне число.")


convertor()
