class Singleton:
		__instance = None

		@property
		def x(self):
			return self.__x

		@x.setter
		def x(self, value):
			self.__x = value

		@staticmethod
		def instance():
			if not Singleton.__instance:
				Singleton.__instance = Singleton()
			return Singleton.__instance

if __name__ == "__main__":
    s1 = Singleton.instance()
    s2 = Singleton.instance()
    s1.x = 10

    print("Singleton")
    print("s1.x = {} | s2.x = {}".format(s1.x, s2.x))
    print("id(s1) = {} | id(s2) = {}".format(id(s1), id(s2)))
    print("-----------------------")