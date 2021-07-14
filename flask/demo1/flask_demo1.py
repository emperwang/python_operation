# -*- encoding:UTF-8 -*-

import flask

app = flask.Flask(__name__)


# 跟目录, 并设置访问method
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "Hello world flask!"


# 接收参数
@app.route("/orders/<orderId>", methods=['GET', 'POST'])
def recv_param(orderId):
    print("receive value: ", orderId)
    return "receive parameter success: "+orderId


if __name__=='__main__':
    app.run()
