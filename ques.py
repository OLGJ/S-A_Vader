###This file runs server requests

#Create RQ que
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

from data import run_datacollection
result = q.enqueue(run_datacollection)

job = queue.enqueue_in(timedelta(hours=24), run_datacollection())

print('result:', result)