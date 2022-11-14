from flask import Flask
from core import handle_message

app = Flask(__name__)


@app.route('/seila')
def index():
  return 'Sup dude'

if __name__ == "__main__":  # Makes sure this is the main process
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)


