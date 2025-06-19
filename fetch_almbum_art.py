import requests
import csv
import time

# Paste token here from get_spotify_token.py
token = 'YOUR OWN TOKEN'
# Input CSV:
input_csv = 'spotify_top50.csv'
# Output CSV:
output_csv = 'spotify_top50_with_art.csv'

# Open CSV to read
with open(input_csv, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Prepare new CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['Position', 'Track', 'Artist', 'AlbumArt']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        search_query = f"{row['Track']} {row['Artist']}"
        print(f"Searching: {search_query}")

        search_url = "https://api.spotify.com/v1/search"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        params = {
            "q": search_query,
            "type": "track",
            "limit": 1
        }

        response = requests.get(search_url, headers=headers, params=params)
        data = response.json()

        # Default fallback:
        album_art_url = 'assets/album-placeholder.jpg'

        try:
            album_art_url = data['tracks']['items'][0]['album']['images'][0]['url']
            print(f"✅ Found album art: {album_art_url}")
        except (IndexError, KeyError):
            print("❌ Album art not found — using placeholder.")

        # Write row to new CSV
        writer.writerow({
            'Position': row['Position'],
            'Track': row['Track'],
            'Artist': row['Artist'],
            'AlbumArt': album_art_url
        })

        time.sleep(0.2)  # polite delay between requests

print(f"\n✅ Done! Saved: {output_csv}")
