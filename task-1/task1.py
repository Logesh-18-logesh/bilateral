def aggregate_weather_data(records):
    city_data = {}

    for record in records:
        city = record.get('city')

        if city:
            temperature = record.get('temperature')
            humidity = record.get('humidity')

            if city not in city_data:
                city_data[city] = {
                    'temperature_sum': 0,
                    'temperature_count': 0,
                    'humidity_sum': 0,
                    'humidity_count': 0
                }

            if temperature is not None:
                city_data[city]['temperature_sum'] += temperature
                city_data[city]['temperature_count'] += 1

            if humidity is not None:
                city_data[city]['humidity_sum'] += humidity
                city_data[city]['humidity_count'] += 1

    city_averages = {}
    for city, data in city_data.items():
        temperature_avg = data['temperature_sum'] / data['temperature_count'] if data['temperature_count'] != 0 else None
        humidity_avg = data['humidity_sum'] / data['humidity_count'] if data['humidity_count'] != 0 else None
        city_averages[city] = {'temperature_avg': temperature_avg, 'humidity_avg': humidity_avg}

    return city_averages

records = [
    {'city': 'New York', 'temperature': 25, 'humidity': 60},
    {'city': 'New York', 'humidity': 55},
    {'city': 'Chicago', 'temperature': 20},
    {'city': 'Chicago', 'temperature': 22, 'humidity': 50},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 70},
    {'city': 'Los Angeles', 'temperature': 32, 'humidity': 65},
    {'city': 'Miami', 'humidity': 80},
    {'city': 'Miami', 'temperature': 28}
]

city_averages = aggregate_weather_data(records)
for city, averages in city_averages.items():
    print(f"City: {city}, Average Temperature: {averages['temperature_avg']}, Average Humidity: {averages['humidity_avg']}")
