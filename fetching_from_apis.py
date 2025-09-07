import requests
import random
from formatter import format

def fetch_compliments(user):
    url = "https://compliments-api.vercel.app/random"
    response = requests.get(url)
    compliment = response.json()["compliment"]
    return format(compliment, "compliment", user)

def fetch_roasts(user):
    url  = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    roast = response.json()["insult"]
    return format(roast, "roast", user)

def fetch_random(user):
    if random.choice([True, False]):
        response = fetch_compliments(user)
    else:
        response = fetch_roasts(user)
    return response