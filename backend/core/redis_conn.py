import os
import redis

def get_redis():
    url = os.getenv("REDIS_URL", "redis://redis:6379/0")
    return redis.Redis.from_url(url)
