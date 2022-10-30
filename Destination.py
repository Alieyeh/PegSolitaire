from Location import Location


class Destination (Location):

    def __init__(self, x: int, y: int):
        super().__init__(x, y)

# self is destination, loc is the current location.

    def is_left(self, loc: Location):
        if self.y == loc.y and self.x + 2 == loc.x:
            return True
        else:
            return False

    def is_right(self, loc: Location):
        if self.y == loc.y and self.x - 2 == loc.x:
            return True
        else:
            return False

    def is_up(self, loc: Location):
        if self.x == loc.x and self.y + 2 == loc.y:
            return True
        else:
            return False

    def is_down(self, loc: Location):
        if self.x == loc.x and self.y - 2 == loc.y:
            return True
        else:
            return False
