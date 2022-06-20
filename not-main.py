import requests
import urllib.request

API_KEY= "Get yours @ api.nasa.gov"



def get_apod():
    try:
        URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        r = requests.get(url = URL)
        data = r.json()
        title = data['title']
        image_url = data['url']
        urllib.request.urlretrieve(image_url, f"{title}.jpg")
        print("Astronomy Picture of the Day Downloaded successfully")
    except:
        print("Error")
        print("Trying again......")
        get_apod()

get_apod()