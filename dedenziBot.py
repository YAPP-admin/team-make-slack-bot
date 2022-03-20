import properties
from slack_sdk import WebClient

class SlackAPI:
    def __init__(self):
        self.client = WebClient(properties.TOKEN)
        
    # 채널이 없으면 예외던지기
    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        
        channels = result.data['channels']
        # 채널이 없으면 여기서 IndexError가 터짐
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        channel_id = channel["id"]
        
        return channel_id
    
    # 만약 return하는 값이 비어있거나 한명이라면, 아무도 모이지 않았어요...! 라는 메시지 던지는 예외처리
    # reaction에 값이 없다면? 예외던지기
    def get_reactions(self, channel_id, timestamp):
        result = self.client.reactions_get(channel = channel_id, timestamp=timestamp)
        jsonObject = result.data['message']
        # 만약 reaction이 없다면, KeyError 터짐
        reactions = jsonObject['reactions']
        
        for reaction in reactions:
            if reaction.get('name') == properties.TARGET_REACTION :
                # 요기서 users가 없거나 1명 있으면 사람이 없다는 예외 던짐
                return_result = reaction.get('users') 
                if return_result <= 1:
                    raise Exception('팀 만들만큼 사람이 없어요!')
    
    # list들의 list를 받아서 post한다. 
    def post_message(self, channel_name, user_lists):
        
        # 이런식으로 유저를 mention할 수 있다.
        for user_list in user_lists:
            user_mention_list = ""
            for user in user_list:
                user_mention_list += '<@'+user+'> '
            self.client.chat_postMessage(channel = channel_name, text=user_mention_list + properties.TEAM_MATCHING_MESSAGE)
    
    def post_init_message(self, channel_name):
        result = self.client.chat_postMessage(channel=channel_name, text= properties.SLACK_INIT_MESSAGE)
        return result.data['ts']
    
    def post_error_message(self, channel_name, error_contents):
        self.client.chat_postMessage(channel=channel_name, text = error_contents)