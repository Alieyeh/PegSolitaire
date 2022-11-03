class Location:
    """
    Object for the location of peg.

    Params:
    ------

    x:
        X coordinate of location on board.

    y:
        Y coordinate of location on board.

    """

    def __init__(self, x: int, y: int):
        """
        Initialises location class. Gets coordinates of
        location and sets the x and y parameters of object.

        Params:
        ------

        x: int, mandatory
            X coordinate of the location of the chosen peg.

        y: int, mandatory
            Y coordinate of the location of the chosen peg.
        """
        self.x = x
        self.y = y
