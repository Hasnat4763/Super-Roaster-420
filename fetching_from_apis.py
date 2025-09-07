import requests

def fetch_compliments():
    url = "https://compliments-api.vercel.app/random"
    response = requests.get(url)
    compliment = response.json()["compliment"]
    return compliment

def fetch_roasts():
    url  = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    roast = response.json()["insult"]
    return roast