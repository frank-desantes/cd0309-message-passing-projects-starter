import os
import sys
from app import create_app

# open log file
logfile = open('flask-grpc-server.log', 'a')

# Redirect stdout and stderr
sys.stdout = logfile
sys.stderr = logfile 

app = create_app(os.getenv("FLASK_ENV") or "test")

if __name__ == "__main__":
    app.run(debug=True)
    
