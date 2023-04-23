import asyncio

from tortoise import Tortoise

from model import Tournament


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["model"]})
    # Generate the schema
    await Tortoise.generate_schemas()


async def using():
    # Create instance by save
    tournament = Tournament(name="New Tournament")
    await tournament.save()

    # Or by .create()
    await Tournament.create(name="Another Tournament")

    # Now search for a record
    tour = await Tournament.filter(name__contains="Another").first()
    print(tour.name)


async def main():
    await init()
    await using()
    await Tortoise.close_connections()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
