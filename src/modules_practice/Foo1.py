class Foo0():
    def __init__(self):
        self.y= None

class Foo1(Foo0):
    def __init__(self):
        self.x= None

    #def foo1(self):
    def foo1(self, foo2Obj):

        print('foo1 func')
        foo2Obj.foo2()
        
        fooThree=f3.Foo3() 
        fooThree.foo3() 

import Foo3 as f3
import Foo0 as f0
