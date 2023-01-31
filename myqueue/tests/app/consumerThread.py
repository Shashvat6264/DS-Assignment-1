import threading 

import sys

sys.path.append('../../../')

from myqueue.consumer import *

class ConsumerThread(threading.Thread):
    def __init__(self, id, topics, *args):
        super().__init__(*args)
        self.id = id
        self.topics = topics
        self.consumer = Consumer(topics, 'http://localhost:8000')
        
        
    def run(self):
        while(1):
            for topic in self.topics:
                try:
                    if self.consumer.can_dequeue(topic):
                        message = self.consumer.dequeue(topic)
                        print()
                        print("Consumer " + str(self.id))
                        print("\tTopic: " + topic)
                        print("\tMessage: " + message)
                except Exception as e:
                    print(e)