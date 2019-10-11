from slack import RTMClient
from dsl import Program
import leds
import os

running_program = None


def stop_running_program():
    global running_program
    if running_program:
        running_program.stop()


def run_program(raw_program):
    global running_program
    stop_running_program()
    running_program = Program(raw_program)
    running_program.start()


@RTMClient.run_on(event='message')
def handle_event(**payload):
    data = payload['data']
    if 'subtype' not in data or data['subtype'] != 'bot_message':
        web_client = payload['web_client']

        if data.get('files'):
            file_id = data.get('files')[0]['id']
            file_content = web_client.files_info(file=file_id).data['content']

            run_program(file_content)

        elif data.get('text'):
            msg = data.get('text').strip().lower()
            if msg == 'on':
                leds.turn_on()

            elif msg == 'off':
                stop_running_program()
                leds.turn_off()

            elif msg.startswith('color'):
                colors = msg.split()[1:]
                stop_running_program()
                leds.set_color([int(c) for c in colors])

            elif msg.startswith('random-color'):
                stop_running_program()
                leds.set_random_color()

            elif msg.startswith('party-hard'):
                leds.set_random_color_two()

        channel_id = data.get('channel')
        event_timestamp = data['ts']

        web_client.reactions_add(
            channel=channel_id,
            name="heavy_check_mark",
            timestamp=event_timestamp
        )


if __name__ == '__main__':
    slack_token = os.environ["SLACK_API_TOKEN"]
    bot = RTMClient(token=slack_token)
    bot.start()
