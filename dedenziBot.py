import properties
from slack_sdk import WebClient

class SlackAPI:
    def __init__(self):
        self.client = WebClient(properties.TOKEN)
        
    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        
        channels = result.data['channels']
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        channel_id = channel["id"]
        
        return channel_id
    
    #만약 return하는 값이 비어있다면, 아무도 모이지 않았어요...! 라는 메시지 던지는 예외처리        
    def get_reactions(self, channel_id, timestamp):
        result = self.client.reactions_get(channel = channel_id, timestamp=timestamp)
        jsonObject = result.data['message']
        reactions = jsonObject['reactions']
        
        for reaction in reactions:
            if reaction.get('name') == properties.TARGET_REACTION :
                return reaction.get('users') 
    
    # list들의 list를 받아서 post한다. 
    def post_message(self, channel_name, user_lists):
        
        # 이런식으로 유저를 mention할 수 있다.
        for user_list in user_lists:
            user_mention_list = ""
            for user in user_list:
                user_mention_list += '<@'+user+'> '
            print(user_mention_list + properties.TEAM_MATCHING_MESSAGE)
            self.client.chat_postMessage(channel = channel_name, text=user_mention_list + properties.TEAM_MATCHING_MESSAGE)
    
    def post_init_message(self, channel_name):
        result = self.client.chat_postMessage(channel=channel_name, text= properties.SLACK_INIT_MESSAGE)
        return result.data['ts']