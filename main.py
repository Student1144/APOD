import streamlit as st
import requests as r
import os
import dotenv

dotenv.load_dotenv(".env")
apikey = os.getenv("api_key")
url = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key={apikey}"

re = r.get(url)
content = re.json()

title = content[0]["title"]

st.title("Astronomy Picture Of the Day!")
st.header(title)

imgurl = content[0]["hdurl"]
response = r.get(imgurl)

with open("image.jpg", "wb") as file:
    file.write(response.content)

st.image("image.jpg")

st.html(content[0]["explanation"])