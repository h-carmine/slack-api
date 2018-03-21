from slackclient import SlackClient
import os

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

users = sc.api_call("users.list")
members = users["members"]

for m in members:
    print(m["profile"]["real_name_normalized"])
