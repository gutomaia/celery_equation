from unittest import TestCase

from celery import Celery
from equation.tasks import flow


class TaskTeat(TestCase):

    def setUp(self):
        self.celery = Celery()
        self.celery.always_eager = True
        self.celery.conf.task_always_eager = True

    def test_flow_1(self):
        res = flow.delay(1)
        self.assertIsNotNone(res)
        self.assertEqual(res.get(), 78)

    def test_flow_2(self):
        res = flow.delay(2)
        self.assertIsNotNone(res)
        self.assertEqual(res.get(), 120)

    def test_flow_100(self):
        res = flow.delay(100)
        self.assertIsNotNone(res)
        self.assertEqual(res.get(), 47895)
