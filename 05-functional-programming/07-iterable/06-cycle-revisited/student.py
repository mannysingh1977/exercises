def cycle(values):
    values = list(values)
    while True:
        for value in values:
            yield value


def alternative_cycle(values):
    values = list(values)
    while True:
        yield from values
