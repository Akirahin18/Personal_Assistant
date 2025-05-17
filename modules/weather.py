import requests

def get_weather(city):
    API_KEY = "YOUR WEATHER API"  
    url = f"YOUR WEATHER API URL"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if response.status_code == 200 and "main" in data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The temperature in {city} is {temp}°C with {desc}."
        return f"Error: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
