import json

map_city_to_coords = {
    'Abuja': '9.02N,7.31E',
    'Nairobi': '1.3S,36.85E',
    'Accra': "5.63N,0.39W"
}

def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        day_number = weather_data['day']
        temperature = weather_data['temperature']
        wind_speed = weather_data['wind_speed']
        return f'On day {day_number},\nThe temperature is {temperature} \nThe wind speed is {wind_speed}'

def show_weather():
    with open('show-weather-from-file\end/all_data.json', 'r') as f:
        all_data = json.load(f)
        all_forecasts = all_data['all_forecasts']

    if 'current_city' not in all_data:
        current_city = input('What is the current city where you want to see the weather?')
        all_data['current_city'] = current_city
        with open('all_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_data, f)
    else:
        current_city = all_data['current_city']

    city_name = current_city
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        coords = map_city_to_coords[city_name]
        weather_data_list = all_forecasts[coords]
        print(show_weather_to_user(weather_data_list))

show_weather()
