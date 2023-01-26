from myqueue import Producer

myproducer = Producer(topics = ['test'], broker = 'http://0.0.0.0:8000')
