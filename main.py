# Author: Krisna Santosa
# Description: This script will retrieve all verses from the Quran API and save them to text files.
# The text files will be saved in the text folder.
# run this script with python3 main.py

import requests
import os

endpoint = "https://quran-api-id.vercel.app/surahs/"

def save_verse_to_file(surah_number, verse_number, arabic_text):
    filename = f"{surah_number:03}{verse_number:03}.txt"
    
    if not os.path.exists("text"):
        os.mkdir("text")
        
    filename = os.path.join("text", filename)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(arabic_text)

def get_ayahs(surah_number):
    response = requests.get(f"{endpoint}{surah_number}")
    bismillah = response.json()["bismillah"]["arab"]
    ayahs = response.json()["ayahs"]
    for verse in ayahs:
        ayah = verse["arab"]
        verse_number = verse["number"]["inSurah"]
        if( surah_number != 1 ):
            save_verse_to_file(surah_number, 0, bismillah)

        save_verse_to_file(surah_number, verse_number, ayah)
        print(f"Surah {surah_number} verse {verse_number} saved.")

def main():
    response = requests.get(endpoint)
    if response.status_code == 200:
        surahs = response.json()
        for surah in surahs:
            surah_number = surah["number"]
            get_ayahs(surah_number)
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    main()
