class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')
    
def most_goals(ballplayers: list):
    ballplayer = max(ballplayers, key=lambda bp: bp.goals)
    return ballplayer.name

def most_points(ballplayers: list):
    ballplayer = max(ballplayers, key=lambda bp: bp.goals + bp.passes)
    return (ballplayer.name, ballplayer.number)

# Write your solution here