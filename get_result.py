import requests

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = 'EAAE49YxDVdIBO5hFcXGJpfmmqNLgQx9zSjEewzqHVxvDcNbmFNRnvHdEdEqC41vqHRPrE7eXfHKI6nl7sQZAD6ou1vfasfSZBAcXZBk1KItSJ2fNxN8DwVgnpreTpNgZCZBWgmYVoHvJSUZCFZCttbvu7ZBAbywzCZBvBi27RoVaRON3sUnG3LaKDkQTZB307i5hWuGvIcTeKy5ZBs8KoDocwHWL61UP6HagRsVLN7bSmglPa9uwYomc5i25OWBNwZDZD'

# Make a GET request to retrieve user data
url = f'https://graph.facebook.com/me'
params = {'access_token': access_token}

response = requests.get(url, params=params)

if response.status_code == 200:
    user_data = response.json()
    print("User Data:")
    print(user_data)
else:
    print('Failed to fetch user data.')
