import os
from app import app


if __name__ == "__main__":
    app.run(
        host = os.getenv('IP', 'localhost'), 
        port = int(os.getenv('PORT', 8000))
        )

    