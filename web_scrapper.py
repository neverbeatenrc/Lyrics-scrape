import requests
from bs4 import BeautifulSoup
import time

def scrape_main_verse(url:str, headers:dict) -> list:

    lyrics = ""

    try:
        print(f"Trying to access the url : {url}")
        time.sleep(3)
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        print(f"Successful! Status Code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        lyrics = soup.find("p", id = "songLyricsDiv")
        lyr = lyrics.get_text(separator="").strip()

        with open("sweater_weather.txt", "w", encoding="utf-8") as f:
            f.write(lyr)
  
        print("✅ Data saved to Sweater_weather.txt ")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Failed to connect to the server.")
    except requests.exceptions.Timeout:
        print("❌ The request timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ A general error occurred during the request: {req_err}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")



if __name__  == "__main__":
    url = "https://www.songlyrics.com/the-neighbourhood/sweater-weather-lyrics/"
    headers = {"User-Agent": "Mozilla/5.0"}
    scrape_main_verse(url=url, headers=headers)