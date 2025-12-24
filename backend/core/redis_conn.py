import os
import redis
import dotenv

dotenv.load_dotenv()

def get_redis():
    url = os.getenv("REDIS_URL")
    return redis.Redis.from_url(url)
