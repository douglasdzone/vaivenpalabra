__author__ = 'dougl_000'
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from azure.storage import TableService, Entity


class AzureTable():
    def create_table(self):
        table_service = TableService(account_name='vaivenpalabras', account_key='MTismmfjowGsfTPwagoVX3nFrDwlAsVcGc+pfag49Ew00fgvLFLjEVj89Pe5MWX7qHFPGujvv0SJlCUd6pnJPQ==')
        table_service.create_table('tasktable')

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
       color = (random(), random(), random())
       with self.canvas:
            Color(*color)
            d = 30.0
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
       color = (random(), random(), random())
       with self.canvas:
            Color(*color)
            d = 30.0
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):
 def build(self):
        print("ddz")
        parent = Widget()
        painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        parent.add_widget(painter)
        parent.add_widget(clearbtn)


        def clear_canvas(obj):
            print("enter...........")
            AzureTable.create_table(self)
            print("exit...........")
            painter.canvas.clear()
        clearbtn.bind(on_release=clear_canvas)

        return parent


if __name__ == '__main__':
    MyPaintApp().run()