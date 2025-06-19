import requests
import base64

# Replace with your real Client ID and Client Secret:
client_id = 'YOUR OWN TOKEN'
client_secret = 'YOUR OWN TOKEN'

# Encode for Authorization header
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Call Spotify Token API
response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={"grant_type": "client_credentials"},
    headers={"Authorization": f"Basic {b64_auth_str}"}
)

# Parse token
token = response.json().get("access_token")

if token:
    print("✅ Access token:")
    print(token)
else:
    print("❌ Failed to get token")
    print(response.json())
