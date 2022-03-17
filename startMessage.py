import dedenziBot
import properties

slack = dedenziBot.SlackAPI()

ts = slack.post_init_message(properties.CHANNEL_NAME)
print(ts)