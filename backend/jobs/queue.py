from rq import Queue
from core.redis_conn import get_redis

redis_conn = get_redis()
queue = Queue("default", connection=redis_conn)
