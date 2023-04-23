from flask import Blueprint, session

bp = Blueprint("base_blueprint", __name__, url_prefix="/bp")


@bp.get("/")
def get_bp():
    already_accessed = session.get("already_accessed")
    if already_accessed:
        return "You already accessed this route"

    session["already_accessed"] = True
    return "New access"
