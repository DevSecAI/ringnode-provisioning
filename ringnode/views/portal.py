# RNG-SAST-004: Markup wrapping user content (XSS).
from flask import Blueprint, request
from markupsafe import Markup

bp = Blueprint("portal", __name__)


@bp.get("/portal")
def portal():
    note = request.args.get("note", "")
    return f"<html><body>{Markup(note)}</body></html>"
