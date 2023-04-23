from datetime import timedelta, timezone, time, date, datetime


def timedelta_example():
    """
    Usado para calcular a diferença entre datas ou horas.
    """
    print("timedelta_example")
    print("timedelta(days=1, seconds=1, microseconds=1, milliseconds=1, minutes=1, hours=1, weeks=1)")
    print(timedelta(days=1, seconds=1, microseconds=1, milliseconds=1, minutes=1, hours=1, weeks=1))
    print()

def timezone_example():
    """
    Usado para definir o timezone.
    """
    print("timezone_example")
    print("timezone(timedelta(hours=1))")
    print(timezone(timedelta(hours=1)))
    print()


def time_example():
    """
    Usado para definir o tempo independente do dia
    """
    print("time_example")
    print("time(1, 1, 1, 1, timezone(timedelta(hours=1)))")
    print(time(1, 1, 1, 1, timezone(timedelta(hours=1))))
    print()

def date_example():
    """
    Usado para definir a data independente do tempo.
    """
    print("date_example")
    print("date(1, 1, 1)")
    print(date(1, 1, 1))
    print()

def datetime_example():
    """
    Usado para definir a data e o tempo.
    """
    print("datetime_example")
    print("datetime(1, 1, 1, 1, 1, 1, 1, timezone(timedelta(hours=1)))")
    print(datetime(1, 1, 1, 1, 1, 1, 1, timezone(timedelta(hours=1))))
    print()

timedelta_example()
timezone_example()
time_example()
date_example()
datetime_example()
