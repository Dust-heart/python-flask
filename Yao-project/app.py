from flask import Flask, url_for, request
from flask_restful import Api

from webapp.basic.add_res import ResourceAdd
from webapp.basic.blue_print import blue_print

app = Flask(__name__)

# 通过register_blueprint的方式新增路由
app.register_blueprint(blue_print)

# 通过flask_restful的方式添加路由
api = Api(app)
# 多个URL均可访问
api.add_resource(ResourceAdd, "/resource-add", "/resource_add", endpoint="test")

with app.test_request_context():
    # url_for:以视图函数名作为参数，返回对应的url，如果不定义endpoint，则是视图类的小写(resourceadd)
    print(url_for("test"))


if __name__ == '__main__':
    app.debug = True
    # app.run(debug=True)
    app.run()
