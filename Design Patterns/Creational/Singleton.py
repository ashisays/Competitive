"""
This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.

"""
import traceback


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        '''
        static access method
        :return:
        '''
        if Singleton.__instance is None:
            return Singleton()
        else:
            return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton !!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

try:
    s = Singleton()
except Exception as e:
    print(e)
