import os
import broadcaster

REDIS_URL = os.getenv('REDIS_URL')
broadcast = broadcaster.Broadcast(REDIS_URL)
