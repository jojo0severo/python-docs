from tortoise import Tortoise, run_async

TORTOISE_CONFIG = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models.tournament", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
    )
    # Generate the schema
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
