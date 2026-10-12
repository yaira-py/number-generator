import tkinter as tk
from tkinter import messagebox
import random

class RandomNumGen:
    def __init__(self,root):
        self.root=root
        self.root.title('Number Generator')
        self.root.geometry('450x450')

        self.title_lb =tk.Label(self.root,text='Random Number Generator',font=('Arial',14,'bold'),fg='#333333')
        self.title_lb.pack(pady=10)

        self.res_box=tk.Button(self.root,text=' ',font=('Arial',14,'bold'),bg='white',fg='#333333',justify='center',bd=1,relief='solid')
        self.res_box.pack(pady=20)

        self.min_frame=tk.Frame(self.root)
        self.min_frame.pack(pady=10)

        self.min_lb=tk.Label(self.min_frame,text='Minimum: ',font=('Arial',15,))
        self.min_lb.pack(side='left')

        self.min_entry=tk.Entry(self.min_frame,width=8,justify='center',bd=1,relief='solid')
        self.min_entry.insert(0,'1')
        self.min_entry.pack(side='left',ipady=4)

        self.max_frame=tk.Frame(self.root)
        self.max_frame.pack(pady=10)

        self.max_lb=tk.Label(self.max_frame,text='Miximum: ',font=('Arial',15))
        self.max_lb.pack(side='left')

        self.max_entry=tk.Entry(self.max_frame,width=8,justify='center',bd=1,relief='solid')
        self.max_entry.insert(0,'100')
        self.max_entry.pack(side='left',ipady=4)

        self.gen_btn=tk.Button(self.root,text='Generate',font=('Arial',15),bg="#4F8641",fg='white',command=self.generate)
        self.gen_btn.pack(pady=20)

        self.reset_btn=tk.Button(self.root,text='Reset',font=('Arial',15),bg="#BE3F1F",fg='white',command=self.reset)
        self.reset_btn.pack(pady=10)
        

    def generate(self):
        min=self.min_entry.get().strip()
        max=self.max_entry.get().strip()

        if min=='' or max=='':
            messagebox.showinfo('Invalid','pls enter values in both fields')
            return

        min_val=int(min)
        max_val=int(max)

        if min_val==1 and max_val==100:
            messagebox.showinfo('Invalid','pls enter new values')
            return

        if min_val>max_val:
            messagebox.showinfo('Inavlid','min value cant be greater than max')
            return

        num =random.randint(min_val,max_val)
        self.res_box.config(text= str(num),font=('Arial',17,'bold'))

        

    def reset(self):
        self.res_box.config(text='')

        self.min_entry.delete(0,tk.END)
        self.min_entry.insert(0,'1')

        self.max_entry.delete(0,tk.END)
        self.max_entry.insert(0,'100')





if __name__=='__main__':
    window= tk.Tk()
    app = RandomNumGen(window)
    window.mainloop()
