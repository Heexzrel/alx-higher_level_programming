#!/usr/bin/python3
""" Square module """


class Square:
    """ Square class 
        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            postion(tuple): postion of square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Find the  square area
        Return:
            the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            value (int): size of a side of the square
        Error to be raise:
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print the square
        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of position
        Args:
            value (tuple): position of the square
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
