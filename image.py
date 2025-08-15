import requests
import os
import dotenv


dotenv.load_dotenv()
key = os.getenv("API")
token = os.getenv("BOT_TOKEN")
chat_id = 6736740776

url_nasa = f"https://api.nasa.gov/planetary/apod?api_key={key}"
response = requests.get(url_nasa)
data = response.json()
print(data)


image_url = data.get("hdurl") or data.get("url")
print("Today's NASA APOD Image URL:")

print(image_url)


# url_telegram = f"https://api.telegram.org/bot{token}/sendPhoto"
# payload = {
#         "chat_id": chat_id,
#         "photo": image_url,
#         # "caption": caption
#     }
# res = requests.post(url_telegram, data=payload)
# print(res)




