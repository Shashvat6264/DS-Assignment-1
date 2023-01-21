import uvicorn
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
    else:
        uvicorn.run("server.app:app", host="0.0.0.0", port=int(sys.argv[1]), reload=True)