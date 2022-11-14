from flask import Flask
from core import handle_message

app = Flask(__name__)


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        # Randomly select the port the machine hosts on.
        port=5000
    )
    print('Running on port 5000')


@app.route('/')
def index():
    return 'Sup dude'
