import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner('Jhon')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner('Kate')
        for j in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_chalange(self):
        walker = Runner('Jhon')
        runner = Runner('Kate')
        for i in range(10):
            walker.walk()
        for j in range(10):
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance, 'test is failed')