from celery import Celery


def create_celery():
    app = Celery('equation')

    app.config_from_object('equation.config')
    app.autodiscover_tasks(['equation.tasks'])
    return app


app = create_celery()
