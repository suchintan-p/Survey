import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image 
import tkinter.font as font
from pathlib import Path
import os
import time
import csv
from loginreg import loginreg

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
class Test():
    def __init__(self):
        self.login=loginreg()
        self.username=self.login.username1        
        print(self.username)
        #self.username='Suchi'
        self.root = tk.Tk()
        ap=FullScreenApp(self.root)
        self.root.title("Survey")
        #self.text = tk.StringVar()
        try:
            self.resultFile = open("output.csv",'a')
            self.wr = csv.writer(self.resultFile, dialect='excel')
        except PermissionError:
            self.label = tk.Label(self.root, text="Error:Close the excel file and start again")
            self.label.pack()
            self.myf=font.Font(size=20)
            self.label['font']=self.myf
            self.label.place(x=500,y=300)
            self.root.mainloop()
        self.myf=font.Font(size=20) 


        self.answers=[] 
        string=self.username
        if len(string): 
            self.answers.append(string)
        if string=="":
            self.exit()
        print(string)
        self.button1 = tk.Button(self.root,
                                text="Color Survey",
                                command=self.startsurvey2)
        

        self.button1.pack()
        self.button1.place(x=600,y=300)          
        self.button1['font']=self.myf
        '''self.button2 = tk.Button(self.root,
                                text="Timepass",
                                command=self.startsurvey1)
        

        self.button2.pack()
        self.button2.place(x=600,y=400)          
        self.button2['font']=self.myf'''
        self.button3 = tk.Button(self.root,
                                text="Facial Expressions",
                                command=self.startsurvey3)
        

        self.button3.pack()
        self.button3.place(x=600,y=500)          
        self.button3['font']=self.myf
        '''img = ImageTk.PhotoImage(Image.open(self.files[0]).resize((1920,1080), Image.ANTIALIAS))
        self.panel1 = tk.Label(self.root, image=img)
        self.panel1.pack() '''

        self.check_staus()
        self.root.mainloop() 
    def exit(self):
        self.root.destroy()
        print("Invalid Login")       
    def getimageset(self):
        paths = Path('Pics').glob('**/*.jpg')
        print(paths)
        for path in paths:
    # because path is object not string
            path_in_str = str(path)
            # Do thing with the path
            print(path_in_str)
        
    def ShowChoice(self):
        print(self.v.get())
    def save_response(self):
        self.answers.append((self.v.get()))
    def startsurvey2(self):        
        for widget in self.root.winfo_children():
               widget.destroy()
        self.progress = Progressbar(self.root,
              length = 1000, mode = 'determinate') 
        self.progress.pack(pady = 10)
        path=os.getcwd()
        npath=path+"\Pics"
        self.files=[]
        for (dirpath, dirnames, filenames) in os.walk(npath):
            self.files.extend(filenames)
            break

        #print(f)
        os.chdir(npath)
        self.answers.append(2)       
        self.tic=time.time()        
        #file=open(r"questions.txt","r")
        self.question_set=self.files
        self.num_questions=len(self.files)
        self.up=100/self.num_questions
       # self.getimageset()
        self.count=1
               
        self.myf=font.Font(size=18) 
        img = ImageTk.PhotoImage(Image.open(self.files[0]).resize((500,400), Image.ANTIALIAS))
        self.panel = tk.Label(self.root, image=img,width=800,bd=10,relief='groove')
        self.panel.image = img
        self.panel.pack()
        #self.panel.place(x=600,y=400)              
        self.v = tk.IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python

        emotions = [
            ("Happy,joy,Peaceful,love,trust",1),
            ("Anger,intimidating,frustration,rage,aggression",2),
            ("Fear,tension,stress,submissive",3),
            ("Disgust,repulsion,boredom",4),
            ("Sad,mournful,grief,remorse",5)
        ] 
        self.colors={
        0:"red",
        1:"blue",
        2:"green",
        3:"black",
        4:"orange",
        5:"yellow",
        6:"magenta",
        }
        prompt=tk.Label(self.root, 
                 text="""Choose the category that best describes your feelings regarding this picture""",
                 justify = tk.LEFT,
                 padx = 20)
        prompt.pack()
        prompt['font']=self.myf
        self.rad=[]
        for val, emotion in enumerate(emotions):
            
            self.rad.append(tk.Radiobutton(self.root, 
                          text=emotion[0],
                          padx = 20, 
                          variable=self.v, 
                          command=self.ShowChoice,
                          value=val,indicatoron=False,
                          overrelief='sunken',height=1,activebackground="red",bd=4
                          ))
            self.rad[val].pack(anchor=tk.W)
            self.rad[val]['font']=self.myf
            self.rad[val].place(x=200,y=500+(val*60))


        self.ques=tk.Button(self.root,
                                text="Next",
                                command=lambda *args: self.changeText(),justify=tk.LEFT,overrelief='sunken')  
        self.ques.pack()
        self.ques.place(x=1100,y=730)
        self.myf=font.Font(size=20)
        self.ques['font']=self.myf        
    def open_img(self,x):           
        img2 = ImageTk.PhotoImage(Image.open(x).resize((500,400), Image.ANTIALIAS))
        self.panel.configure(image=img2)
        self.panel.image = img2
    def changeText(self):  
        self.save_response() 
        if self.count>=self.num_questions:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.toc=time.time()
            if self.toc-self.tic>70:
                self.label = tk.Label(self.root, text="Thank You!!")                
                self.wr.writerow(self.answers)
                self.resultFile.close()
                self.update_status(2)
                print(self.answers)
            else:
                self.label = tk.Label(self.root, text="Please take this survey seriously")
            self.label.pack()
            self.myf=font.Font(size=20)
            self.label['font']=self.myf
            self.label.place(x=650,y=350)                 
        self.open_img(self.question_set[self.count])
        self.progress['value']=self.up*self.count
        self.root.update_idletasks()
        self.count+=1
        for rb in self.rad:
            rb.configure(activebackground=self.colors[(self.count-1)%7])
        
    def startsurvey1(self):        
        self.button1.destroy()
        #self.button2.destroy()
        self.button3.destroy()
        self.progress = Progressbar(self.root,
              length = 1000, mode = 'determinate') 
        self.progress.pack(pady = 10)
        self.file=open("questions.txt","r")
        self.myf=font.Font(size=20)        
        self.tic=time.time()        
        #file=open(r"questions.txt","r")
        self.question_set=self.file.readlines()
        self.num_questions=len(self.question_set)
        self.up=600/self.num_questions
       # self.getimageset()
        self.answers.append(1)
        self.count=1              
        self.myf=font.Font(size=18) 
        for i in range(self.num_questions):
            self.question_set[i]=self.question_set[i].strip('\n')
        tk.Label(self.root).pack()
        tk.Label(self.root,height=5).pack()
        #img = ImageTk.PhotoImage(Image.open(self.files[1]).resize((500,400), Image.ANTIALIAS))
        self.panel = tk.Label(self.root, text=self.question_set[0],width=50,height=3,bd=10,relief='groove')
        #self.panel.image = img
        self.panel.pack()
        self.panel['font']=self.myf
        #self.panel.place(x=400,y=0)              
        self.v = tk.IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python
       
        self.emotions = [
            (self.question_set[1],1),
            (self.question_set[2],2),
            (self.question_set[3],3),
            (self.question_set[4],4),
            (self.question_set[5],5)
        ] 
        self.colors={
        0:"red",
        1:"blue",
        2:"green",
        3:"black",
        4:"orange",
        5:"yellow",
        6:"magenta",
        }
        prompt=tk.Label(self.root, 
                 text="""Choose the most appropriate option""",
                 justify = tk.LEFT,
                 padx = 20)
        prompt.pack()
        prompt['font']=self.myf
        
        self.rad=[]
        for val, emotion in enumerate(self.emotions):
            
            self.rad.append(tk.Radiobutton(self.root, 
                          text=emotion[0],
                          padx = 20,
                          pady=10, 
                          variable=self.v, 
                          anchor=tk.W,
                          command=self.ShowChoice,
                          value=val,indicatoron=False,
                          overrelief='sunken',height=1,activebackground="red",bd=4
                          ))
            self.rad[val].pack(anchor=tk.W)
            self.rad[val]['font']=self.myf
            self.rad[val].place(x=250,y=300+(val*85))


        self.ques=tk.Button(self.root,
                                text="Next",
                                command=lambda *args: self.changeTextq(),justify=tk.LEFT,overrelief='sunken')  
        self.ques.pack()
        self.ques.place(x=1100,y=700)
        self.myf=font.Font(size=20)
        self.ques['font']=self.myf        
    def open_que(self,x):           
        self.panel.configure(text=x)
    def update_status(self,i):
        path=os.getcwd()
        path=path.strip("/Pics")
        path=path.strip("/Exps")
        self.npath=path+"/Users"
        file = open(self.npath+"/"+self.username, "a")
        file.write("\n"+str(i))
        file.close()
    def check_staus(self):
        path=os.getcwd()
        self.npath=path+"/Users"
        file = open(self.npath+"/"+self.username, "r")
        verify = file.read().splitlines()
        self.stat=[int(x) for x in verify[2:]]
        print(self.stat)
        temp=self.myf;
        self.myf=font.Font(size=15)
        if 1 in self.stat:
            self.button2['state']='disabled'
            lab=tk.Label(self.root,text="COMPLETED!",fg='green')
            lab.pack()
            lab.place(x=800,y=402)
            lab['font']=self.myf
        if 2 in self.stat:
            self.button1['state']='disabled'
            lab=tk.Label(self.root,text="COMPLETED!",fg='green')
            lab.pack()
            lab.place(x=800,y=305)
            lab['font']=self.myf
        if 3 in self.stat:
            self.button3['state']='disabled' 
            lab=tk.Label(self.root,text="COMPLETED!",fg='green')
            lab.pack()
            lab.place(x=870,y=505)
            lab['font']=self.myf
        file.close()
        self.myf=temp
    def changeTextq(self):  
        self.save_response() 

        if self.count*6>=self.num_questions:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.toc=time.time()
            if self.toc-self.tic>(self.num_questions)/6:
                self.label = tk.Label(self.root, text="Thank You!!") 
                self.label.pack()  
                self.myf=font.Font(size=20)
                self.label['font']=self.myf
                self.label.place(x=700,y=350)              
                self.wr.writerow(self.answers)
                self.resultFile.close()
                self.update_status(1)
                print(self.answers) 
            else:
                self.label = tk.Label(self.root, text="Please take this survey seriously")
                self.label.pack()
                self.myf=font.Font(size=20)
                self.label['font']=self.myf
                self.label.place(x=600,y=350)                
        self.open_que(self.question_set[self.count*6])
        self.progress['value']=self.up*self.count
        self.root.update_idletasks()
        self.emotions = [
            (self.question_set[self.count*6+1],1),
            (self.question_set[self.count*6+2],2),
            (self.question_set[self.count*6+3],3),
            (self.question_set[self.count*6+4],4),
            (self.question_set[self.count*6+5],5)
        ]
        for val, emotion in enumerate(self.emotions):
            
           self.rad[val].configure(text=emotion[0])

        self.count+=1
        for rb in self.rad:
            rb.configure(activebackground=self.colors[(self.count-1)%7])
    def startsurvey3(self):        
        self.button1.destroy()
        #self.button2.destroy()
        self.button3.destroy()
        self.progress = Progressbar(self.root,
              length = 1000, mode = 'determinate') 
        self.progress.pack(pady = 10)
        path=os.getcwd()
        self.file=open("options.txt","r")
        #self.file2=open("explanations.txt","r")
        self.options=self.file.readlines()
        #self.explanations=self.file2.readlines()
        npath=path+"\Exps"
        self.files=[]
        for (dirpath, dirnames, filenames) in os.walk(npath):
            self.files.extend(filenames)
            break
        self.bpath=path+"\Texts"
        self.tfiles=[]
        for (dirpath, dirnames, filenames) in os.walk(self.bpath):
            self.tfiles.extend(filenames)
            break
        #print(f)
        os.chdir(npath)
        self.answers.append(3)       
        self.tic=time.time()        
        #file=open(r"questions.txt","r")
        self.question_set=self.files
        self.num_questions=len(self.files)
        self.up=100/self.num_questions
       # self.getimageset()
        self.answers.append(1)
        self.count=1  
        self.score=0            
        self.myf=font.Font(size=18) 
        for i in range(self.num_questions*5):
            self.options[i]=self.options[i].strip('\n')        
        img = ImageTk.PhotoImage(Image.open(self.files[0]).resize((500,400), Image.ANTIALIAS))
        self.panel = tk.Label(self.root, image=img,width=800,bd=10,relief='groove')
        self.panel.image = img
        self.panel.pack()
        #self.panel.place(x=600,y=400)              
        self.v = tk.IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python

        self.optionss = [
            (self.options[0],1),
            (self.options[1],2),
            (self.options[2],3),
            (self.options[3],4)
        ] 
        self.colors={
        0:"red",
        1:"blue",
        2:"green",
        3:"black",
        4:"orange",
        5:"yellow",
        6:"magenta",
        }
        prompt=tk.Label(self.root, 
                 text="""Choose the category that best describes this facial expression""",
                 justify = tk.LEFT,
                 padx = 20)
        prompt.pack()
        prompt['font']=self.myf
        self.rad=[]
        for val, option in enumerate(self.optionss):
            
            self.rad.append(tk.Radiobutton(self.root, 
                          text=option[0],
                          padx = 20, 
                          variable=self.v, 
                          command=self.ShowChoice,
                          value=val,indicatoron=False,
                          overrelief='sunken',height=1,activebackground="red",bd=4
                          ))
            self.rad[val].pack(anchor=tk.W)
            self.rad[val]['font']=self.myf
            self.rad[val].place(x=200,y=500+(val*60))


        self.ques=tk.Button(self.root,
                                text="Next",
                                command=self.changeText3,justify=tk.LEFT,overrelief='sunken')  
        self.ques.pack()
        self.ques.place(x=1100,y=730)
        self.myf=font.Font(size=20)
        self.ques['font']=self.myf        
    def open_img(self,x):           
        img2 = ImageTk.PhotoImage(Image.open(x).resize((500,400), Image.ANTIALIAS))
         
        self.panel.configure(image=img2)
        self.panel.image = img2
    def check_response(self):
        if(int(self.options[self.count*5-1])==self.v.get()):
            return True
        return False
    def destroyres(self):
        self.result_screen.destroy()
    def passtime(self,x):
        print(x)
    def display_result(self,res):
        self.result_screen=tk.Toplevel(self.root)
        self.result_screen.title("Explanation")
        self.result_screen.geometry("570x560+500+200")
        img = ImageTk.PhotoImage(Image.open(self.question_set[self.count-1]).resize((350,250), Image.ANTIALIAS))
        panel = tk.Label(self.result_screen, image=img,width=450,bd=10,relief='groove')
        panel.image = img
        panel.pack()
        tk.Label(self.result_screen,text="Your Answer: "+self.optionss[self.v.get()][0]+"     Correct Answer: "+self.optionss[int(self.options[self.count*5-1])][0],font=("Calibri", 12)).pack()
        if(res):
            tk.Label(self.result_screen,text="Correct",font=("Calibri", 12),fg="green").pack()
            self.score+=1
        else:
            tk.Label(self.result_screen,text="Wrong",font=("Calibri", 12),fg="red").pack()
        fil=open(self.bpath+"\\"+self.tfiles[self.count-1],"r")
        self.explanations=fil.readlines()
        for x in self.explanations:
            x=x.strip('\n')
            tk.Label(self.result_screen,text=x,font=("Calibri", 11)).pack(anchor=tk.W)        
        tk.Button(self.result_screen,text="Next Question",font=("Calibri", 12),command=self.destroyres).pack()

    def changeText3(self):  
        self.save_response() 
        res=self.check_response()
        self.display_result(res)
        self.result_screen.after(15000, self.destroyres)
        self.root.bind('<KeyPress>', self.passtime)
        if self.count>=self.num_questions:
            for widget in self.root.winfo_children():
                if widget==self.result_screen:
                    continue
                widget.destroy()
            self.toc=time.time()
            self.answers.append(self.score)
            self.label = tk.Label(self.root, text="Your Score is "+str(self.score)+"/"+str(self.num_questions)+"\n\nThank You!!")                
            self.wr.writerow(self.answers)
            self.resultFile.close()
            self.update_status(3)
            print(self.answers)
            self.label.pack()
            self.myf=font.Font(size=20)
            self.label['font']=self.myf
            self.label.place(x=650,y=350)

        self.open_img(self.question_set[self.count])
        self.progress['value']=self.up*self.count
        self.root.update_idletasks()
        self.optionss = [
            (self.options[self.count*5],1),
            (self.options[self.count*5+1],2),
            (self.options[self.count*5+2],3),
            (self.options[self.count*5+3],4),
        ]
        for val, emotion in enumerate(self.optionss):
            
           self.rad[val].configure(text=emotion[0])
        self.count+=1
        for rb in self.rad:
            rb.configure(activebackground=self.colors[(self.count-1)%7])
        
app=Test()
