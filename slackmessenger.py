from slackclient import SlackClient


class SlackMessenger():
    def __init__(self, slack_token):
        self.sc = SlackClient(slack_token)

    def members(self):
        users = self.sc.api_call("users.list")
        members = users["members"]
        return members

    def user_id(self, user_name):
        user = [m for m in self.members() if m["profile"]["real_name_normalized"] == user_name][0]
        id = user['id']
        return id

    def open_conversation(self, user_name):
        user_id = self.user_id(user_name)
        conversation = self.sc.api_call("conversations.open", users=[user_id])
        return conversation

    def channel_id(self, user_name):
        conversation = self.open_conversation(user_name)
        return conversation['channel']['id']

    def send(self, user_name, message, as_user=False):
        channel_id = self.channel_id(user_name)
        response = self.sc.api_call("chat.postMessage", channel=channel_id, text=message, as_user=as_user)
        return response
