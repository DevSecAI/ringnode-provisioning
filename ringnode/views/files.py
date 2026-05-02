# RNG-SAST-005: send_from_directory with un-normalised filename.
from flask import Blueprint, send_from_directory

bp = Blueprint("files", __name__)
ROOT = "/var/ringnode/files"


@bp.get("/files/<path:name>")
def get(name):
    return send_from_directory(ROOT, name)
