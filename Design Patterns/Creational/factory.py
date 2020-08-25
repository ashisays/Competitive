"""
The factory pattern comes under the creational patterns list category. It provides one of the best ways to create an object. In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface.

Factory patterns are implemented in Python using factory method. When a user calls a method such that we pass in a string and the return value as a new object is implemented through factory method. The type of object used in factory method is determined by string which is passed through method.
"""

class Button:
    html = ""
    def get_html(self):
        return  self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Flash(Button):
    html = "<flash></flash>"

class ButtonFactory:
    def create_button(self,typ):
        targetClass = typ.capitalize()
        return  globals()[targetClass]()

b_obj = ButtonFactory()
buttons = ["image","input","flash"]
for button in buttons:
    print(b_obj.create_button(button).get_html())

