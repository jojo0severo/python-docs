import uvicorn


def main():
    uvicorn.run("big_app:create_app", factory=True)


if __name__ == "__main__":
    main()
