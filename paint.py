from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line, Canvas
from kivy.uix.button import Button
from random import random, randint
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.base import stopTouchApp, runTouchApp
from kivy.uix.label import Label
import sys, os
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton
from kivy.lang import Builder

Builder.load_string('''
''')

d = 1
class Paint(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points = [touch.x , touch.y], width=d)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x , touch.y]

d = 1
class Paint2(App):
    def build(self):
        parent = BoxLayout(orientation= 'vertical')
        #bar = ActionBar()
        #btn = Button(text='SHOW', size_hint=(0.07, 0.1))
        self.painter = Paint()
        label = Label(text='[b]PythonPaint[b]', markup=True, font_size=50, color=(d,d,d))
        clearbtn = Button(text= '[b]Apagar[b]',markup=True, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})
        corazul = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(0,0,1,1))
        corvermelho = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(1,0,0,1))
        corverde = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(0,1,0,1))
        coramarelo = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(1,1,0,1))
        corlaranja = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(1,0.5,0,1))
        corrosa = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(1,0,0.5,1))
        corroxo = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(0.5,0,0.5,1))
        corcinza = Button(text = '',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(0.5,0.5,0.5,1))
        corbranco = Button(text = '',font_size= 14,size_hint=(0.05,0.1),background_color=(4,4,4,1))
        corpreta = Button(text = '[b]Preto[b]',font_size= 14, markup=True,size_hint=(0.05,0.1),background_color=(0,0,0,1))
        largura_menor = Button(text = "Linha 1", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})
        largura_media = Button(text = "Linha 2.5", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})
        largura_maior = Button(text = "Linha 5", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})
        sair = Button(text = "Sair", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .9}) 
        fundo_branco = Button(text = "Fundo branco", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})
        fundo_preto = Button(text = "Fundo preto", font_size=14, size_hint=(0.1,0.1),pos_hint = {"x": .9, "y": .5})		
		
        clearbtn.bind(on_release = self.clear_canvas)
        corazul.bind(on_release = self.corazul)
        corvermelho.bind(on_release = self.corvermelho)
        corverde.bind(on_release = self.corverde)
        coramarelo.bind(on_release = self.coramarelo)
        corlaranja.bind(on_release = self.corlaranja)
        corrosa.bind(on_release = self.corrosa)
        corroxo.bind(on_release = self.corroxo)
        corcinza.bind(on_release = self.corcinza)
        corbranco.bind(on_release = self.corbranco)
        corpreta.bind(on_release = self.corpreta)
        largura_menor.bind(on_release = self.largura_menor)
        largura_media.bind(on_release = self.largura_media)
        largura_maior.bind(on_release = self.largura_maior)
        sair.bind(on_release = self.sair)
        fundo_branco.bind(on_release = self.branco)
        fundo_preto.bind(on_release = self.preto)
        #btn.bind(on_release= self.show)
		
        #parent.add_widget(bar)
        parent.add_widget(label)
        parent.add_widget(self.painter)
        parent.add_widget(corazul)
        parent.add_widget(corvermelho)
        parent.add_widget(corverde)
        parent.add_widget(coramarelo)
        parent.add_widget(corlaranja)
        parent.add_widget(corrosa)
        parent.add_widget(corroxo)
        parent.add_widget(corcinza)
        parent.add_widget(corbranco)
        parent.add_widget(corpreta)
        parent.add_widget(fundo_branco)
        parent.add_widget(fundo_preto)
        parent.add_widget(sair)
        parent.add_widget(clearbtn)
        parent.add_widget(largura_menor)
        parent.add_widget(largura_media)
        parent.add_widget(largura_maior)
        #parent.add_widget(btn)
		
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def corazul(self, obj):
        self.painter.canvas.add(Color(0,0,1))
    def corvermelho(self, obj):
        self.painter.canvas.add(Color(1,0,0))
    def corverde(self, obj):
        self.painter.canvas.add(Color(0,1,0))
    def coramarelo(self, obj):
        self.painter.canvas.add(Color(1,1,0))
    def corlaranja(self, obj):
        self.painter.canvas.add(Color(1,0.5,0))
    def corrosa(self, obj):
        self.painter.canvas.add(Color(1,0,0.5))
    def corroxo(self, obj):
        self.painter.canvas.add(Color(0.5,0,0.5))
    def corcinza(self, obj):
        self.painter.canvas.add(Color(0.5,0.5,0.5))
    def corbranco(self, obj):
        self.painter.canvas.add(Color(1,1,1))
    def corpreta(self, obj):
        self.painter.canvas.add(Color(0,0,0))
    def largura_menor(self, obj):
        global d
        d = 1
    def largura_media(self, obj):
        global d
        d = 2.5
    def largura_maior(self, obj):
        global d
        d = 5 
    def sair(self, obj):
        self.stop()
        os._exit(0)
		
    def branco(self, obj):
        self.painter.canvas.add(Color(1,1,1))
        self.painter.canvas.add(Rectangle(pos=(0,0),size=(1380,500)))
    def preto(self, obj):
        self.painter.canvas.add(Color(0,0,0))
        self.painter.canvas.add(Rectangle(pos=(0,0),size=(1380,500)))
        
    def show(self, *largs):
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(self, 'text', x))
        item = Button(text='hello', size_hint=(0.07,0.1))
        item.bind(on_release=lambda btn: dp.select(btn.text))
        dp.add_widget(item)
        dp.open(self)
	
	
if __name__ == '__main__':   
    Paint2().run()
    
