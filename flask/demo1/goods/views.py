from . import goods_pd


@goods_pd.route("/idx", methods=['GET'])
def goods_index():
    return "goods index"
