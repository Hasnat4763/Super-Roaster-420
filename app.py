from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
from slack_sdk import WebClient
load_dotenv(".env")



bot_token = os.environ["SLACK_BOT_TOKEN"]
app_token = os.environ["SLACK_APP_TOKEN"]

app = App(token=bot_token)
client = WebClient(token=bot_token)

@app.command("/roaster_roastme")
def roast_me(ack, respond, command):
    ack()
    user_id = command["user_id"]
    respond(f"<@{user_id}> You are Not A Sigma!")
    
    
    
if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    handler.start()