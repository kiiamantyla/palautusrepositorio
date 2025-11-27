class TennisGame:

    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_points += 1
        else:
            self.p2_points += 1

    def get_score(self):
        if self.is_tied():
            return self.tied_score()
        
        if self.is_endgame():
            return self.advantage_or_win_score()
        
        return self.regular_score()

    def is_tied(self):
        return self.p1_points == self.p2_points

    def tied_score(self):
        if self.p1_points < 3:
            return f"{self.SCORE_NAMES[self.p1_points]}-All"
        return "Deuce"

    def is_endgame(self):
        return self.p1_points >= 4 or self.p2_points >= 4

    def advantage_or_win_score(self):
        diff = self.p1_points - self.p2_points
        if diff == 1:
            return "Advantage player1"
        if diff == -1:
            return "Advantage player2"
        if diff >= 2:
            return "Win for player1"
        return "Win for player2"

    def regular_score(self):
        p1_name = self.SCORE_NAMES[self.p1_points]
        p2_name = self.SCORE_NAMES[self.p2_points]
        return f"{p1_name}-{p2_name}"
