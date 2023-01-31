import sys

sys.path.append('../../../')

from myqueue.consumer import *
from myqueue.exceptions import *

# Configuration of broker

host = '127.0.0.1'
port = '8000'
endpoint = 'http://' + host + ":" + port


# Unit testing of non-exception behaviour of consumer class

try:
    consumer = Consumer(['topic1', 'topic2'], endpoint)
    print('Test Case 1 passed')
except Exception as e:
    print(e)
    print('Test Case 1 failed')
    
try:
    consumer.register('topic3')
    print('Test Case 2 passed')
except:
    print('Test Case 2 failed')

try:
    consumer.register(['topic4', 'topic5'])
    print('Test Case 3 passed')
except:
    print('Test Case 3 failed')
    
try:
    consumer.dequeue('topic1')
    print('Test Case 4 passed')
except Exception as e:
    print(e)
    print('Test Case 4 failed')
    
try:
    consumer.dequeue(['topic2', 'topic3'])
    print('Test Case 5 passed')
except:
    print('Test Case 5 failed')

try:
    size = consumer.get_size('topic1')
    if size == 0:
        print('Test Case 6 passed')
    else:
        print('Test Case 6 failed')
except:
    print('Test Case 6 failed')
    
# Unit testing of exception behaviour of consumer class

try:
    consumer.register('topic1')
    print('Test Case 7 failed')
except AlreadyRegistered:
    print('Test Case 7 passed')
except:
    print('Test Case 7 failed')
    
try:
    consumer.register('topic6')
    print('Test Case 8 failed')
except TopicDoesNotExist:
    print('Test Case 8 passed')
except:
    print('Test Case 8 failed')
    
try:
    consumer.dequeue('topic6')
    print('Test Case 9 failed')
except UnauthorizedException:
    print('Test Case 9 passed')
except:
    print('Test Case 9 failed')
    

    


