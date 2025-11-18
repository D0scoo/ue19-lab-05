import requests

Site = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(Site)
joke = response.json()

print(joke.get('setup'))
print(joke.get('punchline'))