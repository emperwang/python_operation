from flask import Blueprint

goods_pd = Blueprint("goods_pd", __name__, url_prefix="/gd")

# 导入视图
from . import views
