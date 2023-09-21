import requests
from bs4 import BeautifulSoup


def make_request() -> requests.Response:
    url: str = 'https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/schengen-area/temporary-reintroduction-border-control_en'
    return requests.get(url)


def get_countries() -> []:
    r = make_request()
    if not r.status_code == 200:
        return []

    soup = BeautifulSoup(r.text, 'html.parser')
    return [country.text for country in soup.find_all("td", {"data-ecl-table-header": "Country"})]


def get_temporary_borders() -> {}:
    r = make_request()
    if not r.status_code == 200:
        return {}

    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all("td")

    result = {}
    for i in range(len(data) // 3):
        result[data[i * 3].text] = {'Start': data[i * 3 + 1].text.split("-")[0].strip(), 'End': data[i * 3 + 1].text.split("-")[1].strip(), 'Reason': data[i * 3 + 2].text}

    return result


def get_country(country) -> {}:
    r = make_request()
    if not r.status_code == 200:
        return {}

    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all("td")

    result = {}
    for i in range(len(data) // 3):
        if data[i * 3].text == country:
            result['Start'] = data[i * 3 + 1].text.split("-")[0].strip()
            result['End'] = data[i * 3 + 1].text.split("-")[1].strip()
            result['Reason'] = data[i * 3 + 2].text

    return result
    