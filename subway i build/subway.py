


count_turkey=1
count_peri=1
count_fajita=1
count_drink=1
count_coffe=1
count_Veggie=1
count_Sweetonion=1

total_name=[]
total_price=[]
class sandwiches:              ############## CLASSS SANDWICHES #############
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


class beverages :
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



class salads :
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








class product(sandwiches,beverages,salads):
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

        if re.match( '\d+' , self.Name ) or re.match( '\w+\d+' , self.Name ):                ############# checking of input field name  that user should enter name  not number and alphanumeric
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









