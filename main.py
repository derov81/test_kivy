# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import kivy
from kivymd.app import MDApp

from kivymd.uix.gridlayout import MDGridLayout

from kivymd.uix.label import MDLabel



class Container(MDGridLayout):
    pass






class CalcCaloryApp(MDApp):
     def build(self):
        self.load_kv("CalcCalory.kv")

        return Container()











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CalcCaloryApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
