from slackmessenger import SlackMessenger
import os

sm = SlackMessenger(os.environ["SLACK_API_TOKEN"])

user_name = 'slackbot'
message = 'good morning'
as_user = True

print(sm.send(user_name, message, as_user))
