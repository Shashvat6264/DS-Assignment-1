import sys

sys.path.append('../../../')

from myqueue.producer import *
from myqueue.exceptions import *

# Configuration of broker

host = '127.0.0.1'
port = '8000'
endpoint = 'http://' + host + ":" + port


# Unit testing of non-exception behaviour of producer class

try:
    producer = Producer(['topic1', 'topic2'], endpoint)
    print('Test Case 1 passed')
except Exception as e:
    print('Test Case 1 failed')
    
try:
    producer.register('topic3')
    print('Test Case 2 passed')
except Exception as e:
    print('Test Case 2 failed')

try:
    producer.register(['topic4', 'topic5'])
    print('Test Case 3 passed')
except:
    print('Test Case 3 failed')
    
try:
    producer.enqueue('topic1', 'Some message')
    print('Test Case 4 passed')
except:
    print('Test Case 4 failed')
    
try:
    producer.enqueue(['topic2', 'topic3'], 'Some message')
    print('Test Case 5 passed')
except:
    print('Test Case 5 failed')
    
# Unit testing of exception behaviour of producer class

try:
    producer.register('topic1')
    print('Test Case 6 failed')
except AlreadyRegistered as e:
    print('Test Case 6 passed')
except:
    print('Test Case 6 failed')
    
try:
    producer.enqueue('topic6', 'Some topic')
    print('Test Case 7 failed')
except UnauthorizedException:
    print('Test Case 7 passed')
except Exception as e:
    print('Test Case 7 failed')

    


