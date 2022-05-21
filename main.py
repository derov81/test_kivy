# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from  kivy.uix.pagelayout import PageLayout



class Container(FloatLayout):
    pass

class Pages(PageLayout):
    pass



class CalcCaloryApp(App):
    def build(self):
        self.load_kv("CalcCalory.kv")
        return Container()










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CalcCaloryApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
