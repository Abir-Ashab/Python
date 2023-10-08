import requests

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token
access_token = 'EAAE49YxDVdIBO0gttkG6TSi0WbMXtHvUDThXJO5TfBx4laQJ2GtqoCaLXcpMYRQoCZCULgNXpkyCh3z8dLpPEEWENWMyOB5tYgvvuuZAttjLWGF9OiJEE9jc5Firj1YxDkmK3XDK5rMs5PeXmXlMGbIrf72sx9uXLqZBPkQrxMI0vcPrYZBPFcpx0FiIgAfJNdPM8y0QW1oo0UMGV9b8HKlbLrYZAc6ZBc7jAKQyAcLJHGlDzpCqYUK0bD8QZDZD'

# Replace 'RECIPIENT_USER_ID' with the user ID of the recipient
recipient_user_id = '100076693968724'

# The message you want to send
message_text = 'Hello, this is a test message!'

# Create a JSON payload with the message data
message_data = {
    'recipient': {'id': recipient_user_id},
    'message': {'text': message_text}
}

# Make a POST request to send the message
url = f'https://graph.facebook.com/v14.0/{recipient_user_id}/messages'
params = {'access_token': access_token}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, params=params, headers=headers, json=message_data)

print(response)
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print('Failed to send message. Response content:')
    print(response.text)
