import tkinter
import os
from tkinter import * ######### for gui #####
from PIL import ImageTk, Image ######## for inputing image
import re ###################### for checking of input fields
import random              ##### for barcode
from xlwt import Workbook
wb=Workbook()
sheet=wb.add_sheet("sheet 2")




costomer=[]
coutomer_phone=[]

employess=[]
employess_password=[]
count_turkey=1
count_peri=1
count_fajita=1
count_drink=1
count_coffe=1
count_Veggie=1
count_Sweetonion=1
total_name=[]
total_price=[]
class sandwiches:              ############## CLASSS SANDWICHES
    turkey_breast="turkey breast "
    turkey_price=650
    peri_peri = "peri peri chicken "
    peri_peri_price = 650
    Fajita_sensation= "FajitaSensation"
    Fajita_sensation_price = 650
    def turkey_breast1( self ):
        total_name.append(self.turkey_breast)
        total_price.append(self.turkey_price)
    def peri_peri1( self ):
        total_name.append(self.peri_peri)
        total_price.append(self.peri_peri_price)
    def Fajita_sensation1( self ):
        total_name.append ( self.Fajita_sensation )
        total_price.append ( self.Fajita_sensation_price)


class beverages :                   ##### class beverages
    drink = "Drinks"
    drink_price = 120
    coffe = "COFFE"
    coffe_price = 190

    def drink_ ( self ) :
        total_name.append ( self.drink )
        total_price.append ( self.drink_price )

    def coffe_ ( self ) :
        total_name.append ( self.coffe )
        total_price.append ( self.coffe_price )



class salads :                            ######### classss salads
    sweetonion= "Sweet Onion"
    sweetonion_price = 340
    Veggie_delight = "Veggie Delight"
    Veggie_delight_price = 340

    def veggie_ ( self ) :
        total_name.append ( self.Veggie_delight )
        total_price.append ( self.Veggie_delight_price )

    def sweet_ ( self ) :
        total_name.append ( self.sweetonion )
        total_price.append ( self.sweetonion_price )


class product(sandwiches,beverages,salads):   ############# classes product
    pass


class Employer:
    employe=["umer khan","umair ullah"," syed muhammad zaid "]
    def __init__(self):
        self.Name=""
        self.password=""

    def confirmation( self ):

        if self.Name in self.employe:
            Label ( frame1 , text="✓" , bg="yellow" , fg="green" ,font=("Heveltica" , 10) ).grid ( row=2 , column=2 )
            Label ( frame1 , text="✓" , bg="yellow" , fg="green" , font=("Heveltica" , 10) ).grid ( row=3 , column=2 )
            employess.append ( self.Name )
            employess_password.append ( self.password )

        elif self.Name not in self.employe :
            Label ( frame1 , text="x" , bg="yellow" , fg="red"  ,font=("Heveltica" , 10) ).grid ( row=2 , column=2)
            Label ( frame1 , text="x" , bg="yellow" , fg="red" , font=("Heveltica" , 10) ).grid ( row=3 , column=2 )

        employess.append(self.Name)

        employess_password.append(self.password)

    def cheking_Name_field( self ):

        if re.match( "\d+" , self.Name ) or re.match( '\w+\d+' , self.Name ):                ############# checking of input field name  that user should enter name  not number and alphanumeric
            Label ( frame1 , text="please insert name not number" , bg="yellow" , fg="red" , font=("Heveltica" , 10) ).grid ( row=10 , column=0,columnspan=2)
        else:
            Label ( frame1 , text="                                                   " , bg="yellow" , fg="yellow" ,font=("Heveltica" , 10) ).grid ( row=10 , column=0 , columnspan=2 )





class Coustomer_class:
    def __init__ ( self ) :
        self.coustmerName = ""
        self.coustmerphone = ""

    def cheking_Name_field_costomer_field( self ):

        if re.match( '\d+' , self.coustmerName ) or re.match( '\w+\d+' , self.coustmerName ):                ############# checking of input field name  that user should enter name  not number and alphanumeric
            Label ( frame1 , text="x" , bg="yellow" , fg="red" , font=("Heveltica" , 10) ).grid ( row=5 , column=2,columnspan=2)
        else:
            Label ( frame1 , text="✓" , bg="yellow" , fg="green" , font=("Heveltica" , 10) ).grid ( row=5 , column=2 , columnspan=2 ) ######checking#######
            costomer.clear()
            coutomer_phone.clear()
            costomer.append(self.coustmerName) ###### this will add the  input field 3 coustomer Name to global list
            coutomer_phone.append(self.coustmerphone) ############## thiss will
            Label ( frame1 , text=" coutomer name " , bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=11 , column=0 , padx=20 , pady=10 )
            Label ( frame1 , text=" phone.No " , bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid (row=12 , column=0 , padx=20 , pady=10 )
            Label ( frame1 , text=self.coustmerName , bg="yellow" , fg="black" ,
                    font=("Heveltica" , 10) ).grid ( row=11 , column=1)
            Label ( frame1 , text=self.coustmerphone , bg="yellow" , fg="black" ,
                    font=("Heveltica" , 10) ).grid ( row=12 , column=1 )









































































































def turkey_breast_button():################### BUTTON FUNCTION TURKEY  ############
    global count_turkey
    object1=product()
    Label(frame3,text=object1.turkey_breast,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=0,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.turkey_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=0,column=1,padx=20,pady=5)
    product.turkey_breast1(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_turkey, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=0 ,column=3,padx=40,pady=5)
    count_turkey = count_turkey+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)


def _Peri_peri_button():################### BUTTON FUNCTION TURKEY  ############
    global count_peri
    object1=product()
    Label(frame3,text=object1.peri_peri,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=1,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.turkey_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=1,column=1,padx=20,pady=5)
    product.peri_peri1(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_peri, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=1 ,column=3,padx=40,pady=5)
    count_peri = count_peri+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)


def Fajita_sensation_button():################### BUTTON FUNCTION TURKEY  ############
    global count_fajita
    object1=product()
    Label(frame3,text=object1.Fajita_sensation,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=2,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.Fajita_sensation_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=2,column=1,padx=20,pady=5)
    product.Fajita_sensation1(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_fajita, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=2 ,column=3,padx=40,pady=5)
    count_fajita = count_fajita+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)


def Drinks_():################### BUTTON FUNCTION Drinks ############
    global count_drink
    object1=product()
    Label(frame3,text=object1.drink,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=3,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.drink_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=3,column=1,padx=20,pady=5)
    product.drink_(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_drink, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=3 ,column=3,padx=40,pady=5)
    count_drink = count_drink+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)

def coffe_button():################### BUTTON FUNCTION Drinks  ############
    global count_coffe
    object1=product()
    Label(frame3,text=object1.coffe,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=4,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.coffe_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=4,column=1,padx=20,pady=5)
    product.coffe_(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_coffe, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=4 ,column=3,padx=40,pady=5)
    count_coffe = count_coffe+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)





def Sweet_onion():################### BUTTON FUNCTION Drinks  ############
    global count_Sweetonion
    object1=product()
    Label(frame3,text=object1.sweetonion,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=5,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.sweetonion_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=5,column=1,padx=20,pady=5)
    product.sweet_(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_Sweetonion, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=5 ,column=3,padx=40,pady=5)
    count_Sweetonion = count_Sweetonion+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)





def Veggie_button():################### BUTTON FUNCTION Drinks  ############
    global count_Veggie
    object1=product()
    Label(frame3,text=object1.Veggie_delight,bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=6,column=0,padx=20,pady=5)
    Label ( frame3 , text=str(object1.Veggie_delight_price)+"rs",bg="yellow",fg="black",font=("Helvetica", 10) ).grid(row=6,column=1,padx=20,pady=5)
    product.veggie_(object1)
    Label ( frame3 , text="total",bg="yellow",fg="black",font=("Helvetica", 18)).grid(row=10,column=0,padx=20,pady=20 )
    Label ( frame3 , text=count_Veggie, bg="yellow" , fg="black" , font=("Helvetica" , 10) ).grid ( row=6 ,column=3,padx=40,pady=5)
    count_Veggie = count_Veggie+1


    for i in range(len(total_name)):
        Label(frame3,text=sum(total_price),bg="yellow",fg="black",font=("Helvetica", 10)).grid(row=10,column=1,padx=20,pady=20)





def confirm_():
    x=Employer()
    x.Name=entry.get()
    x.password=entry2.get()
    x.confirmation()
    x.cheking_Name_field()
    y=Coustomer_class()
    y.coustmerName=entry3.get()
    y.coustmerphone=entry4.get()
    y.cheking_Name_field_costomer_field()


def checkout():
    global w
    w='#'+str(random.randrange(0,10000))

    frame4 = Frame ( root , bd=4 , relief="ridge" , bg="yellow" )

    frame4.place ( x=1200 , y=400 , width=550 , height=400 )
    Label( frame4 , text=" RECIPT" , bg="yellow" , fg="black" , font=("Heveltica" , 16) ).grid ( row=0 , column=2,padx=10 , pady=3 )
    Label ( frame4 , text=" Costomer" , bg="yellow" , fg="black" , font=("Heveltica" , 16) ).grid ( row=1 , column=2 ,padx=10 , pady=3 )
    Label ( frame4 , text=" Costomer.ph" , bg="yellow" , fg="black" , font=("Heveltica" , 16) ).grid ( row=2 , column=2 ,padx=10 , pady=3 )
    Button( frame4 , text="print" , bg="green" , fg="white" , font=("Heveltica" , 11),command=print_recipt).grid ( row=3 ,column=2 ,padx=10 ,pady=3 )
    Label ( frame4 , text=w , bg="yellow" , fg="black" , font=("Heveltica" , 16) ).grid ( row=0 , column=3 , padx=10 , pady=3 )

    Label ( frame4 , text=costomer[0] , bg="yellow" , fg="black" , font=("Helvetica" , 15) ).grid ( row=1 , column=3 ,padx=3 , pady=3 )
    Label ( frame4 , text=coutomer_phone[0] , bg="yellow" , fg="black" , font=("Helvetica" , 15) ).grid ( row=2 ,column=3 ,padx=3 ,pady=3 )

    for i in range(0,len(total_name)+1):
        try:
            Label ( frame4 , text=total_name[i] , bg="yellow" , fg="black" , font=("Helvetica" , 16) ).grid ( row=[i] , column=0, padx=10 , pady=3 )
            Label ( frame4 , text=total_price[i] , bg="yellow" , fg="black" , font=("Heveltica" , 16) ).grid ( row=[i] , column=1 ,padx=10 ,pady=3 )
            Label ( frame4 , text=sum ( total_price ) , bg="yellow" , fg="black" , font=("Helvetica" , 16) ).grid ( row=10 , column=1 ,padx=10 , pady=15 )
            Label ( frame4 , text="total" , bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=10 , column=0, padx=10 , pady=15 )
        except:
            print("all thing are pure")


def print_recipt():
    sheet.write(1,5,".......SUBWAY......")
    sheet.write ( 2 , 7 , "customer Name" )
    sheet.write ( 2 , 9 , costomer[0] )
    sheet.write ( 4 , 7 , "customer phone" )
    sheet.write ( 4 , 9 , coutomer_phone[0] )
    sheet.write ( 13 , 7 , " total " )
    sheet.write ( 13 , 8 , sum ( total_price ) )

    sheet.write ( 2 , 4 , "RECIPT" )
    sheet.write ( 2 , 6 , w )
    for i in range(0,len(total_name)):

        sheet.write(i+5,4,total_name[i])
        sheet.write(i+5,6,total_price[i])
        wb.save("subway excel sheet.xls")

    os.startfile('D:/usman_home/subway i build/subway excel sheet','print')









































root=Tk()
root.title("Subway")
root.geometry("1920x1080")
root.configure(bg="green")

title=Label(root,text=" SUBWAY POS ",bg="white",fg="black",font=("Times", 40,"bold italic"))
title.place(x=600,y=20)
frame1=Frame(root,bd=4,relief="ridge",bg="yellow")
frame1.place(x=45,y=54,width=380,height=800)

frame_top_title=Label(frame1,text=" Credential ",bg="yellow",fg="black",font=("Helvetica", 16))
frame_top_title.grid(row=0,columnspan=2,padx=45,pady=10)

frame_top_title_sub=Label(frame1,text=" EMPLOYER LOGIN ",bg="yellow",fg="black",font=("Helvetica", 13))
frame_top_title_sub.grid(row=1,columnspan=2,padx=45,pady=10)

frame_top_title_sub=Label(frame1,text="Coustomer",bg="yellow",fg="black",font=("Helvetica", 13))
frame_top_title_sub.grid(row=4,columnspan=2,padx=45,pady=10)






label1=Label(frame1,text="NAME ",bg="yellow",fg="black",font=("Helvetica", 10))
label1.grid(row=2,column=0,padx=20,pady=10)
entry=Entry(frame1)
entry.grid(row=2,column=1,padx=20,pady=10)

label2=Label(frame1,text="PASSWORD ",bg="yellow",fg="black",font=("Helvetica", 10))
label2.grid(row=3,column=0,padx=20,pady=10)
entry2=Entry(frame1)
entry2.grid(row=3,column=1,padx=20,pady=10)

label3=Label(frame1,text=" coutomer name ",bg="yellow",fg="black",font=("Helvetica", 10))
label3.grid(row=5,column=0,padx=20,pady=10)
entry3=Entry(frame1)
entry3.grid(row=5,column=1,padx=20,pady=10)

label3=Label(frame1,text=" PHONE.NO ",bg="yellow",fg="black",font=("Helvetica", 10))
label3.grid(row=6,column=0,padx=20,pady=10)
entry4=Entry(frame1)
entry4.grid(row=6,column=1,padx=20,pady=10)

button1=Button(frame1,text=" CONFIRM ",bg="green",fg="white",command=confirm_)
button1.grid(row=7,column=1,padx=20,pady=10)



#### NEXT FRAME WORK THE BIGGER FRAME ##################################
#### BURGER #####
frame2=Frame(root,bd=4,relief="ridge",bg="yellow")
frame2.place(x=500,y=125,width=1300,height=800)


img_turkey= ImageTk.PhotoImage(Image.open("BBQ-Chicken.jpg"))  #### MAKKING OF TUREKY BREAST
panel = Label(frame2, image = img_turkey,width="200px",height="80px")
panel.grid(row=1,column=0,columnspan=2, padx=30,pady=20)

label_turkeybreast=Label(frame2,text="Price:650RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_turkeybreast.grid(row=2,column=0,columnspan=2,padx=30,pady=10)

button_turkey=Button(frame2,text=" Turkey breast ",bg="green",fg="white",command=turkey_breast_button)
button_turkey.grid(row=3,column=0,columnspan=2,padx=30,pady=10)


img_fajita = ImageTk.PhotoImage(Image.open("Fajita.jpg")) ########### MAKING OF FAJITA
panel = Label(frame2, image = img_fajita,width="200px",height="80px")
panel.grid(row=1,column=3,columnspan=2, padx=60,pady=20)
label_fajita=Label(frame2,text="Price:650RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_fajita.grid(row=2,column=3,columnspan=2,padx=60,pady=10)
button_fajita=Button(frame2,text=" Fajita SENSATION",bg="green",fg="white",command=Fajita_sensation_button)
button_fajita.grid(row=3,column=3,columnspan=2,padx=60,pady=10)


img_Perri = ImageTk.PhotoImage(Image.open("Peri-Peri.jpg")) ###### MAKING OF PERI PERI
panel = Label(frame2, image = img_Perri,width="200px",height="80px")
panel.grid(row=1,column=5,columnspan=2, padx=60,pady=20)
label_peri=Label(frame2,text="Price:650RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_peri.grid(row=2,column=5,columnspan=2,padx=60,pady=10)
button_peri=Button(frame2,text="Peri PERI chicken",bg="green",fg="white",command=_Peri_peri_button)
button_peri.grid(row=3,column=5,columnspan=2,padx=60,pady=10)


#########     Beverages   ####################


img_Drinks= ImageTk.PhotoImage(Image.open("DRINKS.jpg")) ############ MAKING OF DRINKS
panel = Label(frame2, image = img_Drinks,width="200px",height="80px")
panel.grid(row=4,column=0,columnspan=2, padx=30,pady=20)

label_Drinks=Label(frame2,text="Price:120RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_Drinks.grid(row=5,column=0,columnspan=2,padx=30,pady=10)

button_Drinks=Button(frame2,text=" DRINKS ",bg="green",fg="white",command=Drinks_)
button_Drinks.grid(row=6,column=0,columnspan=2,padx=30,pady=10)


img_coffe = ImageTk.PhotoImage(Image.open("COFFE.jpg")) ########### MAKING OF COFFE
panel = Label(frame2, image = img_coffe,width="200px",height="80px")
panel.grid(row=4,column=3,columnspan=2, padx=60,pady=20)
label_coffe=Label(frame2,text="Price:190RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_coffe.grid(row=5,column=3,columnspan=2,padx=60,pady=10)
button_coffe=Button(frame2,text=" COFFE ",bg="green",fg="white",command=coffe_button)
button_coffe.grid(row=6,column=3,columnspan=2,padx=60,pady=10)

######################## SALADS ###################

img_Veggie= ImageTk.PhotoImage(Image.open("Veggie.jpg")) ############ MAKING OF VEGGIE DELIGHT
panel = Label(frame2, image = img_Veggie,width="200px",height="80px")
panel.grid(row=7,column=0,columnspan=2, padx=30,pady=20)

label_veggie=Label(frame2,text="Price:340RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_veggie.grid(row=8,column=0,columnspan=2,padx=30,pady=10)

button_veggie=Button(frame2,text=" VEGGIE DELIGHT ",bg="green",fg="white",command=Veggie_button)
button_veggie.grid(row=9,column=0,columnspan=2,padx=30,pady=10)



img_sweetonion = ImageTk.PhotoImage(Image.open("SweetOnion.jpg")) ########### MAKING OF Sweet onion
panel = Label(frame2, image = img_sweetonion,width="200px",height="80px")
panel.grid(row=7,column=3,columnspan=2, padx=60,pady=20)
label_sweetonion=Label(frame2,text="Price:340RS",bg="yellow",fg="black",font=("Helvetica", 10))
label_sweetonion.grid(row=8,column=3,columnspan=2,padx=60,pady=10)
button_sweetonion=Button(frame2,text=" Sweet_onion ",bg="green",fg="white",command=Sweet_onion)
button_sweetonion.grid(row=9,column=3,columnspan=2,padx=60,pady=10)






##################### Frame3 recipt counter##################################




frame3=Frame(root,bd=4,relief="ridge",bg="yellow")          #### MAKING OF FRAME3
frame3.place(x=1200,y=400,width=550,height=400)              #### frame 3 size and dimension
Label ( frame3 , text="turkey breast", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=0 , column=0,padx=20,pady=5)
Label ( frame3 , text="Peri-Peri", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=1 , column=0,padx=20,pady=5)
Label ( frame3 , text="fajita sensation", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=2 , column=0,padx=20,pady=5)
Label ( frame3 , text="Drinks", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=3 , column=0,padx=20,pady=5)
Label ( frame3 , text="COFFE", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=4, column=0,padx=20,pady=5)
Label ( frame3 , text="SweetOnion", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=5 , column=0,padx=20,pady=5)
Label ( frame3 , text="Veggie_delight", bg="yellow" , fg="black" , font=("Helvetica" , 18) ).grid ( row=6 , column=0,padx=20,pady=5)
checkout=Button(frame3,text="checkout",bg="green",fg="white",command=checkout)    # building a checout button
checkout.grid(row=10,column=3,columnspan=2,padx=30,pady=10)           ### placeing of that buuton












root.mainloop()