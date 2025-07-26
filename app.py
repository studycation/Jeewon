from flask import *

app = Flask(__name__)

# 홈화면
@app.route('/')
def defaultpage():
    return render_template("fieldset.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)