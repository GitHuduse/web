import tkinter as tk
import tkinter.messagebox as msg
import random
import os
diao = random.randint(1, 2)
class Application(tk.Tk):
    global diao
    def __init__(self):
        super().__init__()
        self.title("sb唐睦程")
        self.resizable(False,False)
        self.windget()
    def windget(self):
        tk.Label(self,text="给唐睦程做绝育").pack()
        tk.Button(self,text="开始手术",command=self.start).pack()
    def start(self):
        if diao == 1:
            msg.showinfo("sb唐睦程","绝育成功")
        else:
            msg.showerror("sb唐睦程","绝育失败：他死了")
        os.system(f"start pythonw {__file__}")
        self.quit()
if __name__=='__main__':
    app = Application()
    app.mainloop()