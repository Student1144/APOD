import streamlit as st
import requests as r
import os
import dotenv

dotenv.load_dotenv(".env")
apikey = os.getenv("api_key")
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

re = r.get(url)
content = re.json()

title = content["title"]

st.title("Astronomy Picture Of the Day!")
st.header(title)

imgurl = content["url"]
response = r.get(imgurl)

with open("image.jpg", "wb") as file:
    file.write(response.content)

st.image("image.jpg")

st.write(content["explanation"])