import os
from app import create_app

# setup environment variables
import config_env

app = create_app(os.environ['APP_SETTINGS'])

if __name__ == "__main__":
    app.run( host = os.getenv('IP', 'localhost'), 
             #port = int(os.getenv('PORT', 8000)) 
            )