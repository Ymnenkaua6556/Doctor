from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import (Color,Rectangle)
from Text import Dict_of_muscles
from kivy.clock import Clock

gender_muscles = "man"  #Мужчина стоит
side_muscles = "forward"     #Человек смотрит прямо

side2  = "forward" #скелет смотрит прямо

gender_skin= "man"  #Мужчина стоит
side_skin = "forward"     #Человек смотрит прямо

image_gender_btn_blue = "images/Switch_blue.png"
image_gender_btn_pink = "images/Switch_pink.png"

key = "Двоголовий м'яз плеча"
Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

Window.size = (800, 600)

class Muscle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        self.fl_layout = FloatLayout()
        self.body = Image(source = "Images/Muscles/Man1.png", pos_hint = {'center_x' : .75, "center_y" : .49}, size_hint = (None, None), size = (500, 600))

        self.fl_layout.add_widget(self.body)
        main_layout.add_widget(self.fl_layout)
        
        self.fl_layout2 = None

        #кнопки с мышцами
        self.btn_biceps = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #Біцепс
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .9, "center_y" : .71})
        self.btn_biceps.bind(on_press = self.on_press_biceps)
        
        self.tailor_muscle = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",   #кравецький м'яз
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .8, "center_y" : .46})
        self.tailor_muscle.bind(on_press = self.on_press_tailor)
        
        self.rectus_femoris_muscle = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png", #Прямий м'яз стегна
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .83, "center_y" : .42})
        self.rectus_femoris_muscle.bind(on_press = self.on_rectus_femoris)
        
        self.triceps = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #тріцепс
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .6, "center_y" : .7})
        self.triceps.bind(on_press = self.on_press_triceps)

        self.Quadriceps_thigh_muscle = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #квадріцепс
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .79, "center_y" : .37})
        self.Quadriceps_thigh_muscle.bind(on_press = self.on_quadriceps_thigh_muscle)

        self.Gluteal_muscles = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #попа
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .83, "center_y" : .48})
        self.Gluteal_muscles.bind(on_press = self.on_gluteal_muscles)
        
        self.lumbar = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       ##Великий Поперековий м'яз
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .64, "center_y" : .54})
        self.lumbar.bind(on_press = self.on_press_lumbar)
        
        self.delta = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #delta
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .59, "center_y" : .78})
        self.delta.bind(on_press = self.on_press_delta)
        
        self.forearm = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #Предплечье
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .93, "center_y" : .6})
        self.forearm.bind(on_press = self.on_press_forearm)
        
        self.pectoral = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #Грудь
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .83, "center_y" : .76})
        self.pectoral.bind(on_press = self.on_press_pectoral)
        
        self.toothed = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #зубчастые
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .67, "center_y" : .67})
        self.toothed.bind(on_press = self.on_press_toothed)
        
        self.abdominis = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       #Живот(прес)
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .76, "center_y" : .63})
        self.abdominis.bind(on_press = self.on_press_abdominis)

        self.back_muscle = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .68, "center_y" : .64})
        self.back_muscle.bind(on_press = self.on_press_back_muscle)

        self.trapezius = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       
                          size_hint = (None, None), size = (20, 20), pos_hint = {'center_x' : .73, "center_y" : .69})
        self.trapezius.bind(on_press = self.on_press_trapezius)

        self.platysmal = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",       
                          size_hint = (None, None), size = (25, 25), pos_hint = {'center_x' : .76, "center_y" : .83})
        self.platysmal.bind(on_press = self.on_press_platysmal)

        self.fl_layout.add_widget(self.abdominis)
        self.fl_layout.add_widget(self.toothed)
        self.fl_layout.add_widget(self.pectoral)
        self.fl_layout.add_widget(self.forearm)
        self.fl_layout.add_widget(self.delta)
        self.fl_layout.add_widget(self.lumbar)
        self.fl_layout.add_widget(self.btn_biceps)
        self.fl_layout.add_widget(self.tailor_muscle)
        self.fl_layout.add_widget(self.rectus_femoris_muscle)
        self.fl_layout.add_widget(self.Quadriceps_thigh_muscle)
        self.fl_layout.add_widget(self.platysmal)
        
        self.btn_gender = Button(background_normal = image_gender_btn_blue, background_down = image_gender_btn_blue,size_hint = (None, None), size = (90, 45), pos_hint = {"x" : .75})
        self.btn_gender.on_press = self.gender
        layout.add_widget(self.btn_gender)
        
        btn_layer = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_biceps(self, instance):
        global key
        key="Двоголовий м'яз плеча"
        self.manager.current = 'Print_info'
        
    def on_press_tailor(self, instance):
        global key
        key = "Кравецький м'яз"
        self.manager.current = 'Print_info'
    
    def on_press_triceps(self, instance):
        global key
        key="Триголовий м'яз плеча"
        self.manager.current = 'Print_info'
        
    def on_rectus_femoris(self, instance):
        global key
        key = "Прямий м'яз стегна"
        self.manager.current = 'Print_info'
    
    def on_quadriceps_thigh_muscle(self, instance):
        global key
        key = "Чотириголовий м'яз стегна"
        self.manager.current = 'Print_info'

    def on_gluteal_muscles(self, instance):
        global key
        key = "Сідничні м'язи"
        self.manager.current = 'Print_info'
        
    def on_press_lumbar(self, instance):
        global key
        key="Великий поперековий м'яз"
        self.manager.current = 'Print_info'
    
    def on_press_delta(self, instance):
        global key
        key="Дельтоподібний м'яз"
        self.manager.current = 'Print_info'

    def on_press_forearm(self, instance):
        global key
        key="Предпліччя"
        self.manager.current = 'Print_info'
    
    def on_press_pectoral(self, instance):
        global key
        key="Грудний м'яз"
        self.manager.current = 'Print_info'
    
    def on_press_toothed(self, instance):
        global key
        key="Передній зубчастий м'яз"
        self.manager.current = 'Print_info'
    
    def on_press_abdominis(self, instance):
        global key
        key="Прямий м'яз живота"
        self.manager.current = 'Print_info'

    def on_press_back_muscle(self, instance):
        global key
        key="Найширший м'яз спини"
        self.manager.current = 'Print_info'

    def on_press_trapezius(self, instance):
        global key
        key="Трапецієподібний м'яз"
        self.manager.current = 'Print_info'

    def on_press_platysmal(self, instance):
        global key
        key="Платизмальний м'яз"
        self.manager.current = 'Print_info'

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()
            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .21, 'center_y' : .6})
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .36, 'center_y' : .6})
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .67, 'center_y' : .6})
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .83, 'center_y' : .6})

            self.bone.on_press = self.skeleton
            self.skin.on_press = self.skin_layer
            self.nerves.on_press = self.nerves_layer

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def skeleton(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skeleton'

    def skin_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skin'

    def nerves_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Nerves'
        
#########################################################################################################################        
    def gender(self):
        global gender_muscles
        global side_muscles
        if gender_muscles=="man" and side_muscles=="forward":
            self.body.source="Images/Muscles/Woman1.png"   #woman1
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            self.btn_biceps.pos_hint = {'center_x' : .95, "center_y" : .74}   #biceps
            self.tailor_muscle.pos_hint = {'center_x' : .87, "center_y" : .46} #tailor
            self.rectus_femoris_muscle.pos_hint = {'center_x' : .9, "center_y" : .42} #rectus
            self.Quadriceps_thigh_muscle.pos_hint = {'center_x' : .87, "center_y" : .35}
            self.lumbar.pos_hint = {'center_x' : .74, "center_y" : .52}
            self.abdominis.pos_hint = {'center_x' : .85, "center_y" : .63}
            self.forearm.pos_hint = {'center_x' : 1.1, "center_y" : .63}
            self.delta.pos_hint = {'center_x' : .64, "center_y" : .79}
            self.pectoral.pos_hint = {'center_x' : .88, "center_y" : .76}
            self.toothed.pos_hint = {'center_x' : .74, "center_y" : .67}
            self.platysmal.pos_hint = {'center_x' : .81, "center_y" : .85}
            gender_muscles="woman"
            
        elif gender_muscles=="woman" and side_muscles=="forward":
            self.body.source="Images/Muscles/Man1.png"   #man1
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            self.btn_biceps.pos_hint = {'center_x' : .9, "center_y" : .71}   #biceps
            self.tailor_muscle.pos_hint = {'center_x' : .8, "center_y" : .46} #tailor
            self.rectus_femoris_muscle.pos_hint = {'center_x' : .83, "center_y" : .42} #rectus
            self.Quadriceps_thigh_muscle.pos_hint = {'center_x' : .79, "center_y" : .37}
            self.lumbar.pos_hint = {'center_x' : .64, "center_y" : .54}
            self.abdominis.pos_hint = {'center_x' : .76, "center_y" : .63}
            self.forearm.pos_hint = {'center_x' : .93, "center_y" : .6}
            self.delta.pos_hint = {'center_x' : .59, "center_y" : .78}
            self.pectoral.pos_hint = {'center_x' : .83, "center_y" : .76}
            self.toothed.pos_hint = {'center_x' : .67, "center_y" : .67}
            self.platysmal.pos_hint = {'center_x' : .76, "center_y" : .83}
            gender_muscles = "man"
            
        elif gender_muscles == "man" and side_muscles == "back":
            self.body.source="Images/Muscles/Woman2.png" #woman2
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            self.triceps.pos_hint = {'center_x' : .66, "center_y" : .69}
            self.Gluteal_muscles.pos_hint = {'center_x' : .88, "center_y" : .48}
            self.back_muscle.pos_hint = {'center_x' : .76, "center_y" : .65}
            self.trapezius.pos_hint = {'center_x' : .81, "center_y" : .72}
            gender_muscles="woman"
            
        elif gender_muscles=="woman" and side_muscles =="back":
            self.body.source="Images/Muscles/Man2.png"   #man2
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            self.triceps.pos_hint = {'center_x' : .6, "center_y" : .7}
            self.Gluteal_muscles.pos_hint = {'center_x' : .83, "center_y" : .48}
            self.back_muscle.pos_hint = {'center_x' : .68, "center_y" : .64}
            self.trapezius.pos_hint = {'center_x' : .73, "center_y" : .69}
            gender_muscles="man"
#################################################################################################################################################
    def rotate(self):
        global gender_muscles
        global side_muscles
        if gender_muscles=="man" and side_muscles=="forward":
            self.body.source="Images/Muscles/Man2.png"       #man
            self.fl_layout.remove_widget(self.btn_biceps)
            self.fl_layout.remove_widget(self.tailor_muscle)
            self.fl_layout.remove_widget(self.rectus_femoris_muscle)
            self.fl_layout.remove_widget(self.Quadriceps_thigh_muscle)
            self.fl_layout.remove_widget(self.lumbar)
            self.fl_layout.remove_widget(self.pectoral)
            self.fl_layout.remove_widget(self.abdominis)
            self.fl_layout.remove_widget(self.delta)
            self.fl_layout.remove_widget(self.forearm)
            self.fl_layout.remove_widget(self.toothed)
            self.fl_layout.remove_widget(self.platysmal)
            self.fl_layout.add_widget(self.triceps)
            self.fl_layout.add_widget(self.Gluteal_muscles)
            self.fl_layout.add_widget(self.back_muscle)
            self.fl_layout.add_widget(self.trapezius)
            self.triceps.pos_hint = {'center_x' : .6, "center_y" : .7}
            self.Gluteal_muscles.pos_hint = {'center_x' : .83, "center_y" : .48}
            self.back_muscle.pos_hint = {'center_x' : .68, "center_y" : .64}
            self.trapezius.pos_hint = {'center_x' : .73, "center_y" : .69}
            side_muscles="back"

        elif gender_muscles=="woman" and side_muscles=="forward":
            self.body.source="Images/Muscles/Woman2.png"     #woman2
            self.fl_layout.remove_widget(self.btn_biceps)
            self.fl_layout.remove_widget(self.tailor_muscle)
            self.fl_layout.remove_widget(self.rectus_femoris_muscle)
            self.fl_layout.remove_widget(self.Quadriceps_thigh_muscle)
            self.fl_layout.remove_widget(self.lumbar)
            self.fl_layout.remove_widget(self.pectoral)
            self.fl_layout.remove_widget(self.abdominis)
            self.fl_layout.remove_widget(self.delta)
            self.fl_layout.remove_widget(self.forearm)
            self.fl_layout.remove_widget(self.toothed)
            self.fl_layout.remove_widget(self.platysmal)
            self.fl_layout.add_widget(self.triceps)
            self.fl_layout.add_widget(self.Gluteal_muscles)
            self.fl_layout.add_widget(self.back_muscle)
            self.fl_layout.add_widget(self.trapezius)
            self.triceps.pos_hint = {'center_x' : .66, "center_y" : .69}
            self.Gluteal_muscles.pos_hint = {'center_x' : .88, "center_y" : .48}
            self.back_muscle.pos_hint = {'center_x' : .76, "center_y" : .65}
            self.trapezius.pos_hint = {'center_x' : .81, "center_y" : .72}
            side_muscles="back"

        elif gender_muscles =="man" and side_muscles =="back":
            self.body.source="Images/Muscles/Man1.png"   #man1
            self.fl_layout.add_widget(self.btn_biceps)
            self.fl_layout.add_widget(self.tailor_muscle)
            self.fl_layout.add_widget(self.rectus_femoris_muscle)
            self.fl_layout.add_widget(self.Quadriceps_thigh_muscle)
            self.fl_layout.add_widget(self.delta)
            self.fl_layout.add_widget(self.forearm)
            self.fl_layout.add_widget(self.abdominis)
            self.fl_layout.add_widget(self.toothed)
            self.fl_layout.add_widget(self.pectoral)
            self.fl_layout.add_widget(self.lumbar)
            self.fl_layout.add_widget(self.platysmal)
            self.fl_layout.remove_widget(self.Gluteal_muscles)
            self.fl_layout.remove_widget(self.triceps)
            self.fl_layout.remove_widget(self.back_muscle)
            self.fl_layout.remove_widget(self.trapezius)
            self.btn_biceps.pos_hint = {'center_x' : .9, "center_y" : .71}   #biceps
            self.tailor_muscle.pos_hint = {'center_x' : .8, "center_y" : .46} #tailor
            self.rectus_femoris_muscle.pos_hint = {'center_x' : .83, "center_y" : .42} #rectus
            self.Quadriceps_thigh_muscle.pos_hint = {'center_x' : .79, "center_y" : .37}
            self.lumbar.pos_hint = {'center_x' : .64, "center_y" : .54}
            self.abdominis.pos_hint = {'center_x' : .76, "center_y" : .63}
            self.forearm.pos_hint = {'center_x' : .93, "center_y" : .6}
            self.delta.pos_hint = {'center_x' : .59, "center_y" : .78}
            self.pectoral.pos_hint = {'center_x' : .83, "center_y" : .76}
            self.toothed.pos_hint = {'center_x' : .67, "center_y" : .67}
            self.platysmal.pos_hint = {'center_x' : .76, "center_y" : .83}
            side_muscles="forward"

        elif gender_muscles=="woman" and side_muscles =="back":
            self.body.source="Images/Muscles/Woman1.png"     #woman1
            self.fl_layout.add_widget(self.btn_biceps)
            self.fl_layout.add_widget(self.tailor_muscle)
            self.fl_layout.add_widget(self.rectus_femoris_muscle)
            self.fl_layout.add_widget(self.Quadriceps_thigh_muscle)
            self.fl_layout.add_widget(self.delta)
            self.fl_layout.add_widget(self.forearm)
            self.fl_layout.add_widget(self.abdominis)
            self.fl_layout.add_widget(self.toothed)
            self.fl_layout.add_widget(self.pectoral)
            self.fl_layout.add_widget(self.lumbar)
            self.fl_layout.add_widget(self.platysmal)
            self.fl_layout.remove_widget(self.Gluteal_muscles)
            self.fl_layout.remove_widget(self.triceps)
            self.fl_layout.remove_widget(self.back_muscle)
            self.fl_layout.remove_widget(self.trapezius)
            self.btn_biceps.pos_hint = {'center_x' : .95, "center_y" : .74}   #biceps
            self.tailor_muscle.pos_hint = {'center_x' : .87, "center_y" : .46} #tailor
            self.rectus_femoris_muscle.pos_hint = {'center_x' : .9, "center_y" : .42} #rectus
            self.Quadriceps_thigh_muscle.pos_hint = {'center_x' : .87, "center_y" : .35}
            self.lumbar.pos_hint = {'center_x' : .74, "center_y" : .52}
            self.abdominis.pos_hint = {'center_x' : .85, "center_y" : .63}
            self.forearm.pos_hint = {'center_x' : 1.1, "center_y" : .63}
            self.delta.pos_hint = {'center_x' : .64, "center_y" : .79}
            self.pectoral.pos_hint = {'center_x' : .88, "center_y" : .76}
            self.toothed.pos_hint = {'center_x' : .74, "center_y" : .67}
            self.platysmal.pos_hint = {'center_x' : .81, "center_y" : .85}
            side_muscles="forward"

class Skin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        self.fl_layout = FloatLayout()
        self.body = Image(source = "Images/Skin/skin_man1.png", pos_hint = {'center_x' : .75, "center_y" : .49}, size_hint = (None, None), size = (500, 600))
        self.fl_layout.add_widget(self.body)
        main_layout.add_widget(self.fl_layout)
        
        self.fl_layout2 = None
        
        self.btn_gender = Button(background_normal = image_gender_btn_blue, background_down = image_gender_btn_blue,size_hint = (None, None), size = (90, 45), pos_hint = {"x" : .75})
        self.btn_gender.on_press = self.gender
        layout.add_widget(self.btn_gender)
        
        btn_layer = Button(background_normal = "images/skin.png", background_down = "images/skin.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def layer(self):
        global x, y
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()
            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .21, 'center_y' : .6})
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .36, 'center_y' : .6})
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .67, 'center_y' : .6})
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .83, 'center_y' : .6})

            self.bone.on_press = self.skeleton
            self.muscle.on_press = self.muscles
            self.nerves.on_press = self.nerves_layer

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def skeleton(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skeleton'

    def muscles(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2 = None
        self.manager.current = 'Muscles'

    def nerves_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Nerves'
        
#########################################################################################################################        
    def gender(self):
        global gender_skin
        global side_skin
        if gender_skin=="man" and side_skin=="forward":
            self.body.source="Images/Skin/skin_woman1.png"   #woman1
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            gender_skin="woman"
            
        elif gender_skin=="woman" and side_skin=="forward":
            self.body.source="Images/Skin/skin_man1.png"   #man1
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            gender_skin="man"
            
        elif gender_skin =="man" and side_skin =="back":
            self.body.source="Images/Skin/skin_woman2.png" #woman2
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            gender_skin="woman"
            
        elif gender_skin=="woman" and side_skin =="back":
            self.body.source="Images/Skin/skin_man2.png"   #man2
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            gender_skin="man"
#################################################################################################################################################
    def rotate(self):
        global gender_skin
        global side_skin
        if gender_skin=="man" and side_skin=="forward":
            self.body.source="Images/Skin/skin_man2.png"       #man2
            side_skin="back"

        elif gender_skin=="woman" and side_skin=="forward":
            self.body.source="Images/Skin/skin_woman2.png"     #woman2
            side_skin="back"

        elif gender_skin =="man" and side_skin =="back":
            self.body.source="Images/Skin/skin_man1.png"   #man1
            side_skin="forward"

        elif gender_skin=="woman" and side_skin =="back":
            self.body.source="Images/Skin/skin_woman1.png"     #woman1
            side_skin="forward"

###########################################################################################################################
class Skeleton(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        self.body = Image(source = "Images/Skeleton/Bone1.png", pos_hint = {'center_x' : .75, "center_y" : .49}, size_hint = (None, None), size = (500, 600))
        main_layout.add_widget(self.body)

        self.fl_layout2 = None

        btn_layer = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75},background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()
            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .21, 'center_y' : .6})
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .36, 'center_y' : .6})
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .67, 'center_y' : .6})
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .83, 'center_y' : .6})

            self.muscle.on_press = self.muscle_layer
            self.skin.on_press = self.skin_layer
            self.nerves.on_press = self.nerves_layer

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def muscle_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Muscles'

    def skin_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skin'

    def nerves_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Nerves'

    def rotate(self):
        global side2
        if side2 == "forward":
            self.body.source = "Images/Skeleton/Bone2.png"
            side2 = "back"
        else:
            self.body.source = "Images/Skeleton/Bone1.png"
            side2 = "forward"

class Nerves(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        self.fl_layout = FloatLayout()
        self.body = Image(source = "Images/Nerves/nervesm1.png", pos_hint = {'center_x' : .75, "center_y" : .49}, size_hint = (None, None), size = (500, 600))
        self.fl_layout.add_widget(self.body)
        main_layout.add_widget(self.fl_layout)
        
        self.fl_layout2 = None
        
        self.btn_gender = Button(background_normal = image_gender_btn_blue, background_down = image_gender_btn_blue,size_hint = (None, None), size = (90, 45), pos_hint = {"x" : .75})
        self.btn_gender.on_press = self.gender
        layout.add_widget(self.btn_gender)
        
        btn_layer = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def layer(self):
        global x, y
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()
            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .21, 'center_y' : .6})
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .36, 'center_y' : .6})
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .52, 'center_y' : .6})
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .67, 'center_y' : .6})
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos_hint = {'center_x' : .83, 'center_y' : .6})

            self.bone.on_press = self.skeleton
            self.muscle.on_press = self.muscles
            self.skin.on_press = self.skin_layer

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def skeleton(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skeleton'

    def muscles(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2 = None
        self.manager.current = 'Muscles'

    def skin_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Skin'
        
#########################################################################################################################        
    def gender(self):
        global gender_skin
        global side_skin
        if gender_skin=="man" and side_skin=="forward":
            self.body.source="Images/Nerves/nervesw1.png"   #woman1
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            gender_skin="woman"
            
        elif gender_skin=="woman" and side_skin=="forward":
            self.body.source="Images/Nerves/nervesm1.png"   #man1
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            gender_skin="man"
            
        elif gender_skin =="man" and side_skin =="back":
            self.body.source="Images/Nerves/nervesw2.png" #woman2
            self.btn_gender.background_normal = image_gender_btn_pink
            self.btn_gender.background_down = image_gender_btn_pink
            gender_skin="woman"
            
        elif gender_skin=="woman" and side_skin =="back":
            self.body.source="Images/Nerves/nervesm2.png"   #man2
            self.btn_gender.background_normal = image_gender_btn_blue
            self.btn_gender.background_down = image_gender_btn_blue
            gender_skin="man"
#################################################################################################################################################
    def rotate(self):
        global gender_skin
        global side_skin
        if gender_skin=="man" and side_skin=="forward":
            self.body.source="Images/Nerves/nervesm2.png"       #man2
            side_skin="back"

        elif gender_skin=="woman" and side_skin=="forward":
            self.body.source="Images/Nerves/nervesw2.png"     #woman2
            side_skin="back"

        elif gender_skin =="man" and side_skin =="back":
            self.body.source="Images/Nerves/nervesm1.png"   #man1
            side_skin="forward"

        elif gender_skin=="woman" and side_skin =="back":
            self.body.source="Images/Nerves/nervesw1.png"     #woman1
            side_skin="forward"

class Print_info(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global key
        float_layout = FloatLayout()
        
        back_gr=Button(text = "", background_color = (0, 0, 0, 1), size_hint = (None, None), size = (600, 500), pos_hint = {'center_x' : .45, 'center_y' : .5})
        back_gr.opacity = 0.6
        back_gr_white=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 150), pos_hint = {'center_x' : .45, 'center_y' : .76})
        back_gr_white.opacity = 0.4
        back_gr_white2=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 105), pos_hint = {'center_x' : .45, 'center_y' : .55})
        back_gr_white2.opacity = 0.3
        back_gr_white3=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 200), pos_hint = {'center_x' : .45, 'center_y' : .3})
        back_gr_white3.opacity = 0.2
        

        self.name_muscle = Label(text = key, pos_hint = {'center_x' : .45, 'center_y' : .85},font_size='25sp')
        function_text = Label(text = "Функція", pos_hint = {'center_x' : .45, 'center_y' : .8},font_size='20sp')
        self.function = Label(text = Dict_of_muscles[key]['Функція'], pos_hint = {'center_x' : .45, 'center_y' : .7},font_size='18sp')
        injury_text = Label(text = "Травми/Хвороби", pos_hint = {'center_x' : .45, 'center_y' : .6},font_size='20sp')
        self.injury = Label(text = Dict_of_muscles[key]['Травми/Хвороби'], pos_hint = {'center_x' : .45, 'center_y' : .5},font_size='18sp')
        exercices_text = Label(text = "Корисні вправи", pos_hint = {'center_x' : .45, 'center_y' : .4},font_size='20sp')
        self.exercices = Label(text = Dict_of_muscles[key]['Корисні вправи'], pos_hint = {'center_x' : .45, 'center_y' : .3},font_size='18sp')

        Clock.schedule_interval(self.Update, 0.1)

        btn_close_bg = Button(text = "Нажми, чтобы закрыть", size_hint = (None, None), size = (190, 50), pos_hint = {'center_x' : .65, 'center_y' : .04}, background_color = yellow)
        btn_close_bg.bind(on_press=self.close_info)
        
        float_layout.add_widget(back_gr_white)
        float_layout.add_widget(back_gr_white2)
        float_layout.add_widget(back_gr_white3)
        float_layout.add_widget(back_gr)
        float_layout.add_widget(self.name_muscle)
        float_layout.add_widget(function_text)
        float_layout.add_widget(self.function)
        float_layout.add_widget(injury_text)
        float_layout.add_widget(self.injury)
        float_layout.add_widget(exercices_text)
        float_layout.add_widget(self.exercices)
        float_layout.add_widget(btn_close_bg)
        self.add_widget(float_layout)

    def Update(self, *args):
        global key
        self.name_muscle.text = key
        self.function.text = Dict_of_muscles[key]['Функція']
        self.injury.text = Dict_of_muscles[key]['Травми/Хвороби']

    def close_info(self, instance):
        self.manager.current = "Muscles"

class Screen(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Muscle(name = 'Muscles'))
        sm.add_widget(Skin(name = 'Skin'))
        sm.add_widget(Skeleton(name='Skeleton'))
        sm.add_widget(Nerves(name='Nerves'))
        sm.add_widget(Print_info(name='Print_info'))
        
        return sm

app = Screen()
app.run()
           
