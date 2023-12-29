import requests

def get_location(ip_addr):
    from src.cnc import gradientText

    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    version = response['version']
    city = response['city']
    region_city = response['region']
    country_name = response['country_name']
    latitude = response['latitude']
    longitude = response['longitude']
    timezone = response['timezone']
    network = response['network']

    location_data = gradientText(f'''
IPv4          : {ip_address}
NETWORK       : {network}
VERSION       : {version}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}
''', (147, 103, 176), (189, 174, 199))

    return location_data

def ip_to_loc(args, send, client):
    from src.cnc import gradientText

    
    try:
        ip = ''
        if len(args) == 2:
            ip = str(args[1])
            ip_location = get_location(ip)
            for x in ip_location.split('\n'):
                send(client, x)
        else:
            send(client, gradientText('\n!GEOIP [IP]\n', (147, 103, 176), (189, 174, 199)))
    except:
        send(client, gradientText('\nInvalid data\n', (255,0,0), (255,100,100)))