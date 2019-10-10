from slack import RTMClient
import leds
import os


@RTMClient.run_on(event='message')
def handle_event(**payload):
    data = payload['data']
    web_client = payload['web_client']

    if data.get('files'):
        file_id = data.get('files')[0]['id']
        file_content = web_client.files_info(file=file_id).data['content']

    elif data.get('text'):
        msg = data.get('text').strip().lower()
        if msg == 'on':
            pass
        elif msg == 'off':
            leds.turn_off()

    channel_id = data.get('channel')

    web_client.chat_postMessage(
        channel=channel_id,
        text=f"I am not implemented yet"
    )


if __name__ == '__main__':
    slack_token = os.environ["SLACK_API_TOKEN"]
    bot = RTMClient(token=slack_token)
    bot.start()
