import requests

API_KEY = "YOUR_GOOGLE_API_KEY"
CX = "YOUR_GOOGLE_CX"
QUERY = "spices"

url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CX}&key={API_KEY}&searchType=image"

response = requests.get(url)
data = response.json()

if "items" in data:
    print("Hasil pertama:", data["items"][0]["link"])
else:
    print("Tidak ditemukan hasil.")
