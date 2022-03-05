class Team:
    def __init__(self, teamNum: int, startingPos: str, autoBalls: int, detectColor: bool, floorBalls: bool, droppedBalls: bool, highBalls: int, lowBalls: int, ringsClimbed: int):
        self.teamNum = teamNum
        self.startingPos = startingPos
        self.autoBalls = autoBalls
        self.detectColor = detectColor
        self.floorBalls = floorBalls
        self.droppedBalls = droppedBalls
        self.highBalls = highBalls
        self.lowBalls = lowBalls
        self.ringsClimbed = ringsClimbed

        