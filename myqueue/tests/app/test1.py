import sys

sys.path.append('../')

from app.producerThread import *
from app.consumerThread import *

p1 = ProducerThread(1, './test_asgn1/producer_1.txt', ['T-1', 'T-2', 'T-3'])
p2 = ProducerThread(2, './test_asgn1/producer_2.txt', ['T-1', 'T-3'])
p3 = ProducerThread(3, './test_asgn1/producer_3.txt', ['T-1'])
p4 = ProducerThread(4, './test_asgn1/producer_4.txt', ['T-2'])
p5 = ProducerThread(5, './test_asgn1/producer_5.txt', ['T-2'])

c1 = ConsumerThread(1, ['T-1', 'T-2', 'T-3'])
c2 = ConsumerThread(2, ['T-1', 'T-3'])
c3 = ConsumerThread(3, ['T-1', 'T-3'])


p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

c1.start()
c2.start()
c3.start()
