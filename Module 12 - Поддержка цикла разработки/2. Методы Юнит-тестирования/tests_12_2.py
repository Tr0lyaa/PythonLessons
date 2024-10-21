import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = rt.Runner("Усэйн", 10)
        self.runner2 = rt.Runner("Андрей", 9)
        self.runner3 = rt.Runner("Ник", 3)

    def testTournament1(self):
        tournament = rt.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        for key in result.keys():
            result[key] = str(result[key])
        self.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def testTournament2(self):
        tournament = rt.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        for key in result.keys():
            result[key] = str(result[key])
        self.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

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
