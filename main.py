import requests

api_key = ''
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

params ={
    'serviceKey' : api_key,
    'pageNo' : '1',
    'numOfRows' : '1000',
    'dataType' : 'JSON',
    'base_date' : '20240811',
    'base_time' : '1600',
    'nx' : '62',
    'ny' : '119'
}

response = requests.get(url, params=params)
data = response.json()
print(data)

weather_info = data['response']['body']['items']['item'][3]['obsrValue']
print(f'현재 기온은 {weather_info}입니다.')
