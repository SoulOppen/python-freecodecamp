class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return 2 * (self.height + self.width)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.height<=50 and self.width<=50:
            string=""
            for i in range (self.height):
                string += "*"*self.width+"\n"
            return string
        return "Too big for picture."
    def get_amount_inside(self,shape):
        times_width=self.width//shape.width
        times_height=self.height//shape.height
        return times_width*times_height;
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
class Square(Rectangle):
    def __init__(self, side):        
        super().__init__(side, side)
        self.side=side
    def set_side(self,side):
        self.side=side
        super().set_height(side)
        super().set_width(side)
    def set_height(self, height):
        self.side=height
        super().set_height(height)
        super().set_width(height)
    def set_width(self, width):
        self.side=width
        super().set_height(width)
        super().set_width(width)
    def __str__(self):
        return f'Square(side={self.side})'