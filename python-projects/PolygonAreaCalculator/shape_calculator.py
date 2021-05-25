class Rectangle:
    """[Base class: Rectangle]
    """

    def __init__(self, width=0, height=0):
        """[assign initial values]

        Args:
            height (int, optional): [height of Rectangle]. Defaults to 0.
            width (int, optional): [width of Rectangle]. Defaults to 0.
        """
        self.height = height
        self.width = width

    def __str__(self):
        """[String representation of the shape]

        Returns:
            [string]: [string representation]
        """
        rectangle_str = f"Rectangle(width={self.width}, height={self.height})"
        return rectangle_str

    def get_area(self):
        """[return area of shape]

        Returns:
            [float]: [calculated area of shape]
        """
        return self.height * self.width

    def set_width(self, width=0):
        """[sets width of the shape]

        Args:
            width (float, optional): [user input width of the shape]. Defaults to 0.
        """
        self.width = width

    def set_height(self, height=0):
        """[sets height of shape]

        Args:
            height (float, optional): [user iput height of shape]. Defaults to 0.
        """
        self.height = height

    def get_perimeter(self):
        """[calculate Perimeter of shape]

        Returns:
            [float]: [perimeter of shape]
        """
        return 2*(self.width+self.height)

    def get_diagonal(self):
        """[calculate diagonal of shape]

        Returns:
            [float]: [calculate diagonal of the shape]
        """
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        """[graphical representation of the shape]

        Returns:
            [string]: [returns graphical represenattion of the shape]
        """
        if (self.height > 50 or self.width > 50):
            return "Too big for picture."

        shapeStr = ""
        for l in range(self.height):
            shapeStr += "*"*self.width
            shapeStr += "\n"

        return shapeStr

    def get_amount_inside(self, shape):
        """[how many shapes can fit into given shape ?]

        Args:
            shape ([type]): [shape to fit]

        Returns:
            [integer]: [calculates how many shapes can be fit into bigger shape]
        """
        times_fit = self.get_area()//shape.get_area()
        return (times_fit)


class Square(Rectangle):
    def __init__(self, side=0):
        """[class Square: derived from Rectangle]

        Args:
            side (int, optional): [side of square]. Defaults to 0.
        """
        self.side = side
        super().__init__(side, side)

    def set_side(self, side=9):
        """[sets side of square]

        Args:
            side (int, optional): [sets user inputted side]. Defaults to 9.
        """
        self.side = side
        super().set_height(side)
        super().set_width(side)

    def set_width(self, width=0):
        """[sets width of Rectangle(Base class)]

        Args:
            width (int, optional): [sets square side as width of Base class: Rectangle]. Defaults to 0.
        """
        self.set_side(width)

    def set_height(self, height):
        """[sets height of Rectangle(Base class)]

        Args:
            height ([type]): [sets square side as height of Base class: Rectangle]
        """
        self.side = height

    def __str__(self):
        """[string representation]

        Returns:
            [string]: [returns string representation of square]
        """
        square_str = f"Square(side={self.side})"
        return square_str
