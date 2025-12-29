import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
params = {
    "api_key": API_KEY
}
request_string = f"https://api.nasa.gov/planetary/apod"
print(request_string)

response = requests.get(request_string, params=params).json()

print(response['hdurl'])
img_url = response['hdurl']
img = requests.get(img_url).content
with open("image.png", "wb") as f:
    f.write(img)
st.title("Welcome to NASA World!!", text_alignment="center")
st.image(image="image.png")
st.write(response['explanation'])
# {'copyright': '\nAlan Chen\n', 'date': '2025-12-29', 'explanation': "This is the mess that is left when a star explodes.  The Crab Nebula, the result of a supernova seen in 1054 AD, is filled with mysterious filaments.  The filaments are not only tremendously complex but appear to have less mass than expelled in the original supernova and a higher speed than expected from a free explosion.  The featured image was taken by an amateur astronomer in Leesburg, Florida, USA over three nights last month. It was captured in three primary colors but with extra detail provided by specific emission by hydrogen gas. The Crab Nebula spans about 10 light years.  In the Nebula's very center lies a pulsar: a neutron star as massive as the Sun but with only the size of a small town.  The Crab Pulsar rotates about 30 times each second.   Explore the Universe: Random APOD Generator", 'hdurl': 'https://apod.nasa.gov/apod/image/2512/Crab_Chen_1920.jpg', 'media_type': 'image', 'service_version': 'v1', 'title': 'M1: The Crab Nebula', 'url': 'https://apod.nasa.gov/apod/image/2512/Crab_Chen_960.jpg'}
