EMPTY_STRING = ""


class Rectangle:
    """[summary]
    """

    def __init__(self, width=0, height=0):
        """[summary]

        Args:
            height (int, optional): [description]. Defaults to 0.
            width (int, optional): [description]. Defaults to 0.
        """
        self.height = height
        self.width = width

    def __str__(self):
        rectangle_str = f"Rectangle(width={self.width}, height={self.height})"
        return rectangle_str

    def get_area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.height * self.width

    def set_width(self, width):
        """[summary]

        Args:
            width ([type]): [description]
        """
        self.width = width

    def set_height(self, height=0):
        """[summary]

        Args:
            height (int, optional): [description]. Defaults to 0.
        """
        self.height = height

    def get_perimeter(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return 2*(self.width+self.height)

    def get_diagonal(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return EMPTY_STRING

    def get_amount_inside(self, shape):
        """[summary]

        Args:
            shape ([type]): [description]

        Returns:
            [type]: [description]
        """
        return EMPTY_STRING


class Square(Rectangle):
    def __init__(self, side=0):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side=9):
        self.side = side
        super().set_height(side)
        super().set_width(side)

    def set_width(self, width=0):
        self.set_side(width)

    def set_height(self, height):
        self.side=height

    def __str__(self):
        square_str = f"Square(side={self.side})"
        return square_str
