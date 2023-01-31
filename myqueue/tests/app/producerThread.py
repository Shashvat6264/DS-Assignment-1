import threading
import time
import random

import sys

sys.path.append('../../../')

from myqueue.producer import *

class ProducerThread(threading.Thread):
    def __init__(self, id, filename, topics, *args):
        super().__init__(*args)
        self.id = id
        self.filename = filename
        self.file = open(filename, "r")
        self.producer = Producer(topics, 'http://localhost:8000')
        
    def run(self):
        for line in self.file:    
            time.sleep(random.random())
            try:    
                words = line.split()
                self.producer.enqueue(words[3], words[1])
                print()
                print("Producer " + str(self.id))
                print("\tTopic: " + words[3])
                print("\tMessage: " + words[1])
            except Exception as e:
                print(e)
    
