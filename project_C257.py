from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers
Label(frame,text="Account Number 1 : ",fg="black",bg="white").grid(row=0,column=0,sticky=W,pady=10)
Label(frame,text="Account Number 2 : ",fg="black",bg="white").grid(row=1,column=0,sticky=W,pady=10)
Label(frame,text="Account Number 3: ",fg="black",bg="white").grid(row=2,column=0,sticky=W,pady=10)
Label(frame,text=" Account Number 4: ",fg="black",bg="white").grid(row=3,column=0,sticky=W,pady=10)
Label(frame,text="Account Number 5: ",fg="black",bg="white").grid(row=4,column=0,sticky=W,pady=10)








#Create entry elements to get the use input for account addresses
Account1=Entry(frame)
Account2=Entry(frame)
Account3=Entry(frame) 
Account4=Entry(frame) 
Account5=Entry(frame)  






#place the entry elements on the root window
Account1.grid(row=0,column=1,padx=20,pady=10)
Account2.grid(row=1,column=1,padx=20,pady=10)
Account3.grid(row=2,column=1,padx=20,pady=10)
Account4.grid(row=3,column=1,padx=20,pady=10)
Account5.grid(row=4,column=1,padx=20,pady=10)






#create the text box
result=Text(root,height=10,width=45,bg="white")

#define a function CHECK_BALANCE() and add the code inside it.
def CHECK_BALANCE():
	ANO=[]
	ANO.append(Account1.get())
	ANO.append(Account2.get())
	ANO.append(Account3.get())
	ANO.append(Account4.get())
	ANO.append(Account5.get())
	count=1
	for i in ANO:
		balance=web3.eth.get_balance(i)
		balance=balance*0.0000000000000001
		result.insert(END,f'Account{count} balance{balance}\n')
		count=count+1

    
   
  
    

        
      

frame.pack()

#Create a button element to call the CHECK_BALANCE()
cb=Button(root,width=15,text='CHECK BALANCE',command=CHECK_BALANCE,highlightbackground="white")
cb.pack()


    

result.pack(pady=5)
root.mainloop()

