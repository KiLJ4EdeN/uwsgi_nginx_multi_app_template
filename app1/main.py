"""
APP1
"""
from flask import Flask


app = Flask('app1')


@app.route('/hello_world1')
def hello_world1():
    """
    Flask endpoint
    :return: TXT
    """
    return "Hello World From App 1!"


if __name__ == '__main__':
    app.run()

