from flask import Flask,render_template

import settings

app = Flask(__name__,static_url_path='/s')


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')





app.config.from_object(settings.Dev)

