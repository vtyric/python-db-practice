import services, schemas, database, requests
from bs4 import BeautifulSoup


def load_kofemolki_data():
    url = 'https://price.ru/kofemolki/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    item_list = soup.find_all("div", class_="p-card p-card__model p-card__tile")
    for item in item_list[:20]:
        item_name = item.find('div', class_='p-card__title text-body-m-book').text.strip()
        item_price = _get_digit_from_str(
            item.find('span', class_='p-card__price--new text-subtitle-price-bold').text.strip()
        )
        kofemolka_create = schemas.KofemolkaCreate(name=item_name, price=item_price)
        services.create_kofemolka(database.SessionLocal(), kofemolka_create)


def _get_digit_from_str(input_str: str):
    res = ''
    for item in input_str:
        if item.isdigit():
            res += item

    return int(res)
