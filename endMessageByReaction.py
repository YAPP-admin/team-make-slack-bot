import dedenziBot
import properties
import divide
import sys

slack = dedenziBot.SlackAPI()

try:
    channel_id = slack.get_channel_id(properties.CHANNEL_NAME)
    result = slack.get_reactions(channel_id, sys.argv[1])

    divid_members = divide.divid_member(result)

    members_message_form = divide.member_lists_to_message_lists(divid_members)
    slack.post_message(properties.CHANNEL_NAME, members_message_form)
    
    
except IndexError:
    print("해당하는 메시지가 존재하지 않아요! timestamp를 다시 확인해주세요!")

except KeyError:
    slack.post_error_message(channel_id, "등록된 이모지가 없는데요??? 확인 후 재시도 부탁드려요!")

except Exception as e:
    slack.post_error_message(channel_id, "참여자가 너무 적네요..! 저 바빠요.")

