class Rectangle :
    def __init__(self, x1=0, y1=0, x2=0, y2=0)  :
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def show(self) :
        print(f'좌측 상단 꼭지점이({self.__x1}, {self.__y1})이고 우측 하단 꼭지점이 ({self.__x2}, {self.__y2})인 사각형입니다.')
    
    def getWidth(self) :
        W = self.__x2 - self.__x1
        return W
    
    def getHeight(self) :
        H = self.__y2 - self.__y1
        return H
    
    def getArea(self) :
        A = W * H
        return A
    
    def getPerimeter(self, Rectangle) :
        P = 2*W + 2*H
        return P

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')