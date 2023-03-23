import tkinter as tk
from tkinter import *
import random
import os

os.system("cls")

class Vampir:
    def __init__(self):
        self.ukleto_mjesto = PhotoImage(file="ukleto_mjesto.png")
        self.slika_ukletog_mjesta = canvas.create_image(
            0, 0, image=self.ukleto_mjesto, anchor=NW)

        self.slika_vampir = PhotoImage(file="vampir.png")
        self.img = canvas.create_image(
            50, 500, image=self.slika_vampir, anchor=S)

        self.koordinate = canvas.coords(self.img)

        self.skok = None

        self.jump_direction = -1

        self.trenutne_koordinate = canvas.coords(self.img)

        self.fly = None

        self.fly_koordinate = canvas.coords(self.img)

        self.sudar = False

        self.bounds = False

    def right(self, event):
        x = 10
        y = 0
        if canvas.coords(self.img)[1] == 400 or canvas.coords(self.img)[1] == 100:
            canvas.move(self.img, 100, y)
        else:
            canvas.move(vampir.img, x, y)
        if event.keysym != "Up" and event.keysym != "Down":
            self.trenutne_koordinate = canvas.coords(self.img)
            if self.trenutne_koordinate[1] == 200 and self.skok != True:
                pass
            else:
                self.skok = False

    def left(self, event):
        x = -10
        y = 0
        if canvas.coords(self.img)[1] == 400 or canvas.coords(self.img)[1] == 100:
            canvas.move(self.img, -100, y)
        else:
            canvas.move(self.img, x, y)
        if event.keysym != "Up" and event.keysym != "Down":
            self.trenutne_koordinate = canvas.coords(self.img)
            if self.trenutne_koordinate[1] == 200 and self.skok != True:
                pass
            else:
                self.skok = False

    def jump(self, event):
        if event.keysym == "space":
            self.skok = True

    def fall(self, event):
        self.skok = False

    def obicni_skok(self):
        if self.skok == True:
            canvas.move(self.img, 0, self.jump_direction*100)
            self.trenutne_koordinate = canvas.coords(self.img)
            if self.jump_direction == -1 and self.trenutne_koordinate[1] <= 400:
                self.jump_direction = 1
            elif self.jump_direction == 1 and (self.trenutne_koordinate[1] >= 500 or self.trenutne_koordinate[1] >= 200):
                self.jump_direction = -1
        elif self.skok == False:
            self.trenutne_koordinate = canvas.coords(self.img)
            if (self.trenutne_koordinate[1] > 500):
                def funkcija_za_if():
                    if self.trenutne_koordinate[1] != 100 and self.trenutne_koordinate[1] != 200:
                        canvas.coords(
                            self.img, self.trenutne_koordinate[0], 500)
                    if self.trenutne_koordinate[1] == 100:
                        canvas.coords(
                            self.img, self.trenutne_koordinate[0], 200)
                    root.after(170, funkcija_za_if)
            elif (self.trenutne_koordinate[1] < 500):
                def funkcija_za_elif():
                    if self.trenutne_koordinate[1] != 100 and self.trenutne_koordinate[1] != 200:
                        canvas.coords(
                            self.img, self.trenutne_koordinate[0], 500)
                    if self.trenutne_koordinate[1] == 100:
                        canvas.coords(
                            self.img, self.trenutne_koordinate[0], 200)
                root.after(170, funkcija_za_elif)
            self.jump_direction = -1
        self.skok = None

    def up_press(self, event):
        if event.keysym == 'Up':
            self.fly = True
            if canvas.coords(vampir.img)[1] > 200 and self.fly == True:
                for axe.slika_sjekira in axe.slika_sjekira_lista:
                    if abs(canvas.coords(vampir.img)[0] - canvas.coords(axe.slika_sjekira)[0]) <= 55 and abs((500)-(canvas.coords(axe.slika_sjekira)[1])) <= 300:
                        print("Sudar detektiran!")
                        self.sudar = True

    def down_press(self, event):
        self.fly = False
        if canvas.coords(vampir.img)[1] < 500 and self.fly == False:
            for axe.slika_sjekira in axe.slika_sjekira_lista:
                if abs(canvas.coords(vampir.img)[0] - canvas.coords(axe.slika_sjekira)[0]) <= 55 and abs((500)-(canvas.coords(axe.slika_sjekira)[1])) <= 300:
                    print("Sudar detektiran!")
                    self.sudar = True

    def flying(self):
        if self.fly == True:
            canvas.move(self.img, 0, -300)
            self.fly_koordinate = canvas.coords(self.img)
            if self.fly_koordinate[1] <= 200:
                canvas.coords(self.img, self.fly_koordinate[0], 200)
        elif self.fly == False:
            canvas.move(self.img, 0, 300)
            self.fly_koordinate = canvas.coords(self.img)
            if self.fly_koordinate[1] >= 500:
                canvas.coords(self.img, self.fly_koordinate[0], 500)
        self.fly = None


class Sjekira:
    def __init__(self):
        self.sjekira_image = PhotoImage(file="sjekira.png")
        self.slika_sjekira_lista = []
        for i in range(7):
            self.a = random.randint(50, 750)
            self.b = random.randint(50, 450)
            self.slika_sjekira = canvas.create_image(
                self.a, self.b, image=self.sjekira_image, anchor=S)
            self.slika_sjekira_lista.append(self.slika_sjekira)

    def kretanje_sjekire(self):
        xVelocity = -1
        for sjekira_slika in self.slika_sjekira_lista:
            canvas.move(sjekira_slika, xVelocity, 0)
            root.update()


def check_collision():
    vampir_bbox = canvas.bbox(vampir.img)
    vampir_center_x = (vampir_bbox[0] + vampir_bbox[2]) / 2
    vampir_center_y = (vampir_bbox[1] + vampir_bbox[3]) / 2
    vampir_radius = min(
        (vampir_bbox[2] - vampir_bbox[0]) / 2, (vampir_bbox[3] - vampir_bbox[1]) / 2)

    for axe.slika_sjekira in axe.slika_sjekira_lista:
        sjekira_bbox = canvas.bbox(axe.slika_sjekira)
        sjekira_center_x = (sjekira_bbox[0] + sjekira_bbox[2]) / 2
        sjekira_center_y = (sjekira_bbox[1] + sjekira_bbox[3]) / 2
        sjekira_radius = min(
            (sjekira_bbox[2] - sjekira_bbox[0]) / 2, (sjekira_bbox[3] - sjekira_bbox[1]) / 2)

        distance = ((vampir_center_x - sjekira_center_x) ** 2 +
                    (vampir_center_y - sjekira_center_y) ** 2) ** 0.5
        tolerance = 0
        if canvas.coords(vampir.img)[1] == canvas.coords(axe.slika_sjekira)[1]:
            tolerance = -25
        elif canvas.coords(vampir.img)[1] > canvas.coords(axe.slika_sjekira)[1]:
            tolerance = -18
        elif canvas.coords(vampir.img)[1] < canvas.coords(axe.slika_sjekira)[1]:
            tolerance = -18
        if distance <= (vampir_radius + sjekira_radius + tolerance):
            print("Collision detected!")
            vampir.sudar = True


def check_bounds():
    if canvas.coords(vampir.img)[0] > 800:
        canvas.coords(vampir.img, 50, canvas.coords(vampir.img)[1])
        vampir.bounds = True
    if canvas.coords(vampir.img)[0] < 50:
        canvas.coords(vampir.img, 50, canvas.coords(vampir.img)[1])


def reset_axes():
    global axe
    if vampir.bounds == True:
        axe = Sjekira()
        vampir.bounds = False


def game_over():
    if vampir.sudar == True:
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('consolas', 70), text="GAME OVER", fill="red")
        vampir.sudar = False
        os.system("cls")


root = tk.Tk()
root.geometry("800x500+{}+{}".format(
    int(root.winfo_screenwidth()/2 - 200), int(root.winfo_screenheight()/2 - 100)))
root.title("Vampir")
root.resizable(False, False)
root.iconbitmap("vampir_icon.ico")

canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()

vampir = Vampir()
axe = Sjekira()

root.bind("<Right>", vampir.right)

root.bind("<Left>", vampir.left)

root.bind("<space>", vampir.jump)

root.bind("<KeyRelease-space>", vampir.fall)

root.bind("<Up>", vampir.up_press)

root.bind("<Down>", vampir.down_press)


def obicni_skok_loop():
    vampir.obicni_skok()
    root.after(91, obicni_skok_loop)


def fly_loop():
    vampir.flying()
    root.after(91, fly_loop)


def kretanje_sjekire_loop():
    axe.kretanje_sjekire()
    root.after(10, kretanje_sjekire_loop)


def collision_detection_loop():
    check_collision()
    root.after(10, collision_detection_loop)


def check_bounds_loop():
    check_bounds()
    root.after(10, check_bounds_loop)


def reset_axes_loop():
    reset_axes()
    root.after(10, reset_axes_loop)


def game_over_loop():
    game_over()
    root.after(10, game_over_loop)


obicni_skok_loop()

fly_loop()

kretanje_sjekire_loop()

collision_detection_loop()

check_bounds_loop()

reset_axes_loop()

game_over_loop()

root.mainloop()
