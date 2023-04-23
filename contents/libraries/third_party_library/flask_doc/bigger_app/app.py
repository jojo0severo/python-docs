from flask import Flask

from .route import bp

app = Flask("my bigger app")
app.secret_key = "super secret key"
app.register_blueprint(bp)


@app.get("/")
def get_base():
    return {"status": "ok"}, 203
