import requests
import json
import datetime

customerId = 'your customerId here'
apiKey = 'c2c6a454a5b317e10165e739848e9f0d'
key = '315ff1e75f172edd76f71aa5afccbc16'


def get_info(city_name, key):
    """
    Gets the weather and date-time information from the OpenWeather API.
    Returns it as a dictionary.
    """
    request_string = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

    info = requests.get(request_string).json()

    dt = datetime.datetime.fromtimestamp(info['dt'])

    info['lon'] = str(info['coord']['lon'])

    info['lat'] = str(info['coord']['lat'])

    return info


city_name = input('What city you want information for: ')
info = get_info(city_name, key)

lon = info['lon']
lat = info['lat']

url = 'http://api.reimaginebanking.com/atms?lat={}&lng={}&rad=1&key={}'.format(lat, lon, apiKey)
atm_info = requests.get(url).json()



def request(atm_info):
    """
    Handles the request sent in by the ESP32. Returns an already formatted
    string for the ESP32 to print out.
    """
    information = atm_info
    all_info = []
    all_info.append(information['name'])
    all_info.append(information['date'])
    all_info.append(information['time'])
    # all_info.append(information['lon'])
    # all_info.append(information['lat'])
    # all_info.append(information['temperature'])
    # all_info.append(information['weather'])
    # all_info.append(information['humidity'])
    # all_info.append(information['pressure'])
    all_info = "\n".join(all_info)
    return all_info


def kelvin_to_fahrenheit(temp):
    """
    Given a temperature in kelvin, returns the corresponding
    temperature in fahrenheit.
    """
    return round((temp - 273.15) * 9 / 5 + 32)

city_name = 'McLean'
info = get_info(city_name, key)
# lon = info['lon']
# lat = info['lat']
lat = '38.9283'
lon = '-77.1753'


def request(atm_info):
    """
    Handles the request sent in by the ESP32. Returns an already formatted
    string for the ESP32 to print out.
    """
    all_info = []
    all_info.append(atm_info['data'])
    all_info.append(atm_info['date'])
    all_info.append(atm_info['time'])
    all_info = "\n".join(all_info)
    return all_info


payload = {
    "type": "Savings",
    "nickname": "test",
    "rewards": 10000,
    "balance": 10000,
}
# Create a Savings Account
response = requests.post(
    url,
    data=json.dumps(payload),
    headers={'content-type': 'application/json'},
)

if response.status_code == 201:
    print('account created')
