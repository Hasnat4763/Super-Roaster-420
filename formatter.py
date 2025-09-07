def format(data, type, user):
    blocks = []

    blocks.append({
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"💬 Here's your {type}!",
        }
    })
    blocks.append({"type": "divider"})
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"<@{user}> {data}"
        }
    })

    return blocks
