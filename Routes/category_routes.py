from flask import request, Response, Blueprint

import controllers

categories = Blueprint('categories', __name__)


@categories.route("/category", methods=["GET"])
def category_get_all() -> Response:
    return controllers.wish_list_get_all(request)

@categories.route("/categories", methods=["POST"])
def category_add() -> Response:
    return controllers.wish_list_add(request)

@categories.route("/category/<category_id>", methods=["GET"])
def category_get_by_id(category_id) -> Response:
    return controllers.wish_list_update(request, category_id)

@categories.route("/category/<category_id>", methods=["PUT"])
def category_update_by_id(category_id) -> Response:
    return controllers.wish_list_update(request, category_id)

@categories.route("/category/delete/<category_id>", methods=["DELETE"])
def wish_list_delete(category_id) -> Response:
    return controllers.wish_list_delete(request, category_id)