# RNG-SAST-001: SSTI — render_template_string on user input.
from flask import Blueprint, request, render_template_string

bp = Blueprint("templates", __name__)


@bp.get("/preview")
def preview():
    raw = request.args.get("body", "")
    return render_template_string(raw)
