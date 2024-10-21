import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test_runner = rt.Runner("Test")
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        test_runner = rt.Runner("Test")
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test_runner1 = rt.Runner("Test1")
        test_runner2 = rt.Runner("Test2")
        for _ in range(10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = rt.Runner("Усэйн", 10)
        self.runner2 = rt.Runner("Андрей", 9)
        self.runner3 = rt.Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testTournament1(self):
        tournament = rt.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        for key in result.keys():
            result[key] = str(result[key])
        self.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testTournament2(self):
        tournament = rt.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        for key in result.keys():
            result[key] = str(result[key])
        self.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testTournament3(self):
        tournament = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        for key in result.keys():
            result[key] = str(result[key])
        self.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)
