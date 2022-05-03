from tkinter import *
from add_user import *
from add_animal import *
from delete_animal import *

class main_page:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root.title("Main Page"),height=500,width=800,bg='dodgerblue3')

        self.f.propagate(0)

        self.f.pack()
        
#####
        #Heading
        self.n1=Label(text='Welcome to Zoo Management System',bg='dodgerblue3',font=('Arial Bold',25))
        self.n1.place(x=150,y=20)
        
        #Add Book Details button
        self.b_addBook=Button(text='Add Animal',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14),command=lambda: self.buttonclick(1))
        self.b_addBook.place(x=250,y=150)
#####
        #Delete Book button
        self.b_deleteBook=Button(text='Delete Animal ',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14),command=lambda: self.buttonclick(2))
        self.b_deleteBook.place(x=250,y=200)
        
        #View Book button
        self.b_bookList=Button(text='Vaccinated Animals',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14))
        self.b_bookList.place(x=250,y=250)
#####
        #Issue Book
        self.b_issueBook=Button(text='NA',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14))
        self.b_issueBook.place(x=250,y=300)
        
        #Return Book button
        self.b_returnBook=Button(text='Delete Employee',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14))
        self.b_returnBook.place(x=250,y=350)

        #Add users button
        self.b_returnBook=Button(text='Add Employee',fg='white',bg="dark red",width=25,height=1,font=('Calibri',14),command=lambda: self.buttonclick(0))
        self.b_returnBook.place(x=250,y=400)       


    def buttonclick(self,num):
        if(num==0):
            self.root.destroy()
            ad_us()
            cursor.close()
            conn.close()
        elif(num==1):
            self.root.destroy()
            ad_bk()
            cursor.close()
            conn.close()
        elif(num==2):
            self.root.destroy()
            dele()
            cursor.close()
            conn.close()
        else:
            self.root.destroy()          
            
def mp():
    root=Tk()

    mb=main_page(root)

    root.mainloop()
