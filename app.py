from slacker import Slacker
from setting import token
import asyncio
import websockets

print(token)
slack = Slacker(token)

response = slack.rtm.start()
endpoint = response.body['url']


async def main():
    ws = await websockets.connect(endpoint)
    while True:
        message_json = await ws.recv()
        print(message_json)
        # slack.chat.post_message('#random', 'wow')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
