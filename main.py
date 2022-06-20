import os
import requests
import urllib.request
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
# Get your API key from api.nasa.gov



def get_image(title, image_url):
    try:
        urllib.request.urlretrieve(image_url, f"images/{title}.jpg")
        print("Downloaded successfully")
    except:
        print("Error downloading")



def get_apod():
    URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    r = requests.get(url = URL)
    if r.status_code == 200:
        data = r.json()
        print(data)

        
        date = data['date']
        title = data['title']
        explanation = data['explanation']
        image_hdurl = data['hdurl']
        image_url = data['url']
        get_image(title, image_hdurl)
    else:
        get_apod()


get_apod()