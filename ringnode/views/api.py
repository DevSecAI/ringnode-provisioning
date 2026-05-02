# RNG-SAST-009: any error returns repr(e) to client.
from flask import Blueprint, request, jsonify

bp = Blueprint("api", __name__)


@bp.post("/api/provision")
def provision():
    try:
        msisdn = request.json["msisdn"]
        # ... business logic ...
        return jsonify({"ok": True, "msisdn": msisdn})
    except Exception as e:
        return jsonify({"error": repr(e), "request": dict(request.json or {})}), 500
