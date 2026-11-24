
import os
import requests
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

url = (
    "https://webapi.bps.go.id/v1/api/list/"
    "model/th/domain/0000/var/1/key/" + API_KEY
)

response = requests.get(url, timeout=60)

print("STATUS HTTP:", response.status_code)
print("RESPON BPS:")
print(response.text[:5000])

if response.status_code == 200:
    data = response.json()

    with open("periode_inflasi.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print("\nDaftar periode berhasil disimpan.")
