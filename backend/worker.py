from rq import Worker, Queue
from core.redis_conn import get_redis

def main():
    redis_conn = get_redis()

    q = Queue("default", connection=redis_conn)

    worker = Worker([q], connection=redis_conn)
    worker.work()

if __name__ == "__main__":
    main()
