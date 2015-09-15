from flask import (
    Flask,
    request
)
from flask.ext.pushrod import Pushrod, pushrod_view

app = Flask(__name__)
Pushrod(app)

@app.route('/')
@pushrod_view(jinja_template='index.html')
def hello():
    url = request.args.get('url')
    if not url:
        return {}
    else:
        return {
            'url': url
        }

if __name__ == '__main__':
    app.run(debug=True)
