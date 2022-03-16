from slack_sdk import WebClient

LIMITED_NUMBER_OF_PEOPLE = 8
CHANNEL_NAME = "bot-test"
TARGET_REACTION = 'o'

class SlackAPI:
    def __init__(self, token):
        self.client = WebClient(token)
        
    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        
        channels = result.data['channels']
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        channel_id = channel["id"]
        
        return channel_id
    

    #만약 return하는 값이 비어있다면, 아무도 모이지 않았어요...! 라는 메시지 던지는 예외처리        
    def get_reactions_get(self, channel_id, timestamp):
        result = self.client.reactions_get(channel = channel_id, timestamp=timestamp)
        jsonObject = result.data['message']
        reactions = jsonObject['reactions']
        
        for reaction in reactions:
            if reaction.get('name') == TARGET_REACTION :
                return reaction.get('users') 
        
    def post_message(self, channel_name):
        result = self.client.chat_postMessage(channel = channel_name, text="test_slack_bot")
        return result.data['ts']
    
    def divid_member(self, members):
        total_member = len(members)
        print(members)
        set(members)
        
        
    def invite_number_of_people():
        print("good2")
        
        
    
token = "xoxb-3249488414740-3240702468902-lBOqqL4JBzCFlfm6G7og1gwW"
slack = SlackAPI(token)

channel_id = slack.get_channel_id(CHANNEL_NAME)
# created_at = slack.post_message("bot-test")
result = slack.get_reactions_get(channel_id, 1647424990.983839)

slack.divid_member(result)

