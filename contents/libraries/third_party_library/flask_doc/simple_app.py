from flask import Flask, 

app = Flask("my app")


@app.get("/")
def get_app() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    app.run()
