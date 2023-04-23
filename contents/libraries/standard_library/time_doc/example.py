import time


def example_now():
    print("\nNow:")
    print(time.time())
    print()


def example_sleep():
    print("\nSleep:")
    print(time.time())
    time.sleep(2)
    print(time.time())
    print()


def example_strftime():
    print("\nStrftime:")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print()


def example_strptime():
    print("\nStrptime:")
    print(time.strptime("2016-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"))
    print()


def example_time():
    print("\nTime:")
    print(time.time())
    print(time.localtime())
    print(time.gmtime())
    print()

def example_tzset():
    print("\nTzset:")
    print(time.tzname)
    print(time.timezone)
    print(time.daylight)
    print()


example_now()
example_sleep()
example_strftime()
example_strptime()
example_time()
example_tzset()