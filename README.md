# Top50MusicUSA
This project scrapes the current Top 50 Spotify USA chart and displays it as a clean, Spotify-inspired web page with album art, track titles, and artists — updated daily!  
✅ Python script uses Spotify API to fetch real-time album art 
✅ CSV stores Top 50 tracks 
✅ JavaScript dynamically builds the playlist 
🔥 Features
Live Top 50 USA songs

Displays track position, title, artist, album art

Uses Spotify API to get album art

Clean Spotify-style UI

Works fully client-side (no server needed)

Auto-refresh: fetch new art with updated token any time
1️⃣ Run get_spotify_token.py → Get Spotify API token
2️⃣ Run fetch_album_art.py → Generates spotify_top50_with_art.csv
3️⃣ Run local server:

bash
Copy
Edit
python -m http.server 8000
