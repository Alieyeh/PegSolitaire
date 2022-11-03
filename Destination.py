from Location import Location


class Destination (Location):
    """
    Destination class is an extension of the location class
    that has additional functions and is used for the location
    of the destination of the peg.
    """

    def __init__(self, x: int, y: int):
        """
        Initialises the destination class by getting the
        x and y coordinates of the destination.

        Params:
        ------

        x: integer, mandatory
            X coordinate of the destination on board.

        y: integer, mandatory.
            Y coordinate of the destination on board.
        """
        super().__init__(x, y)

    def is_left(self, loc: Location):
        """
        Checks if the destination is two steps to the left
        of the current location.

        Params:
        ------

        loc: Location, mandatory
            The current location of the chosen peg.

        Returns:
        --------
        Boolean
        """
        if self.y == loc.y and self.x + 2 == loc.x:
            return True
        else:
            return False

    def is_right(self, loc: Location):
        """
        Checks if the destination is two steps to the right
        of the current location.

        Params:
        ------

        loc: Location, mandatory
            The current location of the chosen peg.

        Returns:
        --------
        Boolean
        """
        if self.y == loc.y and self.x - 2 == loc.x:
            return True
        else:
            return False

    def is_up(self, loc: Location):
        """
        Checks if the destination is two steps above the
        current location.

        Params:
        ------

        loc: Location, mandatory
            The current location of the chosen peg.

        Returns:
        --------
        Boolean
        """
        if self.x == loc.x and self.y + 2 == loc.y:
            return True
        else:
            return False

    def is_down(self, loc: Location):
        """
        Checks if the destination is two steps below the
        current location.

        Params:
        ------

        loc: Location, mandatory
            The current location of the chosen peg.

        Returns:
        --------
        Boolean
        """
        if self.x == loc.x and self.y - 2 == loc.y:
            return True
        else:
            return False
