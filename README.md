# Celery Equation


This is a testing project for debuging purpose on Celery.


This is a simple project to debug Celery eager behavior on
cases using group and chain in a dynamic task. I've notice
that the behavior of the eager mode does not match the
async behavior.

## For the Async Mode (Regular Celery)

You just need a local Redis running for testing, then
just:

```
make worker
```

It will create a local VirtualEnv at **venv** directory with the dependencies
and a worker instance running.

If you open a Python repr within the VirtualEnv **venv**, that's the expected
from the tasks:
```
>>> from equation.main import *
>>> from equation.tasks import *
>>> flow.delay(1).get()
78
>>> flow.delay(2).get()
120
>>> flow.delay(100).get()
47895
```

## For the Eager Mode

I'm running eager mode on tests just to show up the unexpected behavior:

You just need to run the tests with:

```
make test
```

What I've discovered so far, a chain followed by a group, does not receive the
arguments from the previous task.

