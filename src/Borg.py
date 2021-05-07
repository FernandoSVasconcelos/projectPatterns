class Borg:
    __shared_state = {}
 
    @property
    def x(self):
        return self.__x
 
    @x.setter
    def x(self, value):
        self.__x = value
 
    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == "__main__":
    b1 = Borg()
    b2 = Borg()
    b1.x = 20
    print('Borg')
    print('b1.x={} | b2.x={}'.format(b1.x, b2.x))
    print('id(b1)={} | id(b2)={}'.format(id(b1), id(b2)))