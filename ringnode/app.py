# RNG-SAST-002: debug=True, host=0.0.0.0.
# RNG-SAST-010: WTF_CSRF_ENABLED=False.
from flask import Flask
from .config import SECRET_KEY
from .views import portal, files, api

app = Flask(__name__)
app.config["SECRET_KEY"]         = SECRET_KEY
app.config["WTF_CSRF_ENABLED"]   = False

app.register_blueprint(portal.bp)
app.register_blueprint(files.bp)
app.register_blueprint(api.bp)


@app.get("/healthz")
def healthz():
    return {"ok": True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
