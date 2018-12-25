class Screen(object):
    # def __init__(self,width,height):
    #     self.__width = width
    #     self.height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width*self.__height
s = Screen()
s.width = 70
s.height = 80
print('resolution =', s.resolution)
if s.resolution == 5600:
    print('测试通过!')
else:
    print('测试失败!')
