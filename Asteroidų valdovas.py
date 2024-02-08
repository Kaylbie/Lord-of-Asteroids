import random
import time
import math
import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.bgpic("setupas.gif")
turtle.title("Asteroidų valdovas")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)
#Paveikslėliai
turtle.register_shape("meteoritas.gif")
turtle.register_shape("palydovas.gif")
#Klases
class Sprite(turtle.Turtle):
     def __init__(self, spriteshape, color, startx, starty):
          turtle.Turtle.__init__(self, shape = spriteshape)
          self.speed(0)
          self.penup()
          self.color(color)
          self.fd(0)
          self.goto(startx, starty)
          self.speed = 0
          
     def susidurimas(self, other):
          if (self.xcor() >= (other.xcor() - 20)) and \
               (self.xcor() <= (other.xcor() + 20)) and \
               (self.ycor() >= (other.ycor() - 20)) and \
               (self.ycor() <= (other.ycor() + 20)):
               return True
          else:
               return False
     #Judejimas          
     def jud(self):
          self.fd(self.speed)
          
          if self.xcor() < -290:
               self.rt(60)
               self.setx(-290)
          
          elif self.xcor() > 290:
               self.rt(60)
               self.setx(290)
               
          if self.ycor() < -290:
               self.rt(60)
               self.sety(-290)          
          
          elif self.ycor() > 290:
               self.rt(60)
               self.sety(290)

class Zaidejas(Sprite):
            def __init__(self, spriteshape, color, startx, starty):
                Sprite.__init__(self, spriteshape, color, startx, starty)
                self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
                self.speed = 0
                self.lives = 3
                self.setheading(90)
            def pas_kair(self):
                self.lt(45)
            def pas_des(self):
                self.rt(45)
            def greiciau(self):
                self.speed += 0.2
            def leciau(self):
                self.speed -= 0.2

class Meteoritas(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.speed = 1
          self.setheading(random.randint(0,360))
     def jud(self):
          self.fd(self.speed)
          if self.xcor() < -290:
               self.lt(60)
               self.setx(-290)          
          elif self.xcor() > 290:
               self.lt(60)
               self.setx(290)              
          if self.ycor() < -290:
               self.lt(60)
               self.sety(-290)                    
          elif self.ycor() > 290:
               self.lt(60)
               self.sety(290)           

class Palydovas(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.speed = 1
          self.setheading(random.randint(0,360))          
     def jud(self):
          self.fd(self.speed)          
          degrees = random.randint(20, 60)          
          if self.xcor() < -290:
               self.lt(degrees)
               self.setx(-290)          
          elif self.xcor() > 290:
               self.lt(degrees)
               self.setx(290)               
          if self.ycor() < -290:
               self.lt(degrees)
               self.sety(-290)                    
          elif self.ycor() > 290:
               self.lt(degrees)
               self.sety(290)              
     def saugotis(self, other):
          if (self.xcor() >= (other.xcor() -40)) and \
               (self.xcor() <= (other.xcor() + 40)) and \
               (self.ycor() >= (other.ycor() -40)) and \
               (self.ycor() <= (other.ycor() + 40)):   
               self.lt(30)    

class Kulka(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, startx, starty)
          self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
          self.virsus = "pasirenges"
          self.speed = 15          
     def sauna(self):
          if self.virsus == "pasirenges":
               self.virsus = "sauti"          
     def jud(self):
          if self.virsus == "pasirenges":
               self.hideturtle()               
               self.goto(-1000,1000)         
          if self.virsus == "sauti":               
               self.goto(zaidejas.xcor(), zaidejas.ycor())
               self.setheading(zaidejas.heading())
               self.showturtle()
               self.virsus = "saudo"               
               return True                    
          if self.virsus == "saudo":
               self.fd(self.speed)                                     
          if self.xcor() < -290 or self.xcor() > 290 \
               or self.ycor() < -290 or self.ycor() > 290:
               self.virsus = "pasirenges"              
     
class Dalele(Sprite):
     def __init__(self, spriteshape, color, startx, starty):
          Sprite.__init__(self, spriteshape, color, -1000, -1000)
          self.frame = 0
          self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)          
     def sprogimas(self, startx, starty):
          self.goto(startx, starty)
          self.setheading(random.randint(0, 360))
          self.frame = 1          
     def jud(self):
          if self.frame != 0:
               self.fd((20-self.frame)/2)
               self.frame += 1               
               if self.frame < 6:
                    self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
               elif self.frame < 11:
                    self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
               else:
                    self.shapesize(stretch_wid=0.05, stretch_len=0.05, outline=None)               
               if self.frame > 18:
                    self.frame = 0
                    self.goto(-1000, -1000)                    
          #Linijos patikrinimas
          if self.xcor() < -290 or self.xcor() > 290 \
               or self.ycor() < -290 or self.ycor() > 290:
               self.frame = 0
               self.goto(-1000, -1000)
                              
class Zaidimas():
     def __init__(self):
          self.lygis = 1
          self.score = 0
          self.veik = "tais"
          self.pen = turtle.Turtle()
          self.lives = 3
          self.gravity = 0.1          
     def lenta(self):
          #Lenta
          self.pen.speed(0)
          self.pen.color("white")
          self.pen.pensize(3)
          self.pen.penup()
          self.pen.goto(-300, 300)
          self.pen.pendown()
          for side in range(4):
               self.pen.fd(600)
               self.pen.rt(90)
          self.pen.ht()
          self.pen.penup()
     def pradzia(self):
                turtle.bgpic("kosmosas.gif")
                self.veik = "paruosimas"                
     def virsus(self):
          self.pen.undo()
          if zaidimas.lives > 0:
               msg = u"Lygis: %s Gyvybės: %s Taškai: %s" %(self.lygis, self.lives, self.score)      
          else: 
               msg = u"Žaidimas baigtas Taškai: %s" %(self.score)
          self.pen.penup()
          self.pen.goto(-300, 310)
          self.pen.write(msg, font=("Arial", 16, "normal"))
     def sauti(self):
          for kulka in kulkos:
               if kulka.virsus == "pasirenges":
                    kulka.sauna()
                    break 
     def taisykles(self):
          turtle.bgpic("setupas.gif")
          turtle.update()
          time.sleep(5)
          turtle.bgpic("kosmosas.gif")
          self.veik = "paruosimas"          
     def veikla(self, veik):
          veiklos = ["tais", "paruosimas", "zaidzia", "perkrauti", "baigta"]
          if veik in veiklos:
               self.veik = veik
          else:
               veik = "tais"
               
zaidimas = Zaidimas()
zaidimas.lenta()
zaidimas.virsus()
if zaidimas.veik == "tais":
     zaidimas.taisykles()
if zaidimas.veik == "paruosimas":
     zaidejas = Zaidejas("triangle", "white", 0, 0)               
     meteoritai = []
     for e in range(zaidimas.lygis):
          meteoritai.append(Meteoritas("meteoritas.gif", "red", -100, 0))
     palydovai = []
     for a in range(zaidimas.lygis):
          palydovai.append(Palydovas("palydovas.gif", "blue", 100, 0))          
     daleles = []
     colors = ["red", "yellow", "orange"]
     for p in range(20):
          daleles.append(Dalele("circle", random.choice(colors), -1000, -1000))
     kulkos = []
     for b in range(2):
          kulkos.append(Kulka("triangle", "yellow", 0.0, 0.0))
     zaidimas.veikla("zaidzia")

turtle.onkey(zaidejas.pas_kair, "Left")
turtle.onkey(zaidejas.pas_des, "Right")
turtle.onkey(zaidejas.greiciau, "Up")
turtle.onkey(zaidejas.leciau, "Down")
turtle.onkey(zaidimas.sauti, "space")
turtle.listen()
x = random.randint(-250, 250)
y = random.randint(-250, 250)
while True:        
     turtle.update()
     if zaidimas.veik == "perkrauti":
          zaidimas.lives = 3
          zaidimas.score = 0
          zaidejas.speed = 0
          zaidejas.goto(0,0)
          zaidejas.setheading(0)
          zaidejas.dx = 0
          zaidejas.dy = 0                                        
          for meteoritas in meteoritai:
               meteoritas.goto(x, y)
               meteoritas.speed = 1               
          for palydovas in palydovai:
               palydovas.goto(x, y)     
               palydovas.speed = 1               
          zaidimas.veikla("zaidzia")     
     if zaidimas.veik == "zaidzia":
          zaidejas.jud()                                                                                          
          for kulka in kulkos:
               kulka.jud()     
          for meteoritas in meteoritai: 
               meteoritas.jud()
               if zaidejas.susidurimas(meteoritas):                    
                    zaidejas.color("red")
                    for dalele in daleles:
                         dalele.sprogimas(meteoritas.xcor(), meteoritas.ycor())
                    zaidejas.rt(random.randint(100, 200))
                    meteoritas.goto(x, y)    
                    meteoritas.speed -= 0.5
                    zaidimas.lives -= 1
                    if zaidimas.lives < 1:
                         zaidimas.veikla("baigta")
                    zaidimas.virsus()
                    zaidejas.color("white")               
               for kulka in kulkos:
                    if kulka.susidurimas(meteoritas):                         
                         for dalele in daleles:
                              dalele.sprogimas(meteoritas.xcor(), meteoritas.ycor())                        
                         kulka.virsus = "pasirenges"
                         meteoritas.goto(x, y)    
                         meteoritas.setheading(random.randint(0,360))
                         meteoritas.speed += 0.2
                         zaidimas.score += 100
                         zaidimas.virsus()                                             
          for palydovas in palydovai:
               palydovas.jud()                              
               for meteoritas in meteoritai: 
                    palydovas.saugotis(meteoritas)    
               palydovas.saugotis(zaidejas)                    
               for kulka in kulkos:
                    if kulka.susidurimas(palydovas):                         
                         for dalele in daleles:
                              dalele.sprogimas(palydovas.xcor(), palydovas.ycor())
                         kulka.virsus = "pasirenges"
                         palydovas.goto(x, y)     
                         palydovas.speed += 0.5
                         zaidimas.score -= 50
                         zaidimas.virsus()                    
     for dalele in daleles:
          dalele.jud()                   
     if zaidimas.veik == "baigta":
          for i in range(360):
               zaidejas.rt(1)                                    
               for meteoritas in meteoritai:
                    meteoritas.ht()
                    meteoritas.clear()
                    del meteoritas                                        
               for palydovas in palydovai:
                    palydovas.ht()
                    palydovas.clear()
                    del palydovas                    
               meteoritas=[]
               meteoritai.append(Meteoritas("meteoritas.gif", "red", x, y))
               palydovai = []
               palydovai.append(Palydovas("palydovas.gif", "blue", x, y))
          else:
               exit()              
     if zaidimas.score / (zaidimas.lygis) > 500:
          zaidimas.lygis += 1
          palydovas.speed = 0.5
          meteoritas.speed = 0.6
          meteoritai.append(Meteoritas("meteoritas.gif", "red", x, y))
          palydovai.append(Palydovas("palydovas.gif", "blue", x, y))     
