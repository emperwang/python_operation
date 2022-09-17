# -*- encoding:UTF-8 -*-
from flask import Flask, request
from demo1.goods import goods_pd
from demo1.convert.mobile import Mobile

# 在参数中设置静态文件 以及 template路径
app = Flask(__name__, static_folder="static", template_folder="templates")
app.register_blueprint(goods_pd)



# 跟目录, 并设置访问method
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "Hello world flask!"


# 接收参数
@app.route("/orders/<orderId>", methods=['GET'])
def recv_param(orderId):
    print("receive value: ", orderId)
    return "receive parameter success: "+orderId


# int: 是自带的 转换器，可以尝试自定义转换器
@app.route("/ids/<int:id>", methods=['GET'])
def convert(id):
    print("receive value:{}, tyep: {} ".format(id, type(id)))
    return "receive parameter success: {}".format(id)


# 注册自定义转换器
app.url_map.converters['mobile'] = Mobile


@app.route("/num/<mobile:pnum>", methods=['GET'])
def custom_convert(pnum):
    print("receive mobile value:{}, tyep: {} ".format(pnum, type(id)))
    return "receive mobile parameter success: {}".format(pnum)


# 获取请求参数
@app.route('/arg', methods=['GET'])
def get_query_string():
    name = request.args.get("name")
    return "get request name: {}".format(name)


# set response 1
@app.route('/res1', methods=['GET'])
def gen_res1():
    # 响应体, 响应码, cookie设置
    return "response body", 666, {"name": "zhangsan"}


# set response 2
@app.route('/res2')
def gen_res2():
    res = app.make_response("response body2")
    res.set_cookie("name", "zhangsan")
    res.status_code = 403
    return res


# 异常处理
# @app.errorhandler(500)
@app.errorhandler(403)
def error_500(e):
    print(e)
    return "server run away"


@app.route('/err')
def gen_err():
    1 / 0
    return "error"


@app.errorhandler(ZeroDivisionError)
def error_exception(e):
    print(e)
    return "除数不可为0"

# 钩子函数
@app.before_first_request
def before_first():
    print("before first")


@app.before_request
def before_req():
    print("before request")


@app.after_request
def after_req(respoonse):
    print("after request")
    return respoonse

@app.teardown_request
def tear_down(response):
    print("teardown request")
    return response


# if __name__=='__main__':
#     app.run()
