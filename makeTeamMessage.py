import dedenziBot
import properties
import divide
import sys

slack = dedenziBot.SlackAPI()

channel_id = slack.get_channel_id(properties.CHANNEL_NAME)
# 만약에 숫자 없으면 예외처리
print(sys.argv[1])
# result = slack.get_reactions(channel_id, sys.argv[1])
result = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

divid_members = divide.divid_member(result)
slack.post_message(properties.CHANNEL_NAME, divid_members)