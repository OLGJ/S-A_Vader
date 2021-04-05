###This file runs server requests

#Create RQ que
from redis import Redis
from rq import Queue
from datetime import timedelta

q = Queue(connection=Redis())

#from data import run_datacollection
from wsb_data_appender import run_data_adder

discussion_result = q.enqueue(run_data_adder)

discussion_job = q.enqueue_in(timedelta(seconds=600), run_data_adder())



#result = q.enqueue(run_datacollection)

#job = queue.enqueue_in(timedelta(hours=24), run_datacollection())

print('Job done:', discussion_result)