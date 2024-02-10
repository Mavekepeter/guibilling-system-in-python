from tkinter import*
import random,os,tempfile
from tkinter import messagebox
import smtplib



# functionality part
def clear():
    bathsoapEntry.delete(0,END)
    facecreamlabelEntry.delete(0,END)
    facewashlabelEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgellabelEntry.delete(0,END)
    bodylotionEntry.delete(0,END)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheetEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)


    fantaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spritEntry.delete(0,END)
    MilkEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cococolaEntry.delete(0,END)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    textarea.delete(1.0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)


def send_email():
    def send_gmail():
        try:
          ob=smtplib.SMTP('smtp.gmail.com',465)
          ob.starttls()
          ob.login(senderEntry.get(),passwordEntry.get())
          Message=email_textarea.get(1.0,END)
          ob.sendmail(senderEntry.get(),receiverEntry.get(),Message)
          ob.quit()
          messagebox.showinfo('Success','Bill is sent successfully',parent=root1)
          root1.destroy()
        except:
            messagebox.showerror('error','Something went wrong please try again latter',parent=root1)


    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderframe=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderframe.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderframe,text="sender'semail",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordlabel=Label(senderframe,text="password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recepientframe=LabelFrame(root1,text='Recepient',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recepientframe.grid(row=1,column=0,padx=40,pady=20)

        receiverlabel=Label(recepientframe,text="Email address",font=('arial',14,'bold'),bg='gray20',fg='white')
        receiverlabel.grid(row=0,column=0,padx=10,pady=8)

        receiverEntry=Entry(recepientframe,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        receiverEntry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recepientframe,text="message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=8)
        email_textarea=Text(recepientframe,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=',''))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)
        root1.mainloop()

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('error','Bill is empty')
    else:
       file=tempfile.mktemp('.txt')
       open(file,'w').write(textarea.get(1.0,END))
       os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i .split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break


        else:
            messagebox.showerror('error','Invalid Bill number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'billnumber {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)



billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer details are required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No product selected please select product')
    elif cosmeticpriceEntry.get()=='0 Ksh' and grocerypriceEntry.get()=='0 Ksh' and drinkspriceEntry.get()=='0 Ksh':
       messagebox.showerror('Error','No product selected please select product')
    else:
        textarea.insert(END,'***Welcome Customer****')
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t***Welcome Customer****\n')
        textarea.insert(END,f'billnumber: {billnumber}')
        textarea.insert(END,f'\nCustomername: {nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomerphonenumber: {phoneEntry.get()}\n')
        textarea.insert(END,f'\n========================================\n')
        textarea.insert(END,'\nProduct\t\tQuantity\t\tPrice\n')
        textarea.insert(END,f'\n========================================\n')
    if bathsoapEntry.get()!='0':
        textarea.insert(END,f'Bath soap\t\t{bathsoapEntry.get()}\t\t{soapprice} Ksh')

    if hairsprayEntry.get()!='0':
        textarea.insert(END,f'\nhair spray\t\t{hairsprayEntry.get()}\t\t{hairsprayprice} Ksh\n')

    if facecreamlabelEntry.get()!='0':
        textarea.insert(END,f'\nface cream\t\t{facecreamlabelEntry.get()}\t\t{facecreamprice} Ksh\n')

    if hairgellabelEntry.get()!='0':
        textarea.insert(END,f'hairgel\t\t{hairgellabelEntry.get()}\t\t{hairgelprice} Ksh')

    if bodylotionEntry.get()!='0':
        textarea.insert(END,f'\nbodylotion\t\t{bodylotionEntry.get()}\t\t{bodylotionprice} Ksh\n')

    if facewashlabelEntry.get()!='0':
        textarea.insert(END,f'\nfacewash\t\t{facewashlabelEntry.get()}\t\t{facewashprice} Ksh\n')
     #Bill text for grocery
    if riceEntry.get()!='0':
        textarea.insert(END,f'\nrice\t\t{riceEntry.get()}\t\t{riceprice} Ksh\n')
    if oilEntry.get()!='0':
        textarea.insert(END,f'\noil\t\t{oilEntry.get()}\t\t{oilprice} Ksh\n')
    if daalEntry.get()!='0':
        textarea.insert(END,f'\ndaal\t\t{daalEntry.get()}\t\t{daalprice} Ksh\n')
    if sugarEntry.get()!='0':
        textarea.insert(END,f'\nsugar\t\t{sugarEntry.get()}\t\t{sugarprice} Ksh\n')
    if teaEntry.get()!='0':
        textarea.insert(END,f'\ntea\t\t{teaEntry.get()}\t\t{teaprice} Ksh\n')
    if wheetEntry.get()!='0':
        textarea.insert(END,f'\nwheet\t\t{wheetEntry.get()}\t\t{wheetprice} Ksh\n')

    #billing text area for drinks
    if fantaEntry.get()!='0':
        textarea.insert(END,f'\nfanta\t\t{fantaEntry.get()}\t\t{fantaprice} Ksh\n')
    if pepsiEntry.get()!='0':
        textarea.insert(END,f'\npepsi\t\t{pepsiEntry.get()}\t\t{pepsiprice} Ksh\n')
    if spritEntry.get()!='0':
        textarea.insert(END,f'\nsprit\t\t{spritEntry.get()}\t\t{spritprice} Ksh\n')
    if MilkEntry.get()!='0':
        textarea.insert(END,f'\nmilk\t\t{MilkEntry.get()}\t\t{milkprice} Ksh\n')
    if cococolaEntry.get()!='0':
        textarea.insert(END,f'\ncococola\t\t{cococolaEntry.get()}\t\t{cococolaprice} Ksh\n')
    if frootiEntry.get()!='0':
        textarea.insert(END,f'\nfrooti\t\t{frootiEntry.get()}\t\t{frootiprice} Ksh\n')
    textarea.insert(END,f'\n========================================\n')
    # billing for taxes
    if cosmetictaxEntry.get()!='0.0 Ksh':
        textarea.insert(END,f'\ncosmetictax\t\t{cosmetictaxEntry.get()}\n')
    if grocerytaxEntry.get()!='0.0 Ksh':
        textarea.insert(END,f'\ngrocerytax\t\t{grocerytaxEntry.get()}\n')
    if drinkstaxEntry.get()!='0.0 Ksh':
        textarea.insert(END,f'\ndrinkstax\t\t{drinkstaxEntry.get()}\n')
    textarea.insert(END,f'\ntotalbill\t\t{totalbill}\n')
    textarea.insert(END,f'\n========================================\n')  
    save_bill()
def total():
#cosmetic price calculation
    global soapprice
    global hairsprayprice
    global facecreamprice
    global hairgelprice
    global bodylotionprice
    global facewashprice
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamlabelEntry.get())*50
    facewashprice=int(facewashlabelEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgellabelEntry.get())*200
    bodylotionprice=int(bodylotionEntry.get())*250
    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairgelprice+hairsprayprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Ksh')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Ksh')


# grocery price calculation
    global riceprice
    global oilprice
    global daalprice
    global sugarprice
    global teaprice
    global wheetprice
    riceprice=int(riceEntry.get())*250
    oilprice=int(oilEntry.get())*230
    daalprice=int(daalEntry.get())*50
    sugarprice=int(sugarEntry.get())*200
    teaprice=int(teaEntry.get())*25
    wheetprice=int(wheetEntry.get())*210
    totalgroceryprice=riceprice+oilprice+daalprice+sugarprice+teaprice+wheetprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Ksh')
    grocerytax=totalgroceryprice*0.5
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{grocerytax} Ksh')
#cool drinks price calculations
    global fantaprice
    global pepsiprice
    global spritprice
    global milkprice
    global cococolaprice
    global frootiprice
    global totalbill
    fantaprice=int(fantaEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*40
    spritprice=int(pepsiEntry.get())*70
    milkprice=int(MilkEntry.get())*55
    cococolaprice=int(cococolaEntry.get())*45
    frootiprice=int(frootiEntry.get())*60
    totaldrinksprice=fantaprice+pepsiprice+spritprice+milkprice+cococolaprice+frootiprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Ksh')
    drinkstax=totaldrinksprice*0.12
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{drinkstax} Ksh')
    totalbill=totalcosmeticprice+totaldrinksprice+totalgroceryprice+cosmetictax+drinkstax+grocerytax

#gui part
root=Tk()
root.title('Retail billing system')
root.geometry('1287x650')

headinglabel=Label(root,text='Retail billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headinglabel.pack(fill=X)
customer_details_frame=LabelFrame(root,text='customer details',font=('times new roman',12,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)
namelabel=Label(customer_details_frame,text='Name',font=('times new roman',12,'bold'),bg='gray20',fg='white')
namelabel.grid(row=0,column=0,padx=20,pady=2)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)
phonelabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)
billnumberlabel=Label(customer_details_frame,text='bill number',font=('times new roman',12,'bold'),bg='gray20',fg='white')
billnumberlabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',12),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)
searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=10)

productsFrame=Frame(root)
productsFrame.pack(fill=X)
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetic',font=('times new roman',14,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)



bathsoaplabel=Label(cosmeticsFrame,text='Bathsoap',font=('times new roman',14,'bold'),bg='gray20',fg='white')
bathsoaplabel.grid(row=0,column=0,pady=5,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=5,padx=10)
bathsoapEntry.insert(0,0)

facecreamlabel=Label(cosmeticsFrame,text='facecream',font=('times new roman',14,'bold'),bg='gray20',fg='white')
facecreamlabel.grid(row=1,column=0,pady=5,sticky='w')
facecreamlabelEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
facecreamlabelEntry.grid(row=1,column=1,pady=5,padx=10)
facecreamlabelEntry.insert(0,0)

facewashlabel=Label(cosmeticsFrame,text='face wash',font=('times new roman',14,'bold'),bg='gray20',fg='white')
facewashlabel.grid(row=2,column=0,pady=5,sticky='w')
facewashlabelEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
facewashlabelEntry.grid(row=2,column=1,pady=5)
facewashlabelEntry.insert(0,0)

hairspraylabel=Label(cosmeticsFrame,text='hair spray',font=('times new roman',14,'bold'),bg='gray20',fg='white')
hairspraylabel.grid(row=3,column=0,pady=5,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=5)
hairsprayEntry.insert(0,0)

hairgellabel=Label(cosmeticsFrame,text='hair gel',font=('times new roman',14,'bold'),bg='gray20',fg='white')
hairgellabel.grid(row=4,column=0,pady=5,sticky='w')
hairgellabelEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
hairgellabelEntry.grid(row=4,column=1,pady=5)
hairgellabelEntry.insert(0,0)

bodylotionlabel=Label(cosmeticsFrame,text='body lotion',font=('times new roman',14,'bold'),bg='gray20',fg='white')
bodylotionlabel.grid(row=5,column=0,pady=5,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',14,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=5)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',14,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

ricelabel=Label(groceryFrame,text='rice',font=('times new roman',14,'bold'),bg='gray20',fg='white')
ricelabel.grid(row=0,column=0,pady=5,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=5)
riceEntry.insert(0,0)

oillabel=Label(groceryFrame,text='oil',font=('times new roman',14,'bold'),bg='gray20',fg='white')
oillabel.grid(row=1,column=0,pady=5,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=5)
oilEntry.insert(0,0)

daallabel=Label(groceryFrame,text='daal',font=('times new roman',14,'bold'),bg='gray20',fg='white')
daallabel.grid(row=2,column=0,pady=5,sticky='w')
daalEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=5)
daalEntry.insert(0,0)

wheetlabel=Label(groceryFrame,text='wheet',font=('times new roman',14,'bold'),bg='gray20',fg='white')
wheetlabel.grid(row=3,column=0,pady=5,sticky='w')
wheetEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
wheetEntry.grid(row=3,column=1,pady=5)
wheetEntry.insert(0,0)

sugarlabel=Label(groceryFrame,text='sugar',font=('times new roman',14,'bold'),bg='gray20',fg='white')
sugarlabel.grid(row=4,column=0,pady=5,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=5)
sugarEntry.insert(0,0)

tealabel=Label(groceryFrame,text='tea',font=('times new roman',14,'bold'),bg='gray20',fg='white')
tealabel.grid(row=5,column=0,pady=5,sticky='w')
teaEntry=Entry(groceryFrame,font=('times new roman',14,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=5)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Cold drinks',font=('times new roman',14,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

fantalabel=Label(drinksFrame,text='fanta',font=('times new roman',14,'bold'),bg='gray20',fg='white')
fantalabel.grid(row=0,column=0,pady=5,sticky='w')
fantaEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
fantaEntry.grid(row=0,column=1,pady=5)
fantaEntry.insert(0,0)

pepsilabel=Label(drinksFrame,text='pepsi',font=('times new roman',14,'bold'),bg='gray20',fg='white')
pepsilabel.grid(row=1,column=0,pady=5,sticky='w')
pepsiEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=5)
pepsiEntry.insert(0,0)

spritlabel=Label(drinksFrame,text='sprit',font=('times new roman',14,'bold'),bg='gray20',fg='white')
spritlabel.grid(row=2,column=0,pady=5,sticky='w')
spritEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
spritEntry.grid(row=2,column=1,pady=5)
spritEntry.insert(0,0)

Milklabel=Label(drinksFrame,text='Milk',font=('times new roman',14,'bold'),bg='gray20',fg='white')
Milklabel.grid(row=3,column=0,pady=5,sticky='w')
MilkEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
MilkEntry.grid(row=3,column=1,pady=5)
MilkEntry.insert(0,0)

frootilabel=Label(drinksFrame,text='frooti',font=('times new roman',14,'bold'),bg='gray20',fg='white')
frootilabel.grid(row=4,column=0,pady=5,sticky='w')
frootiEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=5)
frootiEntry.insert(0,0)

cococolalabel=Label(drinksFrame,text='cococola',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cococolalabel.grid(row=5,column=0,pady=5,sticky='w')
cococolaEntry=Entry(drinksFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=5)
cococolaEntry.insert(0,0)

billframe=Label(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text='Bill area',font=('times new roman',14,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

Scrollbar=Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=55,yscrollcommand=Scrollbar.set)
textarea.pack()

Scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack(fill=X)

cosmeticpricelabel=Label(billmenuFrame,text='cosmeticprice',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticpricelabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=5,padx=10)

grocerypricelabel=Label(billmenuFrame,text='grocery price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypricelabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=5,padx=10)

drinkspricelabel=Label(billmenuFrame,text='cold drink price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkspricelabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=5,padx=10)

cosmetictaxlabel=Label(billmenuFrame,text='cosmetictax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmetictaxlabel.grid(row=0,column=2,pady=5,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=5,padx=10)

grocerytaxlabel=Label(billmenuFrame,text='grocery tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxlabel.grid(row=1,column=2,pady=5,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=5,padx=10)

drinkstaxlabel=Label(billmenuFrame,text='cold drinks tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkstaxlabel.grid(row=2,column=2,pady=5,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=5,padx=10)

buttonframe=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,text='Total',font=('arial',12,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonframe,text='Bill',font=('arial',12,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonframe,text='Email',font=('arial',12,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonframe,text='Print',font=('arial',12,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonframe,text='Clear',font=('arial',12,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)




root.mainloop()