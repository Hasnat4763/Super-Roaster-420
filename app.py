from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
from slack_sdk import WebClient
load_dotenv(".env")
from fetching_from_apis import fetch_compliments, fetch_roasts, fetch_random



bot_token = os.environ["SLACK_BOT_TOKEN"]
app_token = os.environ["SLACK_APP_TOKEN"]

app = App(token=bot_token)
client = WebClient(token=bot_token)


@app.event("app_mention")
def compliment_me(body, say):
    event = body.get("event", {})
    user_id = None
    response = None

    choicesample = event.get("text","").split()
    
    choice = choicesample[1].lower()
    
    if choicesample[2].lower() == "me":
            user_id = event.get("user")
    else:
        user_id = choicesample[2].strip("<>@")


    if choice == "compliment":
        response = fetch_compliments(user_id)
        
    elif choice == "roast":
        response = fetch_roasts(user_id)
        
    elif choice == "random":
        response = fetch_random(user_id)
        
    else:
        response = "Please use the format '@Super Roaster 420 compliment me' or '@Super Roaster 420 roast @username' or '@Super Roaster 420 random me"
        user_id = event.get("user")

    say(blocks = response, text=f"<@{user_id}> {response}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    handler.start()
    