from celery import shared_task, group


@shared_task
def asum(*args):
    l = []
    for a in args:
        if isinstance(a, int):
            l.append(a)
        elif isinstance(a, list):
            l.extend(a)
    print(l)
    total = l.pop()
    while len(l) > 0:
        total += l.pop()
    print(total)
    return total


@shared_task
def amul(*args):
    l = []
    for a in args:
        assert a is not None
        if isinstance(a, int):
            l.append(a)
        elif isinstance(a, list):
            l.extend(a)

    total = l.pop()
    while len(l) > 0:
        total *= l.pop()
    return total


@shared_task(bind=True)
def grouped(self, val):
    task = (group(asum.s(val, n) for n in range(val)) |
            asum.s(val))
    raise self.replace(task)


@shared_task(bind=True)
def flow(self, val):
    workflow = (asum.s(1, val) |
                asum.s(2) |
                grouped.s() |
                amul.s(3))

    return self.replace(workflow)
