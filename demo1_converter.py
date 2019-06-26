from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['mobile'] = MobileConverter

@app.route('/<mobile:mob_num>')
def send_sms_code(mob_num):
    return 'send sms code to {}'.format(mob_num)


@app.route('/users/<any(white,blue,black):user_id>')
def index(user_id):
    return 'hello {}'.format(user_id)


if __name__ == '__main__':
    app.run()
