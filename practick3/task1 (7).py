#1.Ввод названия города с консольного ввода

#2.Отобразить следующие характеристики:
#•Температура,
#•Как ощущается, 
#•Сообщение про ветер,
#•Давление в ед. изм,
#•Влажность %,
#•Ясно/облачно/снег/дождь/облачно с прояснениями
#•и  др.


import requests

# Уникальный ключ доступа к API OpenWeatherMap
API_KEY = "79d1ca96933b0328e1c7e3e7a26cb347"

def main():
    # Ввод названия города пользователем
    city = input("Введите название города: ")

    # URL эндпоинта и параметры запроса
    # units=metric преобразует температуру из Кельвинов в Цельсии
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "lang": "ru",
        "appid": API_KEY
    }

    # Выполняем GET-запрос и сразу парсим JSON-ответ в словарь
    weather_data = requests.get(url, params=params).json()

    # Извлекаем температуру и округляем до целого числа
    temperature = round(weather_data["main"]["temp"])
    temperature_feels = round(weather_data["main"]["feels_like"])

    # Получаем скорость ветра (метры в секунду)
    wind_speed = weather_data["wind"]["speed"]
    wind_message = f"Скорость ветра: {wind_speed} м/с"

    # Давление (в гектопаскалях) и влажность (в процентах)
    pressure = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]

    # Берем текстовое описание из вложенного списка weather
    weather_description = weather_data["weather"][0]["description"].lower()

    # Кастомная классификация статуса погоды на основе ключевых слов в описании
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
        # Если ключевое слово не найдено, просто выводим описание с заглавной буквы
        weather_status = weather_description.capitalize()

    # Вывод всех собранных данных в консоль
    print("Сейчас в городе", city, str(temperature), "°C")
    print("Ощущается как", str(temperature_feels), "°C")
    print(wind_message)
    print("Давление:", pressure, "гПа")
    print("Влажность:", humidity, "%")
    print("Погода:", weather_status)

if __name__ == "__main__":
    main()
