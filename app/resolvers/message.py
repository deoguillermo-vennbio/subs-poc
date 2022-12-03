from datetime import datetime
import json
import ariadne
from app.utils.broadcaster import broadcast

subscription = ariadne.SubscriptionType()
mutation = ariadne.MutationType()
broadcast_channel = 'ch-message'

@mutation.field('pushMessage')
async def push_message(*_, message):
    msg = {'text': message['text'], 'created': str(datetime.utcnow())}
    #
    # Normally, we have mutation specific logic here
    # For example, we can save the message to database
    # But for this example, we will just broadcast the message
    #
    await broadcast.publish(
        broadcast_channel,
        json.dumps(msg)
    ) 

    return msg

@subscription.source('messagePushed')
async def message_pushed(*_):
    async with broadcast.subscribe(broadcast_channel) as subscriber:
        async for event in subscriber:
            yield json.loads(event.message)

@subscription.field('messagePushed')
async def resolve_message_pushed(message, info):
    return message 
