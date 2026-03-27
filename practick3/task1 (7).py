import requests

API_KEY = "79d1ca96933b0328e1c7e3e7a26cb347"

def main():
    # ввод города с консоли
    city = input("Введите название города: ")

    # формируем запрос
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "lang": "ru",
        "appid": API_KEY
    }

    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url, params=params).json()

    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data["main"]["temp"])
    temperature_feels = round(weather_data["main"]["feels_like"])

    # ветер
    wind_speed = weather_data["wind"]["speed"]
    wind_message = f"Скорость ветра: {wind_speed} м/с"

    # давление и влажность
    pressure = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]

    # описание погоды
    weather_description = weather_data["weather"][0]["description"].lower()

    if "ясно" in weather_description:
        weather_status = "Ясно"
    elif "облачно с прояснениями" in weather_description:
        weather_status = "Облачно с прояснениями"
    elif "облачно" in weather_description or "пасмурно" in weather_description:
        weather_status = "Облачно"
    elif "снег" in weather_description:
        weather_status = "Снег"
    elif "дождь" in weather_description:
        weather_status = "Дождь"
    else:
        weather_status = weather_description.capitalize()

    # вывод результата
    print("Сейчас в городе", city, str(temperature), "°C")
    print("Ощущается как", str(temperature_feels), "°C")
    print(wind_message)
    print("Давление:", pressure, "гПа")
    print("Влажность:", humidity, "%")
    print("Погода:", weather_status)

if __name__ == "__main__":
    main()