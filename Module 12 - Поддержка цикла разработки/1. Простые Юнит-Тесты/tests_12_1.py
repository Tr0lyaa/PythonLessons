import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = runner.Runner("Test")
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = runner.Runner("Test")
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner1 = runner.Runner("Test1")
        test_runner2 = runner.Runner("Test2")
        for _ in range(10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)
