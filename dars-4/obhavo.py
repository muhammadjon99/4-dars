import requests
import datetime

def obhavomalumoti(shaharnomi):
    obhavoapi = '358b854d955ebbba525fbecd1ba0909c'
    url = 'https://api.openweathermap.org/data/2.5/weather'

    parametr = {
        'appid': obhavoapi,
        'q': shaharnomi,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=parametr)

    if response.status_code == 200:
        data = response.json()
        uzunlik = data['coord']['lon']
        kenlik = data['coord']['lat']
        havo = data['weather'][0]['main']
        toliq = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        harorat = data['main']['temp']
        tuyuladi = data['main']['feels_like']
        bosim = data['main']['pressure']
        namlik = data['main']['humidity']
        dengizsathi = data['main']['sea_level']
        korish = data['visibility']
        shamoltezligi = data['wind']['speed']

        bulutlar = data['clouds']['all']
        sana = data['dt']
        sana = datetime.datetime.fromtimestamp(sana)
        davlat = data['sys']['country']
        quyoshchiq = data['sys']['sunrise']
        quyoshchiq = datetime.datetime.fromtimestamp(quyoshchiq)
        quyoshbot = data['sys']['sunset']
        quyoshbot = datetime.datetime.fromtimestamp(quyoshbot)
        vaqtzonasi = data['timezone']

        text = f"""Shahar: {shaharnomi}
    Ob-havo: {havo}. {toliq}
    Harorat: {harorat}˚C. Tuyuladi {tuyuladi}˚C.
    Havo bosimi: {bosim}
    Namlik: {namlik}%
    Dengiz sathidan: {dengizsathi}m
    Ko'rish: {korish}m
    Shamol tezligi: {shamoltezligi}m/s
    Bulutlar: {bulutlar} ta
    Davlat: {davlat}

    Quyosh chiqishi: {quyoshchiq}
    Quyosh botishi: {quyoshbot}
    Vaqt zonasi: {vaqtzonasi}

    So'rov yuborilgan vaqt: {sana}

    Uzunlik: {uzunlik}
    Kenglik: {kenlik}


    """
        return text, icon
    else:
        return 'Shaxar topilmadi'