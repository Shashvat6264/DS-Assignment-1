# Distributed Systems Assignment 1
Implementing a distributed Queue

## Problem Statement
Steps of the problem statement
- Implementing a logging distributed queue 
- Adding persistence to the system
- Developing library for client producers and consumers

## Languages and Libraries
The whole software is written in **Python** programming language. **FastAPI** framework is used to implement HTTP APIs of the logging distributed queue. **SQLAlchemy** is used for ORM of database to support persistence in the system. Currently the system uses an **Sqlite3** database but can be easily connected to **PostgreSQL** database. 

## How to run
### Running from source
1. Clone this repository
```
git clone https://github.com/Shashvat6264/DS-Assignment-1.git
```

2. Change directory to the repository
```
cd DS-Assignment-1
```

3. Install all dependencies
```
pip install -r requirements.txt
```

4. Start the logging service queue
```
chmod +x start.sh
./start.sh
```

5. Run your own programs or visit [localhost:8000/docs](localhost:8000/docs) to view the API provided

### Running from docker image
1. Pull the docker image for logging queue from dockerhub
```
docker pull shashvat6264/logging-queue:latest
```

2. Run the docker image pulled from dockerhub
```
docker run -d --name logging-queue -p 8000:8000 shashvat6264/logging-queue
```

3. Run your own programs or visit [localhost:8000/docs](localhost:8000/docs) to view the API provided

## Using the client library
The client library is named as **myqueue**. The library can be imported in python programs and used directly as long as the logging-queue service is running. Detailed documentation for the library is provided in documentation file.

