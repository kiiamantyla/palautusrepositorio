import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return[
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_search_finds_existing_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.points, 124)
        
    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        names = [p.name for p in team_players]
        self.assertEqual(len(team_players), 3)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)
        self.assertIn("Semenko", names)

    def test_team_returns_empty_list_if_team_not_found(self):
        team_players = self.stats.team("XYZ")
        self.assertEqual(team_players, [])

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 2)

    def test_top_returns_players_sorted_by_points(self):
        top_players = self.stats.top(3)
        points = [p.points for p in top_players]
        self.assertEqual(points, sorted(points, reverse=True))

    def test_top_returns_correct_top_player(self):
        top_player = self.stats.top(1)[0]
        self.assertEqual(top_player.name, "Gretzky")
        self.assertEqual(top_player.points, 124)

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Unknown Player")
        self.assertIsNone(player)
        
    def test_top_sorted_by_points_default(self):
        top = self.stats.top(3)
        points = [p.points for p in top]
        self.assertEqual(points, sorted(points, reverse=True))

    def test_top_sorted_by_points_explicit(self):
        top = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")

    def test_top_sorted_by_goals(self):
        top = self.stats.top(3, SortBy.GOALS)
        goals = [p.goals for p in top]
        self.assertEqual(goals, sorted(goals, reverse=True))
        self.assertEqual(top[0].name, "Lemieux")

    def test_top_sorted_by_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)
        assists = [p.assists for p in top]
        self.assertEqual(assists, sorted(assists, reverse=True))
        self.assertEqual(top[0].name, "Gretzky")