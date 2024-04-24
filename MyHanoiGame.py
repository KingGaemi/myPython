import tkinter as tk
from tkinter import messagebox
import string
import time


# Rods name for 'A,B,C ~...'
uppercase_alphabet = list(string.ascii_uppercase)


colors = ['red','orange','yellow','green','blue', 'navy', 'purple', 'black']



class ButtonHandler():
    def __init__(self, root, hanoi_instance):
        self.root = root
        self.previous_button = None
        self.buttons = []
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side='bottom')
        self.hanoi = hanoi_instance
        self.count = 0  
        self.label = tk.Label(root, text =str(self.count))
        self.label.pack(side='bottom')
        self.log = []


    def creat_button(self, button_name):

        button = tk.Button(self.button_frame, text=button_name, command=lambda x=button_name : self.on_button_clicked(x), width=12, height=5)
        button.pack(side='left')

    def creat_autoMode(self):
        button = tk.Button(root, text='AutoMode', command = lambda : self.start_auto(), width=12, height=5)
        button.pack(side='bottom')

    def start_auto(self):
        print("Start auto")
        self.hanoi.reset()
        self.log = []
        self.count = 0
        self.autoMove(5,'A','B','C')
        print("Show Move")
        self.showMove()
          

    def autoMove(self, n, source, auxiliary, target):
        if n <= 0:
            
            return
      
        self.autoMove(n - 1, source, target, auxiliary)

        self.hanoi.rods[target].append(self.hanoi.rods[source].pop())
        self.log.append(source)
        self.log.append(target)
        self.autoMove(n - 1, auxiliary, source, target)

        

    def showMove(self):
        print(self.log)
        self.hanoi.reset()
        for i, rod in enumerate(self.log):
            self.root.after(100 * i, lambda x=rod: self.on_button_clicked(x) )
           
            
            



    def on_button_clicked(self, current_button):
        # print(f'Button {current_button} clicked!')
        if self.previous_button:
            #print(f'Previous Button is {self.previous_button}')
            #print(f'Current Button is {current_button}')
            if self.hanoi.move(self.previous_button, current_button):
                if self.previous_button != current_button:
                    self.count += 1
                    self.label.config(text=str(self.count))
                    # Check if the game end
                    if len(self.hanoi.rods['C']) == self.hanoi.number_of_rings:
                        if self.count == 2 ^ self.hanoi.number_of_rings - 1:
                            messagebox.showinfo("Congratulations!", "You have perfectly completed the Tower of Hanoi!")
                        else:
                            messagebox.showinfo("Congratulations!", "You have completed the Tower of Hanoi!")
                        self.log = []
                self.previous_button = None
                
        else:
            if not self.hanoi.rods[current_button]:
                return
            self.previous_button = current_button
            self.hanoi.pickUp(current_button)




class Hanoi():
    
    def __init__(self, number_of_rings, canvas):
        self.number_of_rings = number_of_rings
        self.anchor_x = 50
        self.anchor_y = 110
        self.canvas = canvas
        self.rings = []
        self.rods = {
                    'A' : list(range(number_of_rings)),
                    'B' : [],
                    'C' : []
                }

    def drawHanoi(self):

        #draw rods
        self.canvas.create_rectangle((self.anchor_x + 90), 50, (self.anchor_x + 100), 200, fill="brown")
        self.canvas.create_rectangle((self.anchor_x + 390), 50,(self.anchor_x + 400), 200, fill="brown")
        self.canvas.create_rectangle((self.anchor_x + 690), 50,(self.anchor_x + 700), 200, fill="brown")

        #draw rings
        for i in range(self.number_of_rings):
          ring = self.canvas.create_rectangle(
                                    self.anchor_x + 80 - i*20 ,
                                    self.anchor_y + (80- 20*self.number_of_rings) + 20 + i*20,
                                    self.anchor_x + 110 + i*20,
                                    self.anchor_y + (80- 20*self.number_of_rings) + 40 + i*20, fill=f"{colors[i]}")
          self.rings.append(ring)

    def reDrawHanoi(self):
        print("Current state:\n", self.rods)
        for j, rod  in enumerate(['A', 'B', 'C']):
            for i, ring in enumerate(self.rods[rod]):
                self.canvas.coords(self.rings[ring],
                                    self.anchor_x + 80 - ring*20 + j*300,
                                    self.anchor_y + (80- 20*len(self.rods[rod])) + 20 + i*20,
                                    self.anchor_x + 110 + ring*20 + j*300,
                                    self.anchor_y + (80- 20*len(self.rods[rod])) + 40 + i*20)

    def pickUp(self,rod):
        if self.rods[rod]:
            self.canvas.move(self.rings[self.rods[rod][0]], 0, -20)

    def reset(self):
        self.rods['A'] = list(range(self.number_of_rings))
        self.rods['B'] = []
        self.rods['C'] = []
        self.reDrawHanoi()

    def move(self, start, target):
        
        if start != target and self.rods[start]:
            if not self.rods[target] or self.rods[target][0] > self.rods[start][0]:
                self.rods[target].insert(0, self.rods[start].pop(0))
                self.reDrawHanoi()
                return True
            else:
            #   print(f'{self.rods[start][0]}to {self.rods[target][0]}')
                print("Can't do that")
                return False
        else:
            self.reDrawHanoi()
            return True
        


    

root = tk.Tk()
root.title("My Hanoi Tower Game")
canvas = tk.Canvas(root, width=900, height=300)
canvas.pack()

myHanoi = Hanoi(number_of_rings = 5, canvas=canvas)
myHanoi.drawHanoi()


handler = ButtonHandler(root, myHanoi)


button_names = ['A', 'B', 'C']
for name in button_names:
    handler.creat_button(name)
handler.creat_autoMode()

#print(myHanoi.rings)
# handler.autoMove(5, 'A','B','C')



root.mainloop()


