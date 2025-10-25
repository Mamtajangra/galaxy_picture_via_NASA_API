import requests
import os
import dotenv


dotenv.load_dotenv()
key = os.getenv("API")
# token = os.getenv("BOT_TOKEN")
# chat_id = 6736740776
print(key)

# API=cz3A08Bd8UzaCN0rfGQJSJl1D3Flb9hybOhzjj2I
url_nasa = f"https://api.nasa.gov/planetary/apod?api_key={key}"
response = requests.get(url_nasa)
data = response.json()
print(data)


image_url = data.get("hdurl") or data.get("url")
print("Today's NASA APOD Image URL:")

print(image_url)







