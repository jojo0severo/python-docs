import requests


def example_get():
    r = requests.get("https://www.google.com")
    print(r.status_code)
    print(r.headers["content-type"])
    print(r.encoding)
    print(r.text)


def example_session():
    s = requests.Session()
    s.get("https://www.google.com")
    print(s.cookies)


def example_post():
    r = requests.post("https://httpbin.org/post")
    print(r.text)

    data = r.json()
    print(data)
    print(data["form"])


example_get()
example_post()
example_session()
