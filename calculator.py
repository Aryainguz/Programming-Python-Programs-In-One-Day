from tkinter import *
import math
import mpmath

root = Tk()
root.title('This is a scientific calculator made by Aryan, Arpita Sambher, Aryan Gupta')
root.iconbitmap(r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")   # r make a normal string to path withou r / will be a string not a backslashh for path

# r Means 'Raw String'
# Normally, Python uses backslashes as escape characters. Prefacing the string definition with 'r' is a useful way to define a string where you need the backslash to be an actual backslash



root.geometry('550x700')

e = Entry(root,width='55',borderwidth='5')  
e.grid(row=0,column=0,columnspan=3,padx=20,pady=15)

def b_click(number):

            # e.delete(0,END)   # this deletes what already is in the input box

            pre = str(e.get())       # get() stores or gets whatever entered preivously

            e.delete(0, END)  
            # the arguments inside .delete() tells index note-: first argument is cumpolsory 2nd i optional 
            # this is to add new number eg-: first we click 1 then click 2 it will give 121 not 12 to only add number without previous number we use e.delete() so we get 12 not 112  
            
            e.insert(0,str(pre) +str(number))

# firstly when clicking any number e.get() will get nothing and e.insert() will make e the first number clicked 

# then on clicking 2nd number, e.get() stores previous number and then deletes it in e but stores in e.get() and e.insert will give previous numbers(stored in e.get() but not displayed on e) + new number clicke this cycle goes on until not clicked anything
 


            # note that 0 means 0th index i.e it will input at 0th index
            # we use str so +  only numbers in characters and not actualyy add numbers eg 1+1 be 11 not 2
            # to convert number in string we can write '1' insrtead of 1 in parenthesis in command b_click()

def clear():
    e.delete(0,END)

def add():
    sum =  e.get()    # this is storing ist number
    global ans      # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math           # math here is variable
    math = 'addition'
    ans =int(sum)
    e.delete(0,END)

def sub():
    sum =  e.get()
    global ans      # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math     # we need to use global again because to change value of math we need it to be a variable in this def function aswell
    math = 'subtraction'
    ans =int(sum)
    e.delete(0,END)

def mul():
    sum =  e.get()
    global ans      # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math
    math = 'multiplication'
    ans =int(sum)
    e.delete(0,END)

def div():
    sum =  e.get()
    global ans      # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math
    math = 'divison'
    ans =int(sum)
    e.delete(0,END)

def exp():
    sum =  e.get()
    global ans      # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math
    math = 'exponential'
    ans =int(sum)
    e.delete(0,END)

def mod():
    sum =  e.get()
    global ans     # we are doing this because addition is not a global variable and to use it in equal to button we do this
    global math      
    math = 'modoulas'
    ans =int(sum)
    e.delete(0,END)
  
def equal():
    answer = e.get()             # this is storing or getting 2nd number
    e.delete(0,END)

    if math == 'addition':
        e.insert(0, ans + int(answer))      # we could only use addition variable here because we made it a global variable 
                                               # 0 means we are inserting at 0th index
                                            # here we don't use global because we are not changing value of math here but using it only

    if math == 'subtraction':
        e.insert(0, ans - int(answer))      # first number is ans and 2nd number is answer
    if math == 'multiplication':
        e.insert(0, ans * int(answer))
    if math == 'division':
        e.insert(0, ans / int(answer))
    if math == 'exponential':
        e.insert(0, ans ** int(answer))
    if math == 'modoulas':
        e.insert(0, ans % int(answer))
    
    

           
    
# defining buttons

# we used lambda because inside command we can't use function (defined earlier) with parameters inside parenthesis

x1=Button(root, text='1',padx=40,pady=20, command=lambda: b_click(1),border=3)   
x2=Button(root, text='2',padx=40,pady=20, command=lambda: b_click(2),border=3)
x3=Button(root, text='3',padx=40,pady=20, command=lambda: b_click(3),border=3)
x4=Button(root, text='4',padx=40,pady=20, command=lambda: b_click(4),border=3)
x5=Button(root, text='5',padx=40,pady=20, command=lambda: b_click(5),border=3)
x6=Button(root, text='6',padx=40,pady=20, command=lambda: b_click(6),border=3)
x7=Button(root, text='7',padx=40,pady=20, command=lambda: b_click(7),border=3)
x8=Button(root, text='8',padx=40,pady=20, command=lambda: b_click(8),border=3)
x9=Button(root, text='9',padx=40,pady=20, command=lambda: b_click(9),border=3)
x0=Button(root, text='0',padx=40,pady=20, command=lambda: b_click(0),border=3)
xadd=Button(root, text='+',padx=39,pady=20, command=add,border=3)
xsub=Button(root, text='-',padx=39,pady=20, command=sub,border=3)
xmul=Button(root, text='*',padx=39,pady=20, command=mul,border=3)
xdiv=Button(root, text='/',padx=39,pady=20, command=div,border=3)
xexp=Button(root, text='**',padx=39,pady=20, command=exp,border=3)
xmod=Button(root, text='%',padx=39,pady=20, command=mod,border=3)
xsin = Button(root, text='sin',padx=39,pady=20,command=add,border=3)
xcos = Button(root, text='cos',padx=39,pady=20,command=add)
xtan = Button(root, text='cos',padx=39,pady=20,command=add)
xcot = Button(root, text='cos',padx=39,pady=20,command=add)
xsec = Button(root, text='cos',padx=39,pady=20,command=add)
xcosec = Button(root, text='cos',padx=39,pady=20,command=add)
xlog = Button(root, text='cos',padx=39,pady=20,command=add)


xc = Button(root, text='c',padx=39,pady=20, command=add,border=3)
xequal=Button(root, text='=',padx=103,pady=20, command=equal,border=3)
xclear=Button(root, text='Clear',padx=93,pady=20, command=clear,border=3)


# Putting buttons on screen 

x7.grid(row=3,column=0)
x8.grid(row=3,column=1)
x9.grid(row=3,column=2)

x4.grid(row=2,column=0)
x5.grid(row=2,column=1)
x6.grid(row=2,column=2)
x1.grid(row=1,column=0)
x2.grid(row=1,column=1)
x3.grid(row=1,column=2)
x0.grid(row=4,column=0)

xadd.grid(row=6,column=0)
xsub.grid(row=6,column=1)
xmul.grid(row=6,column=2)
xdiv.grid(row=7,column=0)
xexp.grid(row=7,column=1)
xmod.grid(row=7,column=2)
xsin.grid(row=8,column=0)

xc.grid(row=5,column=0)
xequal.grid(row=5,column=1,columnspan=2)
xclear.grid(row=4,column=1,columnspan=2)




root.mainloop()
