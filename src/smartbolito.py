from slack import RTMClient
import leds
import os


@RTMClient.run_on(event='message')
def handle_event(**payload):
    data = payload['data']
    if 'subtype' not in data or data['subtype'] != 'bot_message':
        web_client = payload['web_client']

        if data.get('files'):
            file_id = data.get('files')[0]['id']
            file_content = web_client.files_info(file=file_id).data['content']

            return #TODO implement file interpretation

        elif data.get('text'):
            msg = data.get('text').strip().lower()
            if msg == 'on':
                leds.turn_on()
            elif msg == 'off':
                leds.turn_off()
            elif msg.startswith('color'):
                colors = msg.split()[1:]
                leds.set_color([int(c) for c in colors])

        channel_id = data.get('channel')
        event_timestamp = data['ts']

        web_client.reactions_add(
            channel=channel_id,
            name="thumbsup",
            timestamp=event_timestamp
        )


if __name__ == '__main__':
    slack_token = os.environ["SLACK_API_TOKEN"]
    bot = RTMClient(token=slack_token)
    bot.start()
