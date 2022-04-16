import dedenziBot
import properties

slack = dedenziBot.SlackAPI()

try:
    ts = slack.post_init_message(properties.CHANNEL_NAME)
    print(ts)
except:
    print("없는 채널이에요! 채널 이름을 다시 설정하세요!")