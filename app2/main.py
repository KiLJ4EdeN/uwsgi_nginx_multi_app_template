"""
APP2
"""
from flask import Flask


app = Flask('app2')


@app.route('/hello_world2')
def hello_world1():
    """
    Flask endpoint
    :return: TXT
    """
    return "Hello World From App 2!"


if __name__ == '__main__':
    app.run()

