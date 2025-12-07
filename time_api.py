from flask import Flask
# create flask instance
app = Flask(__name__)


# create route,each route has different end point

@app.route('/time')

def get_current_time():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


if __name__ == '__main__':
    app.run()